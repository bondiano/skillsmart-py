"""Ordered list methods tests."""
from algorithms.ordered_list import OrderedList, OrderedStringList

def test_ordered_list():
  ordered_list = OrderedList(asc=True)

  assert ordered_list.len() == 0

  ordered_list.add(2)

  assert ordered_list.len() == 1


def test_ordered_string_list():
  ordered_string_list = OrderedStringList(asc=True)

  assert ordered_string_list.len() == 0

  ordered_string_list.add("2")

  assert ordered_string_list.len() == 1
