from hash_table.repeatedWord import repeated_word
import pytest

def test_repeatedWord_error():

  with pytest.raises(ValueError):
    input = ""
    repeated_word(input)



def test_repeatedWord_valid():
  # Arrange
  expected = "a"

  # Act
  actual = repeated_word("Once upon a time, there was a brave princess who...")

  # Assert
  assert actual == expected