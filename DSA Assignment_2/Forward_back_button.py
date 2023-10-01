class Browser:
    def __init__(self):
        self.back_stack = []  
        self.forward_stack = []  
        self.current_url = None  

    def visit_url(self, url):
        self.back_stack.append(self.current_url)
        self.forward_stack = []  
        self.current_url = url

    def back(self):
        
        if self.back_stack:
            self.forward_stack.append(self.current_url)
            self.current_url = self.back_stack.pop()
            return self.current_url
        else:
            return None  

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_url)
            self.current_url = self.forward_stack.pop()
            return self.current_url
        else:
            return None  
    def current_page(self):
        return self.current_url


my_browser = Browser()


my_browser.visit_url("https://www.cs.usfca.edu/~galles/visualization/Algorithms.html")
my_browser.visit_url("https://popupsmart.com/blog/web-scraping-tools")
my_browser.visit_url("https://www.geeksforgeeks.org/stack-data-structure/?ref=shm")

# Perform navigation
print("Current Page:", my_browser.current_page())
print("Going back to:", my_browser.back())
print("Going back to:", my_browser.back())
print("Going forward to:", my_browser.forward())
print("Going forward to:", my_browser.forward())
print("Current Page:", my_browser.current_page())
