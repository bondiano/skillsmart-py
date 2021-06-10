class Deque:
  def __init__(self):
    # инициализация внутреннего хранилища
    self.deque = []

  def addFront(self, item):
    # добавление в голову
    self.deque.insert(0, item)

  def addTail(self, item):
    # добавление в хвост
    self.deque.append(item)

  def removeFront(self):
    if self.deque:
      return self.deque.pop(0)

  def removeTail(self):
    # удаление из хвоста
    if self.deque:
      return self.deque.pop()

  def size(self):
    # размер очереди
    return len(self.deque)

def is_polindrom(string: str) -> bool:
  if (len(string) < 2):
    return True

  deque = Deque()

  for char in string:
    deque.addTail(char.lower())

  while deque.size() > 1:
    if (deque.removeFront() != deque.removeTail()):
      return False

  return True
