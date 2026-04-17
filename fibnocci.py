def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

if __name__ == "__main__":
    n_terms = 20
    result = generate_fibonacci(n_terms)
    
    # We will use 'results.txt' to keep it simple and avoid spelling errors
    file_path = "results.txt"
    
    with open(file_path, "w") as f:
        f.write(f"Fibonacci Sequence: {result}")
    
    print(f"Calculated: {result}")