import sys

def print_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            for _ in range(n):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python head.py <Nit.txt>")
    else:
        filename = sys.argv[1]
        print_first_n_lines(filename, 5)
