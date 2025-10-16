# 🦀 rust-lab

**rust-lab** is a Rust learning and research workspace.  
The goal of this project is to **learn Rust deeply**, take structured notes, and experiment with writing **high-performance, cross-language functions** that can be integrated into **Python**, **JavaScript**, or other ecosystems for efficiency and speed.

---

## 🚀 Overview

This repository is structured to support:

- 📚 Learning and practicing Rust concepts chapter by chapter.
- 🧩 Building reusable Rust modules and crates.
- ⚙️ Experimenting with FFI (Python bindings) and WebAssembly (JavaScript).
- 🗒️ Keeping organized notes and documentation for each learning stage.

---

## 🧰 Requirements

#### **Recomended to use Linux or WSL for Windows**

| Tool | Version | Purpose |
|------|----------|----------|
| [Rust](https://www.rust-lang.org/tools/install) | Latest stable | Main programming language |
| [Cargo](https://doc.rust-lang.org/cargo/) | Installed with Rust | Package & build manager |
| [Git](https://git-scm.com/) | Latest | Version control |
| [VS Code](https://code.visualstudio.com/) + [Rust Analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) | Recommended | Development environment |

---

## ⚙️ Installation

### 1️⃣ Install WSL (For Windows)
**Detailed Documentation :** https://medium.com/@srikantsingh673/run-linux-on-windows-like-a-pro-no-dual-boot-no-vm-5ab4a9683dc8

### 2️⃣ Install Rust (via rustup)
**Official Documentation :** https://doc.rust-lang.org/book/ch01-01-installation.html


## 🏗️ Project Structure

```text
rust-lab/
│
├── Cargo.toml                # Project manifest (dependencies, workspace setup)
├── README.md                 # Documentation (this file)
│
├── notes/                    # Markdown notes and topic breakdowns
│   ├── 01_basics.md
│   ├── 02_memory_and_ownership.md
│   └── ...
│
├── src/
│   ├── lib.rs                # Shared modules (core logic, helpers)
│   ├── main.rs               # Optional central runner
│   └── bin/                  # Each file here is a runnable chapter (cargo run --bin ...)
│       ├── hello.rs
│       ├── io.rs
│
├── labs/                     # Independent experimental crates (each with its own Cargo.toml)
│   ├── project_01/
│   │   ├── Cargo.toml
│   │   └── src/
|   |        ├── lib.rs 
│   |        ├── main.rs 
|   |
│   ├── project_02/
│   │   ├── Cargo.toml
│   │   └── src/
|   |        ├── lib.rs 
│   |        ├── main.rs 
|   |
│   └── project_03/
│       ├── Cargo.toml
│       └── src/
|            ├── lib.rs 
│            ├── main.rs  
│
└── target/                   # Auto-created by Cargo (compiled output)
```

## ▶️ Run a Specific .rs File

```bash
cargo run --bin hello_world
```

## ▶️ Run All Tests

```bash
cargo test
```

## ▶️ Run Specific Project

```bash
cd labs/project_01
cargo run
```
