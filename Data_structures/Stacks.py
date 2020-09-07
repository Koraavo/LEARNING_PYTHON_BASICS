# Stacks mean Last In First Out - LIFO
# like the undo function - last command that was given needs to be removed
# or doing BODMAS

# creating a wrapper for stack
# stack has two functions - push and pop
# push can be done using append() and pop using pop()

class Stack():
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        return self.stack == []

    def push(self, items):
        self.stack.append(items)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def get_stack(self):
        return self.stack
