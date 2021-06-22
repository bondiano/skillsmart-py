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
    while None in self.slots:
      if self.slots[index] is None:
        return index
      else:
        index = (index + self.step) % self.size


  def put(self, value):
    # записываем значение по хэш-функции

    # возвращается индекс слота или None,
    # если из-за коллизий элемент не удаётся
    # разместить
    index = self.seek_slot(value)
    if index is not None:
      self.slots[index] = value
    return index

  def find(self, value):
    # находит индекс слота со значением, или None
    if value in self.slots:
      return self.slots.index(value)
