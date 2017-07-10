#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Hash table implementation
#
#


class HashTable():
    """ An attempt in implementing a HashTable. I'll only
    consider string keys at the moment because I'm more interested
    in conflict resolution rather than the hash function."""

    def __init__(self, size, hashTableType, hash_function=None):
        """ Constructor with an initial size for the array."""
        self.size = size
        self.array = [None] * size
        self.put = lambda key, value: hashTableType.put(self, key, value)
        self.get = lambda key, value: hashTableType.get(self, key, value)
        if hash_function is None:
            self.hash_function = lambda string: hash_function_strings(string, size)
        else:
            self.hash_function = hash_function


def get_with_open_addressing(hashtable, key, value):
    pass


def get_with_separate_chaining(hashtable, key, value):
    pass


def put_with_separate_chaining(hashtable, key, value):
    """ Adds the key value to the table and resolves collisions with separate
    chaining, meaning that array[hash] contains a linked list of all the
    key values which keys' hash are the same."""
    key_hash = hashtable.hash_function(key)
    if hashtable.array[key_hash] is None:
        # Key, value, pointer to next node
        # This is a basic linked list implem
        hashtable.array[key_hash] = (key, value, None)
    else:
        previous = hashtable.array[key_hash]
        while previous[2] is not None:
            previous = previous[2]
        # APpend to the list
        previous[2] = (key, value, None)


def put_with_open_addressing(arrary, hash, value):
    pass


def hash_function_strings(string, max):
    """ Computes a hash for a string which should not be greater than
    max.
    """
    return hash(string) % max


class Type:
    """ Supported hash table implementations, allows for easier define
    when we will compare both."""

    def __init__(self, s):
        if s == 'OPENADDRESSING':
            self.put = put_with_open_addressing
            self.get = get_with_open_addressing
        elif s == 'SEPARATECHAINING':
            self.put = put_with_separate_chaining
            self.get = get_with_separate_chaining
        else:
            raise Exception('Hash table type not implemented: ' + s)
