from algorithms.stack import Stack

class Queue:
  def __init__(self):
    self.inputs = Stack()
    self.outputs = Stack()

  def enqueue(self, item):
    self.inputs.push(item)

  def dequeue(self):
    if not self.outputs.size():
      while self.inputs.size():
          self.outputs.push(self.inputs.pop())

    return self.outputs.pop()

  def size(self):
    return self.inputs.size() + self.outputs.size()

  def scroll(self, n: int):
    count = 0

    while self.size() - count != n:
      self.enqueue(self.dequeue())
      count += 1
