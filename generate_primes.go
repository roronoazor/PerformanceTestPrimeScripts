package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n <= 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	for i := 5; i*i <= n; i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}

func generatePrimes(filename string, limit int) {
	file, err := os.Create(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	num, count := 2, 0

	for count < limit {
		if isPrime(num) {
			fmt.Fprintf(writer, "%d\n", num)
			count++
		}
		num++
	}

	writer.Flush()
}

func main() {

	limit := 10000 // Default limit
	// Check if an argument is provided
	if len(os.Args) > 1 {
		var err error
		limit, err = strconv.Atoi(os.Args[1])
		if err != nil {
			fmt.Println("Invalid number provided, using default limit of 10000")
			limit = 10000
		}
	}

	startTime := time.Now()
	generatePrimes("primes_go.txt", limit)
	endTime := time.Now()

	fmt.Printf("Time taken: %v seconds\n", endTime.Sub(startTime).Seconds())

}
