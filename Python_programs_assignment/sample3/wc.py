import sys

def count_lines_words_chars(filename):
    lines = 0
    words = 0
    chars = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                lines += 1
                words += len(line.split())
                chars += len(line)

        print("Lines:", lines)
        print("Words:", words)
        print("Characters:", chars)

    except FileNotFoundError:
        print("File not found:", filename)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc.py <Nit.txt>")
    else:
        filename = sys.argv[1]
        count_lines_words_chars(filename)
