use std::{
    fs, io,
    path::{Path, PathBuf},
    process::Command,
};

#[allow(clippy::missing_errors_doc)]
pub fn lock_wit_dependencies() -> Result<(), io::Error> {
    let Some(out_dir) = std::env::var_os("OUT_DIR") else {
        return Err(io::Error::new(
            io::ErrorKind::NotFound,
            "build script requires `OUT_DIR` env variable",
        ));
    };

    let deps_path_out = PathBuf::from(out_dir).join("wit").join("deps");
    eprintln!("Trying to create {deps_path_out:?} ...");
    fs::create_dir_all(&deps_path_out)?;
    let deps_path_out = deps_path_out.canonicalize()?;

    let status = Command::new(env!("WIT_DEPS_BINARY"))
        .arg("--deps")
        .arg(&deps_path_out)
        .arg("lock")
        .status()?;

    if !status.success() {
        return Err(io::Error::new(
            io::ErrorKind::Other,
            "wit-deps failed to execute",
        ));
    }

    let deps_path = Path::new("wit").join("deps");
    eprintln!("Trying to symlink to {deps_path:?} ...");
    if fs::read_link(&deps_path).is_ok() {
        fs::remove_file(&deps_path)?;
    }
    std::os::unix::fs::symlink(deps_path_out, deps_path)?;

    println!("cargo::rerun-if-changed=wit/deps.lock");
    println!("cargo::rerun-if-changed=wit/deps.toml");

    Ok(())
}
