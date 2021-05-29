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

    def len(self) -> int:
        node = self.head
        _len = 0
        while node is not None:
            _len += 1
            node = node.next

        return _len

    def insert(self, afterNode: Node, newNode: Node):
        if afterNode is self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode

    def sum_two_number_list(self, other_list):
        """1.8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков."""
        if (self.len() != other_list.len()):
            return

        new_list = LinkedList()

        node = self.head
        other_node = other_list.head
        while node is not None:
            new_node = Node(node.value + other_node.value)
            new_list.add_in_tail(new_node)

            node = node.next
            other_node = other_node.next

        return new_list
