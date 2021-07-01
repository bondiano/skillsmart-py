# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:
  def __init__(self):
    # ваша реализация хранилища
    self.storage = []
    pass

  def size(self):
    # количество элементов в множестве
    return len(self.storage)

  def put(self, value):
    # всегда срабатывает
    if not self.get(value):
      self.storage.append(value)

  def get(self, value):
    # возвращает True если value имеется в множестве,
    # иначе False
    return value in self.storage

  def remove(self, value):
    # возвращает True если value удалено
    # иначе False
    if self.get(value):
      self.storage.remove(value)
      return True
    return False

  def intersection(self, set2):
    # пересечение текущего множества и set2
    new_set = PowerSet()
    for value in set2.storage:
      if self.get(value):
        new_set.put(value)

    return new_set

  def union(self, set2):
    # объединение текущего множества и set2
    new_set = PowerSet()
    new_set.storage = self.storage.copy()

    for value in set2.storage:
      if not new_set.get(value):
        new_set.put(value)

    return new_set

  def difference(self, set2):
    # разница текущего множества и set2
    new_set = PowerSet()

    for value in self.storage:
      if not new_set.get(value) and set2.get(value):
        new_set.put(value)

    return new_set

  def issubset(self, set2):
    # возвращает True, если set2 есть
    # подмножество текущего множества,
    # иначе False
    if set2.size() > self.size():
      return False

    for value in set2.storage:
      if not self.get(value):
        return False

    return True
