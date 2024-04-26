#![cfg_attr(not(test), no_main)]

mod environment;
mod exit;
mod stdio;
mod terminal;

#[allow(clippy::missing_safety_doc, clippy::transmute_int_to_bool)]
mod bindings {
    wit_bindgen::generate!("fcbench:wasi/virtual-cli");
}

pub enum VirtCli {}

#[cfg(target_arch = "wasm32")]
#[allow(unsafe_code)]
mod export {
    use crate::VirtCli;
    crate::bindings::export!(VirtCli with_types_in crate::bindings);
}
