from time import time
import sys

def is_prime(n):
    if n <= 1: 
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(filename, limit):
    primes = []
    num = 2
    count = 0
    while count < limit:
            if is_prime(num):
                primes.append(str(num))
                count += 1
            num += 1

    with open(filename, 'w') as file:
        file.write("\n".join(primes))
        

# Default limit
limit = 10000

# Check if an argument is provided
if len(sys.argv) > 1:
    try:
        input_limit = int(sys.argv[1])
        limit = input_limit
    except ValueError:
        print("Invalid number provided, using default limit of 10000")

start_time = time()
generate_primes("primes_python.txt", limit)
end_time = time()

print(f"Time taken: {end_time - start_time} seconds")