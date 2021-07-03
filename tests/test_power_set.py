"""Power Set methods tests."""
from algorithms.power_set import PowerSet


def test_power_set():
  test_set = PowerSet()

  for i in range(10):
    test_set.put(i)

  assert test_set.size() == 10

  test_set.put(8)

  assert test_set.size() == 10

  assert test_set.issubset(test_set)

  test_subset = PowerSet()

  for i in range(5, 8):
    test_subset.put(i)

  assert test_set.issubset(test_subset)

  test_set_2 = PowerSet()

  for i in range(5, 15):
    test_set_2.put(i)

  test_set_intersection = test_set.intersection(test_set_2)
  assert test_set_intersection.storage == [5, 6, 7, 8, 9]

  test_set_union = test_set.union(test_set_2)

  for value in test_set.storage + test_set_2.storage:
    assert test_set_union.get(value)

  test_set_difference = test_set.difference(test_set_2)

  assert test_set_difference.storage == [0, 1, 2, 3, 4]
