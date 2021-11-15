from insertion_sort import __version__
import insertion_sort
from insertion_sort.insertion_sort import insetion_sorting

def test_version():
    assert __version__ == '0.1.0'

def test_input_type():
    # Arrange
    expected='input is not a list'

    # Act
    actual=insetion_sorting(1)

    # Assert
    assert expected==actual

def test_sorting():
    # Arrange
    expected=[1,2,3,4,5,6,7,8]

    # Act
    actual=insetion_sorting([2,1,6,4,8,3,7,5])

    # Assert
    assert actual==expected