from new_implementation import __version__
from new_implementation.new_implementation import Node, Linked_list
import pytest
import string

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


def test_head_is_first_node():
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
    Linked_list_.insert("c")
    Linked_list_.insert("b")
    Linked_list_.insert("a")
    actual= Linked_list_.__str__()
    assert actual == expected

def test_append():
    Linked_list_ = Linked_list()
    Linked_list_.append(1)
    assert Linked_list_.head.data_ is 1
    Linked_list_.append(2)
    assert Linked_list_.head.next_.data_ is 2
    assert Linked_list_.head.next_.next_ is None



def test_insertAfter():
    Linked_list_ = Linked_list()
    assert Linked_list_.insertAfter(5,1) == "No change, method exception"
    Linked_list_.append(5)
    Linked_list_.insertAfter(5,1)
    assert Linked_list_.head.next_.data_ == 1
    assert Linked_list_.head.next_.next_ == None
    Linked_list_.insertBefore(1,4)
    assert Linked_list_.head.next_.data_ == 4
    assert Linked_list_.head.next_.next_.data_ == 1



def test_insertBefore():
    Linked_list_ = Linked_list()
    assert Linked_list_.insertBefore(5,1) == "No change, method exception"
    Linked_list_.append(5)
    Linked_list_.insertBefore(5,1)
    assert Linked_list_.head.data_ == 1
    Linked_list_.insertBefore(5,2)
    assert Linked_list_.head.next_.data_ == 2
    assert Linked_list_.head.next_.next_.data_ == 5


def test_return_Kth_value():
    # Arrange
    expected=4
    Linked_list_=Linked_list()
    for i in range(1,7):
        Linked_list_.append(i)
    #Act
    actual=Linked_list_.return_Kth_value(2)
    # Assert
    assert actual== expected
    assert Linked_list_.return_Kth_value(7)=='such value does not exist'
    assert Linked_list_.return_Kth_value(6)=='such value does not exist'
    assert Linked_list_.return_Kth_value(-4)==4



def test_ziplists():
    # Arrange
    expected='{ a } -> { 0 } -> { b } -> { 1 } -> { c } -> { 2 } -> { d } -> { 3 } -> { e } -> { 4 } -> { f } -> { 5 } -> { g } -> { 6 } -> { h } -> { 7 } -> { i } -> { 8 } -> NULL'
    list1=Linked_list()
    list2=Linked_list()
    for i in string.ascii_lowercase[0:10]:
        list1.append(i)
    for i in range(0,10):
        list2.append(i)
    # Act
    actual = Linked_list().zipLists(list1,list2)
    # Assert
    assert actual== expected

