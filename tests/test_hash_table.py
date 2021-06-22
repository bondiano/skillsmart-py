"""Hash table methods tests."""
from algorithms.hash_table import HashTable


def test_hash_table():
  hash_table = HashTable(17, 1)

  test_str = 'Hello'
  test_str_index = hash_table.put(test_str)

  assert hash_table.find(test_str) == test_str_index
  assert hash_table.find('test') == None
