class NativeDictionary:
  def __init__(self, sz):
    self.size = sz
    self.slots = [None] * self.size
    self.values = [None] * self.size

  def hash_fun(self, key):
    # в качестве key поступают строки!
    # всегда возвращает корректный индекс слота
    return sum(value.encode()) % self.size

  def is_key(self, key):
    # возвращает True если ключ имеется,
    # иначе False
    return key in self.slots

  def put(self, key, value):
    # гарантированно записываем
    # значение value по ключу key
    index = self.hash_fun(key)
    self.slots[index] = value
    self.values[index] = value


  def get(self, key):
    # возвращает value для key,
    # или None если ключ не найден
    if self.is_key(key):
      index = self.hash_fun(key)
      return self.values[index]
