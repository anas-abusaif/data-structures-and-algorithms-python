from hash_table import __version__
from hash_table.hash_table import HashTable


def test_version():
    assert __version__ == '0.1.0'


import pytest

@pytest.fixture
def hashtable():
	return HashTable()

def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected

def test_hash_word(hashtable):
	expected = 376
	actual =  hashtable._HashTable__hash("dd")
	assert actual == expected

"""
"a"
ord("d") = 100
100 * 7 = 700
700 % 1024 = 700
-----------------
"dd"
200
200 * 7 = 1400
1400 % 1024 = 376
""" 

def test_add():
  pass
def test_contain():
	expected = True
	hashtable= HashTable()
	hashtable.add("dd","adham")

	actual = hashtable.contains("dd")

	assert actual == expected