"""Queue methods tests."""
from algorithms.queue_on_stack import Queue


def test_queue():
  queue = Queue()

  assert queue.size() == 0

  for i in range(3):
    queue.enqueue(i)

  assert queue.size() == 3

  assert queue.dequeue() == 0
  assert queue.dequeue() == 1

  assert queue.size() == 1


def test_scroll_queue():
  queue = Queue()

  for i in range(3):
    queue.enqueue(i)

  queue.scroll(2)

  assert queue.dequeue() == 1
  assert queue.dequeue() == 2
  assert queue.dequeue() == 0

  assert queue.size() == 0
