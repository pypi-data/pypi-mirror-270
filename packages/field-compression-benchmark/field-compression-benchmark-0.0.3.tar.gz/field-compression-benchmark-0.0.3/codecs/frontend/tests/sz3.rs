use std::path::Path;

use pyo3::{intern, prelude::*, types::IntoPyDict};

#[cfg(all(single_wasm_runtime, feature = "wasmtime"))]
#[test]
#[allow(clippy::missing_errors_doc)]
pub fn main() -> Result<(), PyErr> {
    // create a Python runtime

    use pyo3::exceptions::PyRuntimeError;
    pyo3::prepare_freethreaded_python();

    simple_logger::init_with_level(log::Level::Info)
        .map_err(|err| PyRuntimeError::new_err(format!("failed to install logger: {err}")))?;

    Python::with_gil(|py| -> Result<(), PyErr> {
        let numpy = py.import(intern!(py, "numpy"))?;
        let fcbench = PyModule::new(py, "fcbench")?;

        let codecs = codecs_frontend::init_codecs(py, fcbench)
            .map_err(core_error::LocationError::into_error)?;

        let _sz3_class = codecs_frontend::WasmCodecTemplate::import_codec_class(
            py,
            Path::new("..")
                .join("..")
                .join("data")
                .join("codecs")
                .join("sz3.wasm"),
            codecs,
        )?;

        let globals = [
            (intern!(py, "fcbench"), fcbench),
            (intern!(py, "np"), numpy),
        ]
        .into_py_dict(py);

        py.run(
            r#"
eb_abs = 5.62341325190349e-07
codec = fcbench.codecs.Sz3(eb_mode="abs", eb_abs=eb_abs)

data = np.array([
    6.019042195593153, 5.7760916245613645, -1.0284666644749214, 1.5727866902901886,
    -1.2340438839630905, 0.7767894445014174, 2.659782439485495, 5.560226236111176,
    1.2748576219137917, -4.267278962564942, 1.8548097632045832, -0.5646192258182232,
    7.24354544546497, 2.882656133481929, -4.636650035799854, 4.073543134009759,
    0.7744188215262569, 1.944717921085279, 5.553662637138078, 5.107073824860485,
    -2.487060794890152, -0.2782659775977417, -0.34144259497033824, 9.912700198007123,
    0.9133706206035915, -0.5617508673076727, 5.362177057516491, 6.237931377062622,
    -1.6816032579015052, 2.252819047644973, 8.504477133051891, 6.103788340146005,
    -4.1709318619734805, 3.3273686280150656, 4.897006004942515, 3.2280440425178316,
])

encoded = codec.encode(data)
decoded = codec.decode(encoded)

for da, de in zip(data, decoded):
    assert abs(da - de) <= eb_abs
        "#,
            Some(globals),
            None,
        )?;

        Ok(())
    })?;

    Ok(())
}
