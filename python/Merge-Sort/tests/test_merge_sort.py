from merge_sort import __version__
from merge_sort.merge_sort import Mergesort

def test_version():
    assert __version__ == '0.1.0'


def test_input_type():
    # Arrange
    expected='input is not a list'

    # Act
    actual=Mergesort(1)

    # Assert
    assert expected==actual

def test_sorting():
    # Arrange
    expected=[1,2,3,4,5,6,7,8]

    # Act
    actual=Mergesort([2,1,6,4,8,3,7,5])

    # Assert
    assert actual==expected