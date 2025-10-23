//! project_01 - Example experimental crate
//!
//! This project can be used for isolated testing, benchmarking,
//! or building something that could evolve into a standalone library.

use pyo3::prelude::*;

/// A simple function to demonstrate functionality
#[pyfunction]
pub fn experiment_summary() {
    println!("Running project_01 experiment successfully!");
}

// A simple function to find the cube of a number, using i64 to avoid overflow
#[pyfunction]
pub fn find_cube(num: i64) -> i64 {
    num * num * num
}

#[pymodule]
fn project_01(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(experiment_summary, m)?)?;
    m.add_function(wrap_pyfunction!(find_cube, m)?)?;
    Ok(())
}
