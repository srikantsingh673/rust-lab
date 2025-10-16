# 🦀 Chapter 02 — Moderate

In this chapter, we’ll cover:
- Functions
- Control Flow
- Loops

---

## 🧩 Functions

Functions are declared using the `fn` keyword. They help organize code into reusable blocks.

```rust
fn greet(name: &str) {
    println!("Hello, {}!", name);
}

fn main() {
    greet("Rustacean");
}
```

Functions can return values using the `->` syntax:

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b // No semicolon means this is the return value
}

fn main() {
    let sum = add(2, 3);
    println!("Sum: {}", sum);
}
```

---

## 🧩 Control Flow

Rust supports common control flow constructs: `if`, `else`, and `match`.

### If/Else
```rust
fn main() {
    let number = 7;
    if number < 10 {
        println!("Small number");
    } else {
        println!("Big number");
    }
}
```
### Using `if` in a `let` Statement

You can use an `if` expression directly in a `let` statement to assign a value based on a condition. This is useful for concise conditional assignments.

```rust
fn main() {
    let number = 5;
    let result = if number % 2 == 0 {"even"} else {"odd"};
    println!("{} is {}", number, result);
}
```
### Nested If-Else Statement

```rust
fn main() {
    let number = 7;
    if number < 10 {
        println!("Small number");
    }
    else if number > 0 {
         println!("Negative number");
    }
    else {
        println!("Big number");
    }
}
```

### Match
`match` is a powerful pattern matching construct:

```rust
fn main() {
    let grade = 'A';
    match grade {
        'A' => println!("Excellent!"),
        'B' => println!("Good!"),
        'C' => println!("Average!"),
        _ => println!("Unknown grade"),
    }
}
```

---

## 🧩 Loops

Rust provides several looping constructs: `loop`, `while`, and `for`.

### Loop
```rust
fn main() {
    let mut count = 0;
    loop {
        count += 1;
        if count == 3 {
            break;
        }
        println!("Count: {}", count);
    }
}
```

#### Output
```bash
Count: 1
Count: 2
```

### Multiple Loop
```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```

#### Output
```bash
count = 0
remaining = 10
remaining = 9
count = 1
remaining = 10
remaining = 9
count = 2
remaining = 10
End count = 2
```

### While
```rust
fn main() {
    let mut number = 3;
    while number != 0 {
        println!("{}!", number);
        number -= 1;
    }
    println!("Liftoff!");
}
```

#### Output
```bash
3!
2!
1!
Liftoff!
```

### For
```rust
fn main() {
    for x in 0..5 {
        println!("x = {}", x);
    }
}
```

#### Output
```bash
x = 0
x = 1
x = 2
x = 3
x = 4
```

**For more details:** [Rust Book: Control Flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html)