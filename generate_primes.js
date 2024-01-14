const fs = require("fs");

function isPrime(num) {
  if (num <= 1) return false;
  if (num <= 3) return true;

  if (num % 2 === 0 || num % 3 === 0) return false;

  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) return false;
  }
  return true;
}

function generatePrimes(filename, limit) {
  let num = 2;
  let count = 0;
  const stream = fs.createWriteStream(filename);

  while (count < limit) {
    if (isPrime(num)) {
      stream.write(num + "\n");
      count++;
    }
    num++;
  }

  stream.end();
}

let limit = 10000;

// Check if an argument is provided
if (process.argv.length > 2) {
  const inputLimit = parseInt(process.argv[2], 10);
  if (!isNaN(inputLimit)) {
    limit = inputLimit;
  } else {
    console.log("Invalid number provided, using default limit of 10000");
  }
}

const startTime = new Date();
generatePrimes("primes_node.txt", limit);
const endTime = new Date();

console.log(`Time taken: ${(endTime - startTime) / 1000} seconds`);
