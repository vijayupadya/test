export function fibonacci(n: number): number[] {
  const result: number[] = [];
  for (let i = 0; i < n; i++) {
    if (i === 0) result.push(0);
    else if (i === 1) result.push(1);
    else result.push(result[i - 1] + result[i - 2]);
  }
  return result;
}

if (require.main === module) {
  // Example: print first 10 Fibonacci numbers
  const n = 10;
  const sequence = fibonacci(n);
  console.log(`Fibonacci sequence of first ${n} numbers:`);
  console.log(sequence.join(", "));
}
