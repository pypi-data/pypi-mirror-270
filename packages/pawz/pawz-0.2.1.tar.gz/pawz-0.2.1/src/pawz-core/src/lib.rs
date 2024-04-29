use open;
use pyo3::prelude::*;
//use pyo3::exceptions::PyValueError;
//use pyo3::types::PyTuple;

#[pyfunction]
fn open_pawz() {
    let url = "https://www.youtube.com/watch?v=gJ6slhwPp6E";
    open::that(url).unwrap();
}

/// A Python module implemented in Rust.
#[pymodule]
#[allow(deprecated)]
fn pawz_core(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(open_pawz, m)?)?;
    Ok(())
}
