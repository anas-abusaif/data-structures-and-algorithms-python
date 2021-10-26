from stack_and_queue import __version__
from stack_and_queue.queue import Queue
from stack_and_queue.stack import Stack
from stack_and_queue.validate_brackets import validate_brackets
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_stack_push():
    # Arrange
    expected=3
    stack_=Stack()
    # Act
    stack_.push(3)
    # Assert
    assert stack_.peek()==expected


def test_stack_push_multi():
    # Arrange
    expected=5
    stack_=Stack()
    # Act
    for i in range(0,6):
        stack_.push(i)
    # Assert
    assert stack_.peek()==expected


def test_stack_pop():
    # Arrange
    expected=5
    stack_=Stack()
    # Act
    for i in range(0,6):
        stack_.push(i)
    # Assert
    assert stack_.pop()==expected


def test_empty_a_stack():
    # Arrange
    expected=5
    stack_=Stack()
    # Act
    for i in range(0,6):
        stack_.push(i)
    
    for i in range(0,6):
        stack_.pop()
    # Assert
    assert stack_.is_empty()==True


def test_peek():
    # Arrange
    expected=5
    stack_=Stack()
    # Act
    for i in range(0,6):
        stack_.push(i)
    # Assert
    assert stack_.peek()==expected


def test_instantiate_empty_stack():
    # Arrange
    expected=True
    # Act
    stack_=Stack()
    # Assert
    assert stack_.is_empty()==expected


def test_pop_or_peek_on_empty_stack():
    with pytest.raises(Exception):
        stack_=Stack()
        stack_.pop()
        stack_.peek()



def test_enqueue_into_queue():
    # Arrange
    expected=3
    queue_=Queue()
    # Act
    queue_.enqueue(3)
    # Assert
    assert queue_.peek()==expected


def test_enqueue_multi():
    # Arrange
    expexted=3
    queue_=Queue()
    # Act
    for i in range(0,4):
        queue_.enqueue(i)
    # Assert
    assert queue_.back.data_==expexted


def test_dequeue():
    # Arrange
    expected=0
    queue_=Queue()
    # Act
    for i in range(0,4):
        queue_.enqueue(i)
    # Assert
    assert queue_.dequeue()==expected


def test_peek_expected():
    # Arrange
    expected=0
    queue_=Queue()
    # Act
    for i in range(0,4):
        queue_.enqueue(i)
    # Assert
    assert queue_.peek()==expected


def test_can_empty_a_queue():
    # Arrange
    expected=False
    queue_=Queue()
    # Act
    for i in range(1,5):
        queue_.enqueue(i)

    for i in range(1,5):
        print(queue_.dequeue())
    # Assert
    assert queue_.is_empty()==expected


def test_instantiate_empty_queue():
    # Arrange
    expected=True
    # Act
    queue_=Queue()
    # Assert
    assert queue_.is_empty()==expected


def test_dequeue_or_peek_on_empty_queue():
    with pytest.raises(Exception):
        queue_=Queue()
        queue_.dequeue()
        queue_.peek()


def test_validate_brackets_true():
    # Arrange
    expected=True
    # Act
    actual=validate_brackets('{[]}[]({()})')
    # Assert
    assert actual== expected


def test_validate_brackets_false():
    # Arrange
    expected=False
    # Act
    actual=validate_brackets('{[]}]({(})')
    # Assert
    assert actual== expected