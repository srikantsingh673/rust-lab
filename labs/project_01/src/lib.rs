//! project_01 - Example experimental crate
//!
//! This project can be used for isolated testing, benchmarking,
//! or building something that could evolve into a standalone library.

use pyo3::prelude::*;
use rand::Rng;
use std::fs::File;
use std::io::{Write, BufRead, BufReader};

/// A simple function to demonstrate functionality
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

#[pyfunction]
fn arithmetic_operations(x: u128) -> f64 {
    let mut result = 0.0;
    for n in 1..=x {
        let value = (((n as f64 * 3.0) + 7.0) - 4.0) / 2.0 % 5.0;
        result += value;
    }
    result
}

// --------------------------
// 2. Heavy string processing
// --------------------------
#[pyfunction]
fn string_processing(n: usize) -> String {
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
fn list_manipulation(n: usize) -> Vec<usize> {
    let mut rng = rand::thread_rng();
    let mut numbers: Vec<usize> = (0..n).map(|_| rng.gen_range(0..1000)).collect();

    numbers.sort();
    numbers.into_iter().filter(|num| num % 2 == 0).collect()
}


// --------------------------
// 4. File I/O heavy test
// --------------------------
#[pyfunction]
fn file_io(n: usize, filename: &str) -> Vec<String> {
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

// --------------------------
// 5. Conditional if-else speed test
// --------------------------
#[pyfunction]
fn number_to_name(n: usize) -> &'static str {
    if n == 0 { "zero" }
    else if n == 1 { "one" }
    else if n == 2 { "two" }
    else if n == 3 { "three" }
    else if n == 4 { "four" }
    else if n == 5 { "five" }
    else if n == 6 { "six" }
    else if n == 7 { "seven" }
    else if n == 8 { "eight" }
    else if n == 9 { "nine" }
    else if n == 10 { "ten" }
    else if n == 11 { "eleven" }
    else if n == 12 { "twelve" }
    else if n == 13 { "thirteen" }
    else if n == 14 { "fourteen" }
    else if n == 15 { "fifteen" }
    else if n == 16 { "sixteen" }
    else if n == 17 { "seventeen" }
    else if n == 18 { "eighteen" }
    else if n == 19 { "nineteen" }
    else if n == 20 { "twenty" }
    else if n == 21 { "twenty-one" }
    else if n == 22 { "twenty-two" }
    else if n == 23 { "twenty-three" }
    else if n == 24 { "twenty-four" }
    else if n == 25 { "twenty-five" }
    else if n == 26 { "twenty-six" }
    else if n == 27 { "twenty-seven" }
    else if n == 28 { "twenty-eight" }
    else if n == 29 { "twenty-nine" }
    else if n == 30 { "thirty" }
    else if n == 31 { "thirty-one" }
    else if n == 32 { "thirty-two" }
    else if n == 33 { "thirty-three" }
    else if n == 34 { "thirty-four" }
    else if n == 35 { "thirty-five" }
    else if n == 36 { "thirty-six" }
    else if n == 37 { "thirty-seven" }
    else if n == 38 { "thirty-eight" }
    else if n == 39 { "thirty-nine" }
    else if n == 40 { "forty" }
    else if n == 41 { "forty-one" }
    else if n == 42 { "forty-two" }
    else if n == 43 { "forty-three" }
    else if n == 44 { "forty-four" }
    else if n == 45 { "forty-five" }
    else if n == 46 { "forty-six" }
    else if n == 47 { "forty-seven" }
    else if n == 48 { "forty-eight" }
    else if n == 49 { "forty-nine" }
    else if n == 50 { "fifty" }
    else if n == 51 { "fifty-one" }
    else if n == 52 { "fifty-two" }
    else if n == 53 { "fifty-three" }
    else if n == 54 { "fifty-four" }
    else if n == 55 { "fifty-five" }
    else if n == 56 { "fifty-six" }
    else if n == 57 { "fifty-seven" }
    else if n == 58 { "fifty-eight" }
    else if n == 59 { "fifty-nine" }
    else if n == 60 { "sixty" }
    else if n == 61 { "sixty-one" }
    else if n == 62 { "sixty-two" }
    else if n == 63 { "sixty-three" }
    else if n == 64 { "sixty-four" }
    else if n == 65 { "sixty-five" }
    else if n == 66 { "sixty-six" }
    else if n == 67 { "sixty-seven" }
    else if n == 68 { "sixty-eight" }
    else if n == 69 { "sixty-nine" }
    else if n == 70 { "seventy" }
    else if n == 71 { "seventy-one" }
    else if n == 72 { "seventy-two" }
    else if n == 73 { "seventy-three" }
    else if n == 74 { "seventy-four" }
    else if n == 75 { "seventy-five" }
    else if n == 76 { "seventy-six" }
    else if n == 77 { "seventy-seven" }
    else if n == 78 { "seventy-eight" }
    else if n == 79 { "seventy-nine" }
    else if n == 80 { "eighty" }
    else if n == 81 { "eighty-one" }
    else if n == 82 { "eighty-two" }
    else if n == 83 { "eighty-three" }
    else if n == 84 { "eighty-four" }
    else if n == 85 { "eighty-five" }
    else if n == 86 { "eighty-six" }
    else if n == 87 { "eighty-seven" }
    else if n == 88 { "eighty-eight" }
    else if n == 89 { "eighty-nine" }
    else if n == 90 { "ninety" }
    else if n == 91 { "ninety-one" }
    else if n == 92 { "ninety-two" }
    else if n == 93 { "ninety-three" }
    else if n == 94 { "ninety-four" }
    else if n == 95 { "ninety-five" }
    else if n == 96 { "ninety-six" }
    else if n == 97 { "ninety-seven" }
    else if n == 98 { "ninety-eight" }
    else if n == 99 { "ninety-nine" }

    else if n == 100 { "one hundred" }
    else { "out of range" }
}

#[pymodule]
fn project_01(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(heavy_computation, m)?)?;
    m.add_function(wrap_pyfunction!(arithmetic_operations, m)?)?;
    m.add_function(wrap_pyfunction!(string_processing, m)?)?;
    m.add_function(wrap_pyfunction!(list_manipulation, m)?)?;
    m.add_function(wrap_pyfunction!(file_io, m)?)?;
    m.add_function(wrap_pyfunction!(number_to_name, m)?)?;
    Ok(())
}
