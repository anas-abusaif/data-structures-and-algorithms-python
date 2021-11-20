# Hashtables

In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

## Challenge

Challenge Type: New Implementation

Features

Implement a Hashtable Class with the following methods:

* add

Arguments: key, value
Returns: nothing

This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

* get

Arguments: key

Returns: Value associated with that key in the table

* contains
Arguments: key

Returns: Boolean, indicating if the key exists in the table already.

* hash
Arguments: key

Returns: Index in the collection for that key

## Approach & Efficiency

Big O of time = O(1)
Big O of Space = O(1)

## API

add

Arguments: key, value Returns: nothing This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

get

Arguments: key Returns: Value associated with that key in the table

contains

Arguments: key Returns: Boolean, indicating if the key exists in the table already.

hash

Arguments: key Returns: Index in the collection for that key

- [x] Adding a key/value to your hashtable results in the value being in the data structure
- [x] Retrieving based on a key returns the value stored
- [x] Successfully returns null for a key that does not exist in the hashtable
- [x] Successfully handle a collision within the hashtable
- [x] Successfully retrieve a value from a bucket within the hashtable that has a collision
- [x] Successfully hash a key to an in-range value
