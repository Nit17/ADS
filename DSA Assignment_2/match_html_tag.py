def is_valid_html(html):
    stack = []  
    i = 0
    while i < len(html):
        if html[i] == '<':     
            j = html.find('>', i)
            if j == -1:
                return False  
            tag = html[i + 1:j]
            if not tag.endswith('/'):    
                if tag.startswith('/'):
                    if not stack or stack.pop() != tag[1:]:
                        return False  
                else:
                    stack.append(tag)  
            i = j + 1
        else:
            i += 1
    return len(stack) == 0

html1 = "<html><body><p>Sample text</p></body></html>"
html2 = "<html><body><p>Sample text</p></html>"
html3 = "<html><body><p>Sample text</p></body></html>"
html4 = "<html><body><p>Sample text</p></body>"

print(is_valid_html(html1))  
print(is_valid_html(html2))  
print(is_valid_html(html3))  
print(is_valid_html(html4))  
