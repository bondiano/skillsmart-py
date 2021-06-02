class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        while self.head and self.head.value == val:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            if not all:
                return

        node = self.head
        prev_node = None
        while node is not None:
            if node.value == val:
                node.next.prev = prev_node
                prev_node.next = node.next
                if self.head is None:
                    self.tail = None
                if node == self.tail:
                    self.tail = prev_node
                if not all:
                    return
            else:
                prev_node = node
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        node = self.head
        _len = 0
        while node is not None:
            _len += 1
            node = node.next

        return _len

    def insert(self, afterNode, newNode):
        if afterNode is self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next.prev = newNode
            afterNode.next = newNode

    def add_in_head(self, newNode):
        node = self.head
        self.head = newNode
        newNode.next = node
        node.prev = newNode

    def print(self):
        node = self.head
        print("forvard", end=" ")
        while node:
            print(node.value, end=" ")
            node = node.next

        node = self.tail
        print("back", end=" ")
        while node:
            print(node.value, end=" ")
            node = node.prev
        print("")
