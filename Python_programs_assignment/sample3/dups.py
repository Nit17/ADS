def dups(input_list):
    duplicates = []
    seen = set()
    for item in input_list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

input_list = [1, 2, 2, 3, 4, 4, 5]
result = dups(input_list)
print(result)  # Output: [2, 4]
