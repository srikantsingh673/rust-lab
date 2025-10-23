//! project_01 - Example experimental crate
//!
//! This project can be used for isolated testing, benchmarking,
//! or building something that could evolve into a standalone library.

use pyo3::prelude::*;
use rand::Rng;
use std::fs::File;
use std::io::{Write, BufRead, BufReader};

/// A simple function to demonstrate functionality
#[pyfunction]
pub fn experiment_summary() {
    println!("Running project_01 experiment successfully!");
}


// --------------------------
// 1. Heavy mathematical computation
// --------------------------
#[pyfunction]
fn heavy_computation(x: u128) -> u128 {
    (0..=x).map(|n| n * n).sum::<u128>()
}

// --------------------------
// 2. Heavy string processing
// --------------------------
#[pyfunction]
fn heavy_string_processing(n: usize) -> String {
    let mut rng = rand::thread_rng();
    let letters: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".chars().collect();
    let mut result = String::new();

    for _ in 0..n {
        let rand_str: String = (0..100)
            .map(|_| letters[rng.gen_range(0..letters.len())])
            .collect();
        result.push_str(&rand_str.chars().rev().collect::<String>());
    }
    result
}

// --------------------------
// 3. Heavy list manipulation
// --------------------------
#[pyfunction]
fn heavy_list_manipulation(n: usize) -> Vec<usize> {
    let mut rng = rand::thread_rng();
    let mut numbers: Vec<usize> = (0..n).map(|_| rng.gen_range(0..1000)).collect();

    numbers.sort();
    numbers.into_iter().filter(|num| num % 2 == 0).collect()
}

// --------------------------
// 4. File I/O heavy test
// --------------------------
#[pyfunction]
fn heavy_file_io(n: usize, filename: &str) -> Vec<String> {
    let mut rng = rand::thread_rng();
    let mut file = File::create(filename).expect("Unable to create file");

    for _ in 0..n {
        let line: String = (0..100)
            .map(|_| {
                let c = rng.gen_range(0..62);
                match c {
                    0..=25 => (b'a' + c as u8) as char,
                    26..=51 => (b'A' + (c - 26) as u8) as char,
                    _ => (b'0' + (c - 52) as u8) as char,
                }
            })
            .collect();
        writeln!(file, "{}", line).expect("Unable to write to file");
    }

    // Read back
    let file = File::open(filename).expect("Unable to open file");
    BufReader::new(file)
        .lines()
        .map(|l| l.unwrap())
        .collect()
}

#[pymodule]
fn project_01(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(experiment_summary, m)?)?;
    m.add_function(wrap_pyfunction!(heavy_computation, m)?)?;
    m.add_function(wrap_pyfunction!(heavy_string_processing, m)?)?;
    m.add_function(wrap_pyfunction!(heavy_list_manipulation, m)?)?;
    m.add_function(wrap_pyfunction!(heavy_file_io, m)?)?;
    Ok(())
}
