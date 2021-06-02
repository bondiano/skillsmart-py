"""Linked list methods tests."""
from algorithms.linked_list2 import LinkedList2, Node


def test_find():
    linked_list = LinkedList2()

    assert not linked_list.find(10)

    node1 = Node(1)
    linked_list.add_in_tail(node1)

    node10 = Node(10)
    linked_list.add_in_tail(node10)

    assert linked_list.find(10) == node10
    assert not linked_list.find(100)


def test_find_all():
    linked_list = LinkedList2()

    assert not linked_list.find_all(1)

    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(10))
    assert len(linked_list.find_all(10)) == 1

    linked_list.add_in_tail(Node(1))
    assert len(linked_list.find_all(1)) == 2


def test_delete():
    linked_list = LinkedList2()

    node1 = Node(1)
    node0 = Node(0)
    linked_list.add_in_tail(node0)
    linked_list.add_in_tail(Node(10))
    linked_list.add_in_tail(Node(10))
    linked_list.add_in_tail(Node(10))
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(node1)

    linked_list.delete(1)

    assert len(linked_list.find_all(1)) == 1

    linked_list.delete(10, True)

    assert linked_list.len() == 2
    assert linked_list.head == node0
    assert linked_list.tail == node1

    linked_list.delete(0, True)
    assert linked_list.len() == 1
    assert linked_list.head == node1
    assert linked_list.tail == node1


def test_clean():
    linked_list = LinkedList2()

    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))

    linked_list.clean()
    assert linked_list.len() == 0


def test_len():
    linked_list = LinkedList2()

    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(1))

    assert linked_list.len() == 4


def test_insert():
    linked_list = LinkedList2()

    node1 = Node(1)
    node4 = Node(4)
    node2 = Node(2)
    node3 = Node(3)
    linked_list.add_in_tail(node1)
    linked_list.add_in_tail(node2)
    linked_list.add_in_tail(node3)
    linked_list.add_in_tail(node4)

    linked_list.insert(node1, Node(8))

    assert linked_list.len() == 5

    finded_node = linked_list.find(8)
    assert finded_node
    assert node1.next == finded_node

    node10 = Node(10)
    linked_list.insert(node4, node10)

    assert linked_list.tail == node10

    node11 = Node(11)
    linked_list.insert(node2, node11)
    assert node2.next.value == node11.value
    assert node3.prev.value == node11.value
