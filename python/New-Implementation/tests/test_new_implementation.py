from new_implementation import __version__
from new_implementation.new_implementation import Node, Linked_list
import pytest


def test_version():
    assert __version__ == "0.1.0"


def test_node_has_int_data():
    expected = 1
    node = Node(1)
    actual = node.data_
    assert actual == expected


def test_node_has_str_data():
    expected = "some value"
    node = Node("some value")
    actual = node.data_
    assert actual == expected


def test_node_is_a_Node():
    expected = "Node"
    node = Node(1)
    actual = type(node).__name__
    assert actual == expected


def test_node_without_value():
    with pytest.raises(TypeError):
        node = Node()


def test_new_linked_list_is_empty():
    expected = None
    Linked_list_ = Linked_list()
    actual = Linked_list_.head
    assert actual == expected


def test_linked_list_insert_one_node():
    expected = 1
    Linked_list_ = Linked_list()
    Linked_list_.insert(1)
    node = Linked_list_.head
    actual = node.data_
    assert actual == expected



def test_linked_list_insert_twice():
    expected = 1
    Linked_list_ = Linked_list()
    Linked_list_.insert(0)
    Linked_list_.insert(1)
    node = Linked_list_.head
    actual = node.data_
    assert actual == expected
    assert Linked_list_.head.next_.data_ == 0


def test_linked_list_includes_twice():
  expected =True
  Linked_list_ = Linked_list()
  Linked_list_.insert(0)
  actual = Linked_list_.includes(0)
  assert actual == expected


def test_to_string():
    expected = "{ a } -> { b } -> { c } -> NULL"
    Linked_list_ = Linked_list()
    node1= Linked_list_.insert("c")
    node2= Linked_list_.insert("b")
    node3= Linked_list_.insert("a")
    actual= Linked_list_.to_string()
    assert actual == expected