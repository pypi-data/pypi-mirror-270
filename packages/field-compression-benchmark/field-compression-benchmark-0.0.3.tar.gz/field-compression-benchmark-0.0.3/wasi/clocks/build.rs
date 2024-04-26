fn main() -> std::io::Result<()> {
    wit_deps::lock_wit_dependencies()?;

    println!("cargo::rerun-if-changed=../wit");

    Ok(())
}
