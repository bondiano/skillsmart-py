"""Stack methods tests."""
from algorithms.stack import Stack, is_balanced

def test_push():
  stack = Stack()

  assert stack.size() == 0

  stack.push(1)
  assert stack.size() == 1

  stack.push(20)
  assert stack.size() == 2

def test_pop():
  stack = Stack()

  stack.push(1)
  stack.push(20)

  assert stack.pop() == 20
  assert stack.pop() == 1
  assert stack.size() == 0

  assert stack.pop() == None

def test_peek():
  stack = Stack()

  assert stack.peek() == None

  stack.push(1)
  stack.push(20)

  assert stack.peek() == 20
  assert stack.size() == 2
  stack.pop()
  assert stack.peek() == 1
  assert stack.size() == 1

def test_is_balanced():
  assert is_balanced("()")
  assert is_balanced("(()((())()))")
  assert not is_balanced("(")
  assert not is_balanced("(()()(())")
  assert not is_balanced("())(")
  assert not is_balanced("))((")
  assert not is_balanced("((())")
