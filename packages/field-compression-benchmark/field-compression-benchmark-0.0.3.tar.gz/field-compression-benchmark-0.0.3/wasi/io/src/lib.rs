#![cfg_attr(not(test), no_main)]

use crate::bindings::exports::wasi::{
    io::{
        poll::Pollable,
        streams::{InputStream, OutputStream},
    },
    null::io::Guest as WasiVirtNullIO,
};

pub mod error;
pub mod poll;
pub mod streams;

#[allow(clippy::missing_safety_doc)]
mod bindings {
    wit_bindgen::generate!("fcbench:wasi/virtual-io");
}

pub enum VirtIO {}

#[cfg(target_arch = "wasm32")]
#[allow(unsafe_code)]
mod export {
    use crate::VirtIO;
    crate::bindings::export!(VirtIO with_types_in crate::bindings);
}

impl WasiVirtNullIO for VirtIO {
    fn ready_pollable() -> Pollable {
        poll::VirtPollable::ready()
    }

    fn closed_input() -> InputStream {
        streams::VirtInputStream::closed()
    }

    fn output_sink() -> OutputStream {
        streams::VirtOutputStream::sink()
    }

    fn stdout() -> OutputStream {
        streams::VirtOutputStream::stdout()
    }

    fn stderr() -> OutputStream {
        streams::VirtOutputStream::stderr()
    }
}
