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

    return not brackets_stack.size()

def postfix_calc(string: str) -> int:
    operations = {
        "+": lambda a, b: a + b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: b / a,
        "-": lambda a, b: b - a
    }
    number_stack = Stack()

    for char in string.split(' '):
        if char.isdigit():
            number_stack.push(int(char))
        elif char == '=':
            return number_stack.peek()
        else:
            a = number_stack.pop()
            b = number_stack.pop()
            result = operations[char](a, b)
            number_stack.push(result)
