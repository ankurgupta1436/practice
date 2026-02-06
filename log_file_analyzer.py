import re
from collections import Counter
import sys

LOG_PATTERN = re.compile(r"\[(INFO|WARNING|ERROR)\]\s(.+)")

def analyze_log(file_path):
    levels = Counter()
    messages = Counter()

    with open(file_path, "r") as file:
        for line in file:
            match = LOG_PATTERN.search(line)
            if match:
                level, message = match.groups()
                levels[level] += 1
                if level == "ERROR":
                    messages[message] += 1

    return levels, messages

def display_results(levels, messages):
    print("\n📊 Log Level Summary")
    for level, count in levels.items():
        print(f"{level}: {count}")

    if messages:
        print("\n🔥 Most Common Errors")
        for msg, count in messages.most_common(5):
            print(f"{count}x - {msg}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    levels, messages = analyze_log(logfile)
    display_results(levels, messages)

if __name__ == "__main__":
    main()
