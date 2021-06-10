class Queue:
  def __init__(self):
	  self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    if self.queue:
	    return self.queue.pop(0)

  def size(self):
    return len(self.queue)

  def scroll(self, n: int):
    count = 0

    while self.size() - count != n:
      self.enqueue(self.dequeue())
      count += 1
