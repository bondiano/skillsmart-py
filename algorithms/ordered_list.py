class Node:
  def __init__(self, v):
    self.value = v
    self.prev = None
    self.next = None


class OrderedList:
  def __init__(self, asc):
    self.head = None
    self.tail = None
    self.__ascending = asc

  def compare(self, v1, v2):
    if v1 < v2:
      return - 1
    elif v1 == v2:
      return 0
    else:
      return 1

  def add(self, value):
    # автоматическая вставка value
    # в нужную позицию
    new_node = Node(value)
    nodes = self.get_all()
    if not nodes:
      self.head = new_node
      self.tail = new_node
      return

    stop_search = 1 if self.__ascending else - 1
    after_node = None
    for next_n in nodes:
      comp_res = self.compare(next_n.value, value)
      if comp_res == stop_search:
        after_node = next_n.prev
        break
      else:
          after_node = next_n

    if after_node is None: # добавляем в голову
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    elif after_node is self.tail: # в хвост
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    else:
      new_node.prev = after_node
      after_node.next.prev = new_node
      new_node.next = after_node.next
      after_node.next = new_node

  def find(self, val):
    node = self.head
    while node != None:
      if self.compare(node.value, val) == 0:
          break
      node = node.next
    return node

  def delete(self, val):
    deleted_node = self.find(val)
    if deleted_node is not None and deleted_node.value == val:
      if deleted_node is self.head and deleted_node.next is None:
        self.clean(self.__ascending)
      elif deleted_node is self.tail:
        self.tail = deleted_node.prev
        deleted_node.prev.next = None
      elif deleted_node is self.head:
        self.head = deleted_node.next
        deleted_node.next.prev = None
      else:
        deleted_node.prev.next = deleted_node.next
        deleted_node.next.prev = deleted_node.prev

      deleted_node.prev = None
      deleted_node.next = None

  def clean(self, asc):
    self.__init__(asc)

  def len(self):
    return len(self.get_all())

  def get_all(self):
    r = []
    node = self.head
    while node != None:
        r.append(node)
        node = node.next
    return r


class OrderedStringList(OrderedList):
  def __init__(self, asc):
    super(OrderedStringList, self).__init__(asc)

  def compare(self, v1, v2):
    # переопределённая версия для строк
    return super(OrderedStringList, self).compare(v1.strip(), v2.strip())
