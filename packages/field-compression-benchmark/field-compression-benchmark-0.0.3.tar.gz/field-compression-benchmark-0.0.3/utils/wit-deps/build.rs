use std::{
    fs,
    io::{self, Write},
    os::unix::fs::OpenOptionsExt,
    path::PathBuf,
    process::Command,
};

const WIT_DEPS_VERSION_FULL: &str = "0.3.5";

fn main() -> io::Result<()> {
    let out_dir = PathBuf::from(std::env::var_os("OUT_DIR").ok_or_else(|| {
        io::Error::new(io::ErrorKind::NotFound, "missing env variable `OUT_DIR`")
    })?)
    .canonicalize()?;

    let wit_deps_bin = download_from_url(&format!("https://github.com/bytecodealliance/wit-deps/releases/download/v{WIT_DEPS_VERSION_FULL}/wit-deps-x86_64-unknown-linux-musl"))?;
    let wit_deps_path = out_dir.join("wit-deps");

    let mut wit_deps_file = fs::File::options()
        .mode(0o755)
        .write(true)
        .create(true)
        .truncate(true)
        .open(&wit_deps_path)?;
    wit_deps_file.write_all(&wit_deps_bin)?;
    wit_deps_file.flush()?;

    println!(
        "cargo::rustc-env=WIT_DEPS_BINARY={}",
        wit_deps_path.display()
    );

    Ok(())
}

fn download_from_url(url: &str) -> io::Result<Vec<u8>> {
    // We need to use wget instead of reqwest here
    //  since building reqwest inside pyodide-build fails
    let mut cmd = Command::new("wget");
    cmd.arg("-qO-").arg(url);

    let output = cmd.output()?;
    if !output.status.success() {
        return Err(io::Error::new(
            io::ErrorKind::Other,
            format!(
                "wget exited with code {}:\n{}",
                output.status,
                String::from_utf8_lossy(&output.stderr),
            ),
        ));
    }

    Ok(output.stdout)
}
