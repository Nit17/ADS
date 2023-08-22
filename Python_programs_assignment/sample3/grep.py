import sys
import re

def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if re.search(pattern, line):
                    print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <Nit.txt>")
    else:
        pattern = sys.argv[1]
        filename = sys.argv[2]
        grep(pattern, filename)