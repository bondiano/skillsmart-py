"""Linked list methods tests."""
from algorithms.linked_list import LinkedList, Node

# заюзать property-based тесты
def test_find():
    linked_list = LinkedList()

    assert not linked_list.find(10)

    node1 = Node(1)
    linked_list.add_in_tail(node1)

    node10 = Node(10)
    linked_list.add_in_tail(node10)

    assert linked_list.find(10) == node10
    assert not linked_list.find(100)

def test_find_all():
    linked_list = LinkedList()

    assert not linked_list.find_all(1)

    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(10))
    assert len(linked_list.find_all(10)) == 1

    linked_list.add_in_tail(Node(1))
    assert len(linked_list.find_all(1)) == 2

def test_delete():
    linked_list = LinkedList()

    node1 = Node(1)
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(10))
    linked_list.add_in_tail(Node(10))
    linked_list.add_in_tail(Node(10))
    linked_list.add_in_tail(node1)

    linked_list.delete(1)

    assert len(linked_list.find_all(1)) == 1

    linked_list.delete(10, True)

    assert linked_list.len() == 1
    assert linked_list.head == node1
    assert linked_list.tail == node1


def test_clean():
    linked_list = LinkedList()

    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))

    linked_list.clean()
    assert linked_list.len() == 0


def test_len():
    linked_list = LinkedList()

    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))

    assert linked_list.len() == 4


def test_insert():
    linked_list = LinkedList()

    node1 = Node(1)
    node4 = Node(4)
    linked_list.add_in_tail(node1)
    linked_list.add_in_tail(Node(2))
    linked_list.add_in_tail(Node(3))
    linked_list.add_in_tail(node4)


    linked_list.insert(node1, Node(8))

    assert linked_list.len() == 5

    finded_node = linked_list.find(8)
    assert finded_node
    assert node1.next == finded_node

    node10 = Node(10)
    linked_list.insert(node4, node10)

    assert linked_list.tail == node10


def test_sum_two_number_list():
    l1 = [1, 2, 3, 4]
    linked_list1 = LinkedList()
    for v in l1:
        linked_list1.add_in_tail(Node(v))

    l2 = [5, 6, 7, 8]
    linked_list2 = LinkedList()
    for v in l2:
        linked_list2.add_in_tail(Node(v))

    empty_linked_list1 = LinkedList()

    assert not linked_list1.sum_two_number_list(empty_linked_list1)

    sum_linked_list = linked_list1.sum_two_number_list(linked_list2)

    sum_l = [6, 8, 10, 12]
    sum_linked_list_node = sum_linked_list.head
    index = 0
    while sum_linked_list_node is not None:
        assert sum_linked_list_node.value == sum_l[index]

        index += 1
        sum_linked_list_node = sum_linked_list_node.next
