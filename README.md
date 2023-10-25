# Mini PJT 8 - Python to Rust Migration Project
## Overview 
The objective of this project is to rewrite a Python script in the Rust programming language. The primary goals are to migrate the code while maintaining the same functionality for data processing tasks and to evaluate execution speed and resource usage between the two languages.

## Key Repositories Contents 
- `YML Files`: These files contain the respective Python and Rust configurations for workflow definitions used in continuous integration and deployment.
- `lib`: This directory houses a shared Python library with functions utilized in the main.py script. The library is responsible for computing summary statistics (mean, median, standard deviation) for the dataset stored in the heightweight.csv file.
- `main.py` and `test.py`: These are Python scripts for the main application and its associated tests, respectively.
- `Rust Code`: This section comprises main.rs and lib.rs, which are the Rust equivalents of the Python code.
- `requirements.txt`: This file lists the dependencies required for the Python project.

## Migration Steps
These steps will help facilitate the migration of the project from Python to Rust, allowing for a comprehensive evaluation of performance and resource usage.

1. Cargo Initialization: Use cargo init to create Rust project structures.
2. Update Makefile: Modify the Makefile to include Rust-specific build and test commands.
3. Create Separate YML Files: Develop separate YAML configuration files for Python and Rust to accommodate language-specific testing and deployment requirements.
4. Adapt Python Function Libraries: Modify the Python function libraries based on the previous Mini Project (Mini PJT 5) to ensure compatibility with Rust.
5. Create and Modify Cargo Files: Develop or modify the Cargo.toml files to match the functions and dependencies used in the Python project, aligning them with Rust requirements.

## Performance Comparison between Python and Rust 
![image](https://github.com/nogibjj/IDS706_Mini_PJT8/assets/141780408/ba005f86-97c5-4a08-a8a7-11f0fa7d400a)
