import re
import sys


def main():
    print(count(input("Text: ")))

def count(s: str) -> int:
    results = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(results)

if __name__ == "__main__":
    main()