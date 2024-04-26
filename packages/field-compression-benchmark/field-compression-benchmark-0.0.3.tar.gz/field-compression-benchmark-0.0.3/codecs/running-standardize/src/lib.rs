#![allow(clippy::missing_errors_doc)]
#![cfg_attr(not(test), no_main)]

use rolling_stats::Stats;

pub fn running_standardize<T: Float>(data: &[T]) -> Vec<T> {
    let mut stats = Stats::<T>::new();

    data.iter()
        .copied()
        .map(|x| {
            let stddev = if stats.std_dev.is_zero() {
                T::one()
            } else {
                stats.std_dev
            };
            let x2 = (x - stats.mean) / stddev;

            if x.is_finite() && x2.is_finite() {
                stats.update(x);
            }

            x2
        })
        .collect()
}

pub fn running_destandardize<T: Float>(data: &[T]) -> Vec<T> {
    let mut stats = Stats::<T>::new();

    data.iter()
        .copied()
        .map(|x2| {
            let stddev = if stats.std_dev.is_zero() {
                T::one()
            } else {
                stats.std_dev
            };
            let x = (x2 * stddev) + stats.mean;

            if x2.is_finite() && x.is_finite() {
                stats.update(x);
            }

            x
        })
        .collect()
}

#[derive(Clone, serde::Serialize, serde::Deserialize)]
pub struct RunningStandardizeCodec {
    // empty
}

impl codecs_core::Codec for RunningStandardizeCodec {
    type DecodedBuffer = codecs_core::VecBuffer;
    type EncodedBuffer = codecs_core::VecBuffer;

    const CODEC_ID: &'static str = "running-standardize";

    fn from_config<'de, D: serde::Deserializer<'de>>(config: D) -> Result<Self, D::Error> {
        serde::Deserialize::deserialize(config)
    }

    fn encode(
        &self,
        buf: codecs_core::BufferSlice,
        shape: &[usize],
    ) -> Result<codecs_core::ShapedBuffer<Self::EncodedBuffer>, String> {
        let encoded = match buf {
            codecs_core::BufferSlice::F32(data) => {
                codecs_core::BufferVec::F32(running_standardize(data))
            },
            codecs_core::BufferSlice::F64(data) => {
                codecs_core::BufferVec::F64(running_standardize(data))
            },
            buf => {
                return Err(format!(
                    "RunningStandardize::encode does not support the buffer dtype `{}`",
                    buf.ty(),
                ))
            },
        };

        Ok(codecs_core::ShapedBuffer {
            shape: Vec::from(shape),
            buffer: encoded,
        })
    }

    fn decode(
        &self,
        buf: codecs_core::BufferSlice,
        shape: &[usize],
    ) -> Result<codecs_core::ShapedBuffer<Self::DecodedBuffer>, String> {
        let decoded = match buf {
            codecs_core::BufferSlice::F32(data) => {
                codecs_core::BufferVec::F32(running_destandardize(data))
            },
            codecs_core::BufferSlice::F64(data) => {
                codecs_core::BufferVec::F64(running_destandardize(data))
            },
            buf => {
                return Err(format!(
                    "RunningStandardize::decode does not support the buffer dtype `{}`",
                    buf.ty(),
                ))
            },
        };

        Ok(codecs_core::ShapedBuffer {
            shape: Vec::from(shape),
            buffer: decoded,
        })
    }

    fn get_config<S: serde::Serializer>(&self, serializer: S) -> Result<S::Ok, S::Error> {
        serde::Serialize::serialize(&self, serializer)
    }
}

codecs_core_wasm::export_codec! {
    /// RunningStandardize codec which transforms the data to have zero mean
    /// and unit variance.
    ///
    /// Note that this codec computes the running mean and variance to
    /// standardize each element, i.e. the codec warms up over the first few
    /// elements before the mean and variance estimates stabilise. Therefore,
    /// the first few elements will likely be encoded as outliers.
    RunningStandardizeCodec()
}

pub trait Float:
    Copy
    + num_traits::float::Float
    + num_traits::Zero
    + num_traits::One
    + std::ops::AddAssign
    + num_traits::FromPrimitive
    + PartialEq
    + std::fmt::Debug
{
}

impl Float for f32 {}
impl Float for f64 {}
