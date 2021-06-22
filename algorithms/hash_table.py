class HashTable:
  def __init__(self, sz, stp):
    self.size = sz
    self.step = stp
    self.slots = [None] * self.size

  def hash_fun(self, value):
    # в качестве value поступают строки!
    # всегда возвращает корректный индекс слота
    return sum(value.encode()) % self.size

  def seek_slot(self, value):
    # находит индекс пустого слота для значения, или None
    index = self.hash_fun(value)
    i = index
    if self.slots[i] is not None:
      i = (index + self.step) % self.size
      while self.slots[i] is not None and index != i:
        i = (index + self.step) % self.size
    if self.slots[i] is None:
      return i


  def put(self, value):
    # записываем значение по хэш-функции

    # возвращается индекс слота или None,
    # если из-за коллизий элемент не удаётся
    # разместить
    i = self.seek_slot(value)
    if i is not None:
      self.slots[i] = value
    return i

  def find(self, value):
    # находит индекс слота со значением, или None
    if value in self.slots:
      return self.slots.index(value)
