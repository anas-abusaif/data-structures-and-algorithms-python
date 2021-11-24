from hash_table.hash_table import HashTable
from hash_table.hashmap_left_join import left_join


def test_left_join_hashmap():
    table1 = HashTable()
    table1.add("person", "23")
    table1.add("person1", "30")
    table1.add("person2", "27")
    table1.add("person3", "18")
    table1.add("person4", "19")
    table2 = HashTable()
    table2.add("person", "45")
    table2.add("person1", "25")
    table2.add("person2", "19")
    table2.add("person4", "9")

    expected = [
        ['person', '23', '45'],
        ['person1', '30', '25'],
        ['person2', '27', '19'],
        ['person3', '18', None],
        ['person4', '19', '9']
        ]
    actual = left_join(table1, table2)
    assert actual == expected

def test_left_join_hashmap_with_first_hashmap_empty():
    table1 = HashTable()
    table2 = HashTable()
    table2.add("person", "45")
    table2.add("person1", "25")
    table2.add("person2", "19")
    table2.add("person4", "9")

    expected = []

    actual = left_join(table1, table2)
    assert actual == expected

def test_left_join_hashmap_with_second_hashmap_empty():
    table1 = HashTable()
    table1.add("person", "45")
    table1.add("person1", "25")
    table1.add("person2", "19")
    table1.add("person4", "9")
    table2 = HashTable()

    expected = [
        ['person', '45', None],
        ['person1', '25', None],
        ['person2', '19', None],
        ['person4', '9', None]
        ]

    actual = left_join(table1, table2)
    assert actual == expected
def test_left_join_hashmap_with_hashmaps_empty():
        table1 = HashTable()
        table2 = HashTable()
        expected = []
        actual = left_join(table1, table2)
        assert actual == expected