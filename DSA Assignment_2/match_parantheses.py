def is_valid_parentheses(expression):
    stack = []  
    parentheses_map = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != parentheses_map[char]:
                return False  

    return not stack

# Test cases
print(is_valid_parentheses("()")) 
print(is_valid_parentheses("()[]{}"))  
print(is_valid_parentheses("(]"))  
print(is_valid_parentheses("([)]"))  
print(is_valid_parentheses("{[]}"))  
