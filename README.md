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
4. Adapt Python Function Libraries: Modify the Python function libraries based on the previous Mini Project to ensure compatibility with Rust.
5. Create and Modify Cargo Files: Develop or modify the Cargo.toml files to match the functions and dependencies used in the Python project, aligning them with Rust requirements.

## Performance Comparison between Python and Rust 
**1. Rust Result**

![image](https://github.com/nogibjj/IDS706_Mini_PJT8/assets/141780408/448e5dc2-2c48-4f04-ada9-4a118a3a6747)
 - The elapsed time for rust is 38.28 milliseconds.
 - The CPU usage is 0.00%
 - The memory usage is 28.583778%

**2. Python Result**

![image](https://github.com/nogibjj/IDS706_Mini_PJT8/assets/141780408/bc779146-863a-45b0-8d96-313bbda5aac8)
- The elapsed time for python is 0.0936 seconds
- The CPU usage for python is 5.9%
- The memory usage is 28.6%

In this test, Rust demonstrates lower CPU usage and faster execution times compared to Python. This performance advantage is evident in both the total execution time and CPU consumption. Memory usage is roughly equivalent between the two languages, with Rust having a slight edge. One possible explanation for this performance difference is the inherent characteristics of each language. Rust, being a compiled language with aggressive optimizations and a unique ownership system, often outperforms Python, an interpreted language, in raw computational tasks. Rust's design places a strong emphasis on zero-cost abstractions and efficient memory management without the need for a garbage collector. In contrast, Python prioritizes developer productivity and code readability, which can introduce more runtime overhead.
