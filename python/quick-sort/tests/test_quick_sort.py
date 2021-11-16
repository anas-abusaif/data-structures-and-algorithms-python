from quick_sort import __version__
from quick_sort.quick_sort import quick_sort


def test_version():
    assert __version__ == '0.1.0'

def test_input_type():
    # Arrange
    expected='input is not a list'

    # Act
    actual=quick_sort(1,0,1)

    # Assert
    assert expected==actual

def test_sorting():
    # Arrange
    expected=[1,2,3,4,5,6,7,8]

    # Act
    actual=quick_sort([2,1,6,4,8,3,7,5],0,len([2,1,6,4,8,3,7,5])-1)

    # Assert
    assert actual==expected