"""Dynamic Array methods tests."""
from algorithms.dyn_array import DynArray

def test_insert():
  dyn_array = DynArray()
  assert dyn_array.count == 0

  # negatie cases
  err = None
  try:
    dyn_array.insert(200, 1)
  except IndexError as e:
    err = str(e)
  assert err == 'Index is out of bounds'

  print(dyn_array.count)
  dyn_array.insert(0, 200)

  for el in range(20):
    dyn_array.append(el)

  assert dyn_array.count == 21

  dyn_array.insert(4, 200)

  assert dyn_array.count == 22
  assert dyn_array[4] == 200
  for el in range(10):
    dyn_array.append(el)

  assert dyn_array.capacity == 32

  dyn_array.insert(8, 150)

  assert dyn_array.count == 33
  assert dyn_array.capacity == 64
  assert dyn_array[8] == 150


def test_delete():
  dyn_array = DynArray()
  assert dyn_array.count == 0

  # negatie cases
  err = None
  try:
    dyn_array.delete(10)
  except IndexError as e:
    err = str(e)
  assert err == 'Index is out of bounds'

  for el in range(20):
    dyn_array.append(el)

  assert dyn_array.capacity == 32
  assert dyn_array.count == 20

  dyn_array.delete(1)
  assert dyn_array.capacity == 32
  assert dyn_array.count == 19

  for i in range(10):
    dyn_array.delete(i)

  assert dyn_array.capacity == 16
  assert dyn_array.count == 9
