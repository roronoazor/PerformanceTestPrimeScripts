import subprocess
import time
import matplotlib.pyplot as plt
import numpy as np

def run_command(command):
    start_time = time.time()
    subprocess.run(command, shell=True)
    end_time = time.time()
    return end_time - start_time

def main():
    # Sample sizes for prime numbers
    sample_sizes = [1000, 5000, 10000, 100000, 200000, 500000, 1000000, 1500000, 2000000]

    # Initialize dictionaries to store execution times
    times_python = []
    times_go = []
    times_node = []

    for size in sample_sizes:
        # Modify the scripts to take the number of primes as an argument if needed
        python_time = run_command(f"python ./generate_primes.py {size}")
        go_time = run_command(f"go run ./generate_primes.go {size}")
        node_time = run_command(f"node ./generate_primes.js {size}")

        # Store the times
        times_python.append(python_time)
        times_go.append(go_time)
        times_node.append(node_time)

    # Plotting
    plt.figure(figsize=(10, 6))
    bar_width = 0.25
    index = np.arange(len(sample_sizes))

    plt.bar(index, times_python, bar_width, label='Python')
    plt.bar(index + bar_width, times_go, bar_width, label='Go')
    plt.bar(index + 2 * bar_width, times_node, bar_width, label='Node.js')

    plt.xlabel('Number of Primes')
    plt.ylabel('Execution Time (Seconds)')
    plt.xticks(index + bar_width, sample_sizes)
    plt.title('Prime Number Generation PerformanceComparison')
    plt.legend()
    plt.savefig('./performance_comparison.png')
    plt.show()


if __name__ == "__main__":
    main()