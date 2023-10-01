class HTMLTag:
    def __init__(self, tag_name, attributes=None):
        self.tag_name = tag_name
        self.attributes = attributes or {}
    def __str__(self):
        attr_str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        return f'<{self.tag_name} {attr_str}>'
def parse_html(html):
    stack = [] 
    i = 0
    while i < len(html):
        if html[i] == '<':
            j = html.find('>', i)
            if j == -1:
                return False  
            tag_contents = html[i + 1:j]
            if tag_contents.startswith('/'):
                if stack and stack[-1].tag_name == tag_contents[1:]:
                    stack.pop()
                else:
                    return False  
            else:
                parts = tag_contents.split()
                tag_name = parts[0]
                attributes = {}
                for part in parts[1:]:
                    key, value = part.split('=')
                    attributes[key] = value.strip('\'"')
                stack.append(HTMLTag(tag_name, attributes))
            i = j + 1
        else:
            i += 1
    return stack
html_with_attributes = '<div class="container" id="main"><p>Some text</p></div>'
result = parse_html(html_with_attributes)
if result:
    for tag in result:
        print(tag)
else:
    print("Invalid HTML")
