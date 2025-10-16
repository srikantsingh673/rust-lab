# 🦀 Chapter 01 — Basics

Rust is a **statically typed**, **compiled**, and **memory-safe** systems programming language.
It focuses on **speed**, **safety**, and **concurrency**, making it suitable for everything from
low-level systems code to high-performance web backends.

In this chapter, we’ll cover:

- Basic Rust syntax
- Variables and mutability
- Data types and their usage
- Constants and shadowing
- Data-Types
- User Input

---

## ⚙️ Basic Syntax

A minimal Rust program looks like this:

```rust
fn main() {
    println!("Hello, Rust!");
}
```

## 🧩 Variables and Mutability

In Rust, variables are immutable by default — once assigned, their value cannot change.

### Immutable Variable

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {}", x);
    // x = 6; // ❌ Error: cannot assign twice to immutable variable
}
```

### Mutable Variable

You can make a variable mutable using the mut keyword:

```rust
fn main() {
    let mut x = 5;
    println!("x = {}", x);
    x = 6; // ✅ allowed
    println!("x = {}", x);
}
```
#### 🧠 Tip: Always prefer immutability unless mutability is necessary — it improves safety and predictability.


### Constants

Constants are declared using const and must have an explicit type.
They are always immutable and are usually named in UPPER_SNAKE_CASE.

```rust
const MAX_POINTS: u32 = 100_000;

fn main() {
    println!("Max points = {}", MAX_POINTS);
}
```
#### 💡 Tip: Constants can be declared in any scope, including global scope.


### 🌀 Shadowing

Rust allows shadowing — redeclaring a variable with the same name, even with a new type.

```rust
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```
#### Output
```bash
The value of x in the inner scope is: 12
The value of x is: 6
```

## 🧩 Data-Types

Rust is a statically typed language, which means that it must know the types of all variables at compile time. The compiler can usually infer what type we want to use based on the value and how we use it.

```text
| Category                 | Type           | Size / Notes             | Example                                       | Description                        |
| ------------------------ | -------------- | ------------------------ | --------------------------------------------- | ---------------------------------- |
| **Scalar**               | `i8`           | 8-bit signed             | `let x: i8 = -10;`                            | Integer, negative and positive     |
|                          | `i16`          | 16-bit signed            | `let x: i16 = 1000;`                          | Integer, negative and positive     |
|                          | `i32`          | 32-bit signed            | `let x: i32 = 100_000;`                       | Default signed integer type        |
|                          | `i64`          | 64-bit signed            | `let x: i64 = 1_000_000;`                     | Large integer                      |
|                          | `i128`         | 128-bit signed           | `let x: i128 = 10_i128.pow(10);`              | Very large integer                 |
|                          | `isize`        | depends on architecture  | `let x: isize = 42;`                          | Pointer-sized signed integer       |
|                          | `u8`           | 8-bit unsigned           | `let x: u8 = 255;`                            | 0–255, no negative                 |
|                          | `u16`          | 16-bit unsigned          | `let x: u16 = 500;`                           | 0–65,535                           |
|                          | `u32`          | 32-bit unsigned          | `let x: u32 = 1_000_000;`                     | Default unsigned integer           |
|                          | `u64`          | 64-bit unsigned          | `let x: u64 = 1_000_000_000;`                 | Large unsigned integer             |
|                          | `u128`         | 128-bit unsigned         | `let x: u128 = 10_u128.pow(10);`              | Very large unsigned integer        |
|                          | `usize`        | depends on architecture  | `let x: usize = 10;`                          | Pointer-sized unsigned integer     |
|                          | `f32`          | 32-bit floating          | `let x: f32 = 3.14;`                          | Single-precision float             |
|                          | `f64`          | 64-bit floating          | `let x: f64 = 3.141592;`                      | Default float                      |
|                          | `bool`         | 1 byte                   | `let is_rust_fun = true;`                     | Boolean: `true` or `false`         |
|                          | `char`         | 4 bytes (Unicode)        | `let letter: char = '🦀';`                    | Single Unicode scalar value        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Compound**             | `tuple`        | Fixed size, mixed types  | `let t: (i32, bool, char) = (42, true, 'R');` | Can destructure values             |
|                          | `array`        | Fixed size, same type    | `let arr: [i32; 4] = [1,2,3,4];`              | Stack-allocated collection         |
|                          | `slice`        | Dynamic reference        | `let slice: &[i32] = &arr[1..3];`             | View into an array                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **String types**         | `String`       | Heap-allocated           | `let s = String::from("Hello");`              | Growable, owned string             |
|                          | `&str`         | Reference                | `let s: &str = "Hello";`                      | String slice, immutable            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Pointer types**        | `&T`           | Reference                | `let r: &i32 = &x;`                           | Borrowed reference                 |
|                          | `&mut T`       | Mutable reference        | `let r: &mut i32 = &mut x;`                   | Mutable borrow                     |
|                          | `Box<T>`       | Heap pointer             | `let b = Box::new(10);`                       | Owns heap-allocated value          |
|                          | `Rc<T>`        | Reference-counted        | `let r = Rc::new(5);`                         | Shared ownership (single-threaded) |
|                          | `Arc<T>`       | Atomic reference-counted | `let a = Arc::new(5);`                        | Shared ownership (multi-threaded)  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Other types**          | `Option<T>`    | Enum                     | `let o: Option<i32> = Some(10);`              | Represents value or absence        |
|                          | `Result<T, E>` | Enum                     | `let r: Result<i32, &str> = Ok(42);`          | Success or error                   |
|                          | `()`           | Unit type                | `let u = ();`                                 | “Nothing” type, similar to `void`  |
|                          | `never` `!`    |                          | `fn never_returns() -> ! { loop {} }`         | Function never returns             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Reference / Borrowed** | `&[T]`         | Slice                    | `let s: &[i32] = &arr;`                       | Borrowed view of array or vector   |
|___________________________________________________________________________________________________________________________________________________________|
```
**For more reference:** https://doc.rust-lang.org/book/ch03-02-data-types.html


## 🧩 User Input

Rust provides several ways to read user input, most commonly using the `std::io` module. The typical approach is to read a line from standard input and then parse it into the desired type. **(User input always be in String Type)**

### Example: Reading a String

```rust
use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter something:");
    io::stdin().read_line(&mut input).expect("Failed to read line");
    println!("You typed: {}", input.trim());
}
```

### Example: Reading and Parsing a Number

```rust
use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter a number:");
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let num: i32 = input.trim().parse().expect("Please type a number!");
    println!("You entered: {}", num);
}
```

#### 🧠 Tip: Always use `.trim()` before parsing to remove any trailing newline or whitespace.

