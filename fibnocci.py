def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

if __name__ == "__main__":
    n_terms = 20
    result = generate_fibonacci(n_terms)
    
    # Define the output file path
    file_path = "fibonacci_results.txt"
    
    with open(file_path, "w") as f:
        f.write(f"Fibonacci Sequence (First {n_terms} terms):\n")
        f.write(", ".join(map(str, result)))
    
    print(f"Successfully calculated Fibonacci sequence.")
    print(f"Results saved to: {file_path}")
    print(f"Sequence: {result}")