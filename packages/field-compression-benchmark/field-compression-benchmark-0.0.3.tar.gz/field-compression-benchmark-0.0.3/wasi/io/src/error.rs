use crate::{
    bindings::exports::wasi::io::error::{Guest as WasiIoError, GuestError},
    VirtIO,
};

impl WasiIoError for VirtIO {
    type Error = VirtError;
}

pub struct VirtError {
    err: String,
}

impl GuestError for VirtError {
    fn to_debug_string(&self) -> String {
        self.err.clone()
    }
}

impl VirtError {
    #[must_use]
    pub const fn new(err: String) -> Self {
        Self { err }
    }
}
