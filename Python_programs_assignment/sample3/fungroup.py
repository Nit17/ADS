def group(input_list, size):
    grouped_lists = []
    for i in range(0, len(input_list), size):
        grouped_lists.append(input_list[i:i+size])
    return grouped_lists

# Example usage
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group_size = 3
result = group(input_list, group_size)
print(result)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
