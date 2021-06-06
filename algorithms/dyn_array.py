import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
      if (self.count == i):
        self.append(itm)
      else:
        self[i]  # check IndexError
        count = self.count + 1
        if count > self.capacity:
          self.resize(2 * self.capacity)
        # move elements forward
        index = i
        while index < self.count:
          self.array[index + 1] = self.array[index]
          index += 1
        self.count += 1
        self.array[i] = itm

    def delete(self, i):
      # удаляем объект в позиции i
      self[i]
      index = i
      while index >= 0:
        self.array[index - 1] = self.array[index]
        index -= 1;
      self.count = self.count - 1
      fill_percent = self.count / self.capacity * 100
      capacity = int(
          self.capacity / 1.5 if self.capacity > 16 and fill_percent < 50 else self.capacity
          )
      self.resize(capacity if capacity > 16 else 16)
