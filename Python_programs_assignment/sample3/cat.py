import sys

def print_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) != 2:
    print("Usage: python cat.py <Nit.txt>")
else:
    filename = sys.argv[1]
    print_file_contents(filename)
