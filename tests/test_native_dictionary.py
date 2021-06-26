"""Native dictionary methods tests."""
from algorithms.native_dictionary import NativeDictionary


def test_native_dictionary():
  native_dictionary = NativeDictionary(7)

  native_dictionary.put('foo', 1)

  assert native_dictionary.get('foo') == 1
