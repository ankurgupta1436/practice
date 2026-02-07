def count_word_frequency(text: str) -> dict:
    """
    Count the frequency of each word in a string.
    """
    words = text.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency
if __name__ == "__main__":
    sample_text = "Hello world! Hello everyone. Welcome to the world of Python."
    freq = count_word_frequency(sample_text)
    print("Word Frequency:")
    for word, count in freq.items():
        print(f"{word}: {count}")