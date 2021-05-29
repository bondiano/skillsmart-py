class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> list:
        """1.4.: поиск всех узлов по **val**
        (возвращается список найденных узлов)."""
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        """1.1.: удаления первого узла по **val**
        1.2.: Удаление **all** узлов с **val**"""
        node = self.head
        prevNode = None

        while node is not None:
            if (node.value == val):
                if node == self.head:
                    self.head = node.next
                else:
                    self.insert(prevNode, node.next)
                if not all:
                    return

            prevNode = node
            node = node.next

    def clean(self):
        """1.3.: удаление всех уздлов"""
        self.__init__()

    def len(self) -> int:
        """1.5.: текущая длина списка"""
        node = self.head
        _len = 0
        while node is not None:
            _len += 1
            node = node.next

        return _len

    def insert(self, afterNode: Node, newNode: Node):
        """1.6.: Вставка **newNode** после **afterNode**.
        Если **afterNode** == None, элемент добавляется первым в список."""
        if afterNode is self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
