use std::{fmt, io::Write, sync::OnceLock};

use wasm_component_layer::{
    AsContextMut, Func, FuncType, InterfaceIdentifier, Linker, ListType, PackageIdentifier,
    PackageName, ResultType, ResultValue, Value, ValueType,
};

pub fn add_to_linker(linker: &mut Linker, mut ctx: impl AsContextMut) -> Result<(), anyhow::Error> {
    let FcBenchStdioInterface {
        stdio: fcbench_stdio_interface,
    } = FcBenchStdioInterface::get();

    let fcbench_stdio_instance = linker.define_instance(fcbench_stdio_interface.clone())?;

    let result_ty = ResultType::new(Some(ValueType::U8), Some(ValueType::String));

    fcbench_stdio_instance.define_func(
        "write-stdout",
        OutputStream::Stdout.create_write_func(ctx.as_context_mut(), result_ty.clone()),
    )?;
    fcbench_stdio_instance.define_func(
        "flush-stdout",
        OutputStream::Stdout.create_flush_func(ctx.as_context_mut(), result_ty.clone()),
    )?;
    fcbench_stdio_instance.define_func(
        "write-stderr",
        OutputStream::Stderr.create_write_func(ctx.as_context_mut(), result_ty.clone()),
    )?;
    fcbench_stdio_instance.define_func(
        "flush-stderr",
        OutputStream::Stderr.create_flush_func(ctx.as_context_mut(), result_ty),
    )?;

    Ok(())
}

#[derive(Copy, Clone)]
enum OutputStream {
    Stdout,
    Stderr,
}

impl OutputStream {
    fn create_write_func(self, ctx: impl AsContextMut, result_ty: ResultType) -> Func {
        Func::new(
            ctx,
            FuncType::new(
                [ValueType::List(ListType::new(ValueType::U8))],
                [ValueType::Result(result_ty.clone())],
            ),
            move |_ctx, args, results| {
                let [Value::List(contents)] = args else {
                    anyhow::bail!("invalid fcbench:wasi/stdio#write-{self} arguments");
                };
                let Ok(contents) = contents.typed::<u8>() else {
                    anyhow::bail!("invalid fcbench:wasi/stdio#write-{self} argument type");
                };

                let [result] = results else {
                    anyhow::bail!("invalid fcbench:wasi/stdio#write-{self} results");
                };

                *result = Value::Result(ResultValue::new(
                    result_ty.clone(),
                    match match self {
                        Self::Stdout => std::io::stdout().write_all(contents),
                        Self::Stderr => std::io::stderr().write_all(contents),
                    } {
                        Ok(()) => Ok(Some(Value::U8(0))),
                        Err(err) => Err(Some(Value::String(format!("{err}").into()))),
                    },
                )?);

                Ok(())
            },
        )
    }

    fn create_flush_func(self, ctx: impl AsContextMut, result_ty: ResultType) -> Func {
        Func::new(
            ctx,
            FuncType::new([], [ValueType::Result(result_ty.clone())]),
            move |_ctx, args, results| {
                anyhow::ensure!(
                    args.is_empty(),
                    "invalid fcbench:wasi/stdio#flush-{self} arguments"
                );

                let [result] = results else {
                    anyhow::bail!("invalid fcbench:wasi/stdio#flush-{self} results");
                };

                *result = Value::Result(ResultValue::new(
                    result_ty.clone(),
                    match match self {
                        Self::Stdout => std::io::stdout().flush(),
                        Self::Stderr => std::io::stderr().flush(),
                    } {
                        Ok(()) => Ok(Some(Value::U8(0))),
                        Err(err) => Err(Some(Value::String(format!("{err}").into()))),
                    },
                )?);

                Ok(())
            },
        )
    }
}

impl fmt::Display for OutputStream {
    fn fmt(&self, fmt: &mut fmt::Formatter) -> fmt::Result {
        fmt.write_str(match self {
            Self::Stdout => "stdout",
            Self::Stderr => "stderr",
        })
    }
}

#[non_exhaustive]
pub struct FcBenchStdioInterface {
    pub stdio: InterfaceIdentifier,
}

impl FcBenchStdioInterface {
    #[must_use]
    pub fn get() -> &'static Self {
        static FCBENCH_STDIO_INTERFACE: OnceLock<FcBenchStdioInterface> = OnceLock::new();

        FCBENCH_STDIO_INTERFACE.get_or_init(|| Self {
            stdio: InterfaceIdentifier::new(
                PackageIdentifier::new(
                    PackageName::new("fcbench", "wasi"),
                    Some(semver::Version::new(0, 2, 0)),
                ),
                "stdio",
            ),
        })
    }
}
