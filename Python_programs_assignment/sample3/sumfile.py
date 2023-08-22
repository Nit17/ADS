import sys

def sum_numbers_in_file(filename):
    total_sum = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total_sum += number
                except ValueError:
                    print(f"Skipping non-numeric value: {line.strip()}")
        print(f"Sum of all numbers in '{filename}': {total_sum}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sumfile.py <Nit.txt>")
    else:
        filename = sys.argv[1]
        sum_numbers_in_file(filename)
