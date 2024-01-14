

# Prime Number Generation

This repository contains scripts for generating and writing prime numbers to a file. The scripts are implemented in three different programming languages: Python, Go, and Node.js. Each script is designed to generate the first n prime numbers and write them to a text file.

## Languages Used

- Python
- Go (Golang)
- Node.js (JavaScript)

## How It Works

Each script uses a basic algorithm to check for prime numbers and then writes these prime numbers to a file. The Go and Node.js versions utilize buffered and stream writing, respectively, for efficient file operations. The Python script writes directly to the file.

### Python

The Python script (`generate_primes.py`) checks for prime numbers and writes them to `primes_python.txt`.

### Go

The Go script (`generate_primes.go`) uses buffered writing to efficiently write the prime numbers to `primes_go.txt`.

### Node.js

The Node.js script (`generate_primes.js`) leverages stream writing to output the prime numbers to `primes_node.txt`.

## Getting Started

To run these scripts, you need to have the respective runtime environments for Python, Go, and Node.js installed on your machine.

### Running the Python Script

```bash
python generate_primes.py
```

### Running the Go Script

```bash
go run generate_primes.go
```

### Running the Node.js Script

```bash
node generate_primes.js
```

## Performance

These scripts are designed for educational purposes to demonstrate how prime number generation can be implemented and how file I/O is handled in different programming languages. They have not been optimized for high performance or for handling the nuances of large-scale prime number generation.

---

## To View the Performance Visually

To visually compare the performance of the scripts, a Python script named `benchmark_plot.py` is included. This script executes each of the prime number generation scripts across varying sample sizes (e.g., time taken to compute the first 1,000 primes, 10,000 primes, etc.) and plots these times on a graph using `matplotlib`.

### Prerequisites

- Python installed on your system.
- `pip` for installing Python packages.

### Setup and Run Instructions

1. **Create a Virtual Environment:**

   **For Windows:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   **For Mac/Linux:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   This step creates a virtual environment named `venv` and activates it.

2. **Install Required Packages:**

   With the virtual environment activated, install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```



   This command installs all the dependencies listed in `requirements.txt`.

3. **Run the Benchmark Plot Script:**

   **For Windows:**

   ```bash
   python benchmark_plot.py
   ```

   **For Mac/Linux:**

   ```bash
   python3 benchmark_plot.py
   ```

   Run the `benchmark_plot.py` script using the appropriate command for your operating system.

### Output

The script will generate and save an image named `performance_comparison.png` in your current directory. This image visually represents the performance comparison of the different scripts.

---

**Note**: Ensure you replace the placeholder paths and commands with the actual ones according to your project's structure and requirements. This template assumes a standard setup and might need adjustments to fit your specific use case.
```
