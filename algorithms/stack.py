class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if (self.size() == 0):
            return None  # если стек пустой
        return self.stack.pop(0)


    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if (self.size() == 0):
            return None  # если стек пустой
        return self.stack[0]

def is_balanced(string: str) -> bool:
    brackets_stack = Stack()

    for char in string:
        if char == '(':
            brackets_stack.push(char)
        elif char == ')' and not brackets_stack.pop():
            return False

    return not brackets_stack.peek()

def postfix_calc(string: str) -> int:
    return 0
