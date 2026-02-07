def fibonacci(n: int) -> list:
    """
    Return a list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        return []

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]
if __name__ == "__main__":
    n = 10
    print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")