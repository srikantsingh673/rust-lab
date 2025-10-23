# project_01

## Quickstart


1. **Create and activate a Python virtual environment (recommended)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   From the `labs/project_01` directory, run:
   
2. **Install requirements**

   With the virtual environment activated, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Build and install the Rust extension**

   In the same `labs/project_01` directory, run:
   ```bash
   maturin develop
   ```

4. **Run the Python file**

   Still in `labs/project_01`, run:
   ```bash
   python src/exp.py
   ```

This will build the Rust extension and run the provided Python script (`src/exp.py`) that uses the Rust code. All commands should be run from the `labs/project_01` directory, and it is recommended to use the `.venv` virtual environment for isolation.
