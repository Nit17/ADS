class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def reverse_file(input_file, output_file):
    # Initialize a stack
    stack = Stack()

    # Read the file and push each line onto the stack
    with open(input_file, 'r') as file:
        for line in file:
            stack.push(line.strip())

    # Write the lines from the stack back to the output file, reversing the order
    with open(output_file, 'w') as file:
        while not stack.is_empty():
            line = stack.pop()
            file.write(line + '\n')

if __name__ == "__main__":
    input_filename = "input.txt"  # Replace with the name of your input file
    output_filename = "output.txt"  # Replace with the name of your output file

    reverse_file(input_filename, output_filename)
    print("File reversed successfully.")
