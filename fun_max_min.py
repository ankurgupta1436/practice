def find_max_and_min(numbers: list) -> tuple:
    """
    Return the maximum and minimum values from a list of numbers.
    """
    if not numbers:
        raise ValueError("The list cannot be empty")

    return max(numbers), min(numbers)
if __name__ == "__main__":
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    max_num, min_num = find_max_and_min(sample_numbers)
    print(f"Max: {max_num}, Min: {min_num}")