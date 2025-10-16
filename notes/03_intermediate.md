# 🦀 Chapter 03 — Intermediate

In this chapter, we’ll cover:
- Ownership
- Borrowing & References
- Slices
- Structs
- Enums

Each of these topics helps you understand how Rust keeps your program safe — without needing a garbage collector like other languages.

---

## 🧩 Ownership — The Heart of Rust ❤️

Every programming language must decide who owns data in memory and when it should be cleaned up.
Rust’s answer is Ownership — a simple set of rules that guarantee safety.

### 🧠 The Three Ownership Rules

**1. Each value in Rust has one owner.**
**2. When the owner goes out of scope, the value is automatically dropped (memory freed).**
**3. There can be only one owner at a time.**


```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1; // Ownership moves to s2

    // println!("{}", s1); // ❌ Error! s1 no longer owns the data
    println!("{}", s2); // ✅ Works fine
}
```
#### 🧩 What’s happening here?

1. `String::from("hello")` creates data on the heap.
2. `s1` owns that data.
3. When we assign `s1` to `s2`, ownership moves to `s2`.
4. `s1` is now invalid, and Rust prevents us from using it again.
5. This prevents double freeing memory — something that causes crashes in other languages.


## 🧩 Cloning — Make a Real Copy

If you really want to keep both copies, use .clone():

```rust
fn main() {
    let s1 = String::from("rust");
    let s2 = s1.clone(); // Deep copy of data

    println!("s1 = {}, s2 = {}", s1, s2);
}
```

clone() creates a complete copy of the data on the heap.
It’s safe but slightly slower — use it only when needed.

## 🧩 Borrowing & References — Looking Without Owning 🔍

Sometimes, we don’t want to take ownership — we just want to look at the data or use it temporarily.
Rust lets us do that using references (&).

```rust
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1); // &s1 means we are "borrowing" it

    println!("'{}' has length {}", s1, len);
}

fn calculate_length(s: &String) -> usize {
    s.len() // use it, but not own it
}
```

#### 🧩 What’s happening here?

1. `&s1` creates a reference to `s1`.
2. The function can read it but cannot modify or own it.
3. When the function ends, `s1` is still valid.


**When you pass a variable to a function, its ownership can move there too.**

```rust
fn main() {
    let s = String::from("hello");
    take_ownership(s);

    // println!("{}", s); // ❌ Error: s moved into function
}

fn take_ownership(some_string: String) {
    println!("{}", some_string);
}
```

**If you want to keep using it after the function, return it back:**

```rust
fn main() {
    let s1 = String::from("world");
    let s2 = give_back(s1);
    println!("{}", s2);
}

fn give_back(s: String) -> String {
    s // returned, ownership moves back to caller
}
```

### Mutable References (&mut)

If you want to change the borrowed value, you need a mutable reference.

```rust
fn main() {
    let mut s = String::from("hi");
    change(&mut s);
    println!("{}", s);
}

fn change(s: &mut String) {
    s.push_str(", Rust!"); // modifies the original value
}
```

#### ⚠️ Rules for safety:

1. Only one mutable reference at a time.
2. You can’t mix mutable and immutable references.


## 🧩 Slices — Borrowing Parts of Data

A slice lets you reference a small part of a collection (like a string or array) without copying it.

### String Slices

```rust
fn main() {
    let s = String::from("hello world");

    let hello = &s[0..5];
    let world = &s[6..11];

    println!("{}, {}", hello, world);
}
```

#### Output

```bash
hello, world
```

### Array Slices

```rust
fn main() {
    let numbers = [10, 20, 30, 40, 50];
    let slice = &numbers[1..4];
    println!("Slice: {:?}", slice); // {:?} is required for slice & array instead of {}
}
```

#### Output

```bash
Slice: [20, 30, 40]
```


## 🧩 Structs — Making Custom Data Types 🧱

In real programs, you’ll want to group related data together.
Rust does this using structs (short for “structures”).

```rust
struct User {
    username: String,
    email: String,
    active: bool,
}

fn main() {
    let user1 = User {
        username: String::from("sri_rust"),
        email: String::from("sri@rust.com"),
        active: true,
    };

    println!("Username: {}", user1.username);
    println!("Email: {}", user1.email);
    println!("Active: {}", user1.active);
}

```

#### Output

```bash
Username: sri_rust
Email: sri@rust.com
Active: true
```

### 🧩 Mutable Structs

Copy all the other fields from user1, except the ones I overwrite.

```rust
struct User {
    username: String,
    email: String,
    active: bool,
}

fn main() {
    let user1 = User {
        username: String::from("alpha"),
        email: String::from("alpha@mail.com"),
        active: false,
    };

    let user2 = User {
        username: String::from("beta"),
        ..user1
    };
    println!("User2: {}, {}, {}", user2.username, user2.email, user2.active);
}
```

#### Output

```bash
User2: beta, alpha@mail.com, false
```

### 🧩 Tuple Structs

Tuple structs look like tuples but have their own type name.

```rust
struct Color(i32, i32, i32);

fn main() {
    let black = Color(10, 20, 30);
    println!("({}, {}, {})", black.0, black.1, black.2);
}
```

#### Ouput

```bash
(10, 20, 30)
```


## 🧩 Enums — One Type, Many Possibilities 🎭

Enums let you define a type that can be one of many forms.

**Basic Example :**

```rust
#[allow(dead_code)] // to supress the the warning
enum Direction {
    North,
    South,
    East,
    West,
}

fn main() {
    let dir = Direction::East;

    match dir {
        Direction::North => println!("Going up"),
        Direction::South => println!("Going down"),
        Direction::East => println!("Going right"),
        Direction::West => println!("Going left"),
    }
}
```

#### Output

```bash
Going up
```

### 🧩 Enums with Data

Each variant can hold different types of data.

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
}

fn main() {
    let msg = Message::Move { x: 10, y: 20 };

    match msg {
        Message::Quit => println!("Quit message"),
        Message::Move { x, y } => println!("Move to ({}, {})", x, y),
        Message::Write(text) => println!("Text: {}", text),
    }
}
```

#### Output

```bash
Move to (10, 20)
```

### 🧩 The Option Enum — Safer Than Null

Rust does not have null.
Instead, it uses the `Option<T>` enum to represent something that might exist or not.

```rust
fn main() {
    let some_number = Some(5);
    let no_number: Option<i32> = None;

    match no_number {
        Some(value) => println!("Value: {}", value),
        None => println!("No value found"),
    }
}
```

#### Output

```bash
No value found
```
