"""Dynamic Array methods tests."""
from algorithms.deque import Deque, is_polindrom

def test_deque():
  deq = Deque()

  deq.addFront("f1")
  deq.addTail("t1")
  deq.addFront("f2")
  deq.addTail("t2")

  assert deq.removeFront() == "f2"
  assert deq.removeTail() == "t2"
  assert deq.size() == 2

def test_is_polindrom():
  assert is_polindrom("")
  assert is_polindrom("1")
  assert is_polindrom("212")
  assert is_polindrom("deed")
  assert is_polindrom("Malayalam")
  assert not is_polindrom("dog")
  assert not is_polindrom("lolkek")
