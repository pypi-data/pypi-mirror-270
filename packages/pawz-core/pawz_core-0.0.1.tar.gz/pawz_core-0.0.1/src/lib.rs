use pyo3::prelude::*;
//use pyo3::exceptions::PyValueError;
//use pyo3::types::PyTuple;

/// A Python module implemented in Rust.
#[pymodule]
#[allow(deprecated)]
fn pawz_core(_py: Python, _m: &PyModule) -> PyResult<()> {
    Ok(())
}
