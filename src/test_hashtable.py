#!/usr/bin/python
# -*- coding: utf-8 -*-
#


import hashtable
import unittest


TYPE_OPEN_ADDRESSING = hashtable.Type('OPENADDRESSING')
TYPE_SEPARATE_CHAINING = hashtable.Type('SEPARATECHAINING')


class Test(unittest.TestCase):

    def test_put_1(self):
        hs = hashtable.HashTable(2, TYPE_SEPARATE_CHAINING)
        hs.put("Alexis", 3)
        hash = hs.hash_function('Alexis')
        self.assertEquals(('Alexis', 3, None), hs.array[hash])

    def test_collision(self):
        # A hash function which returns 0 if the size of the string is even,
        # 1 otherwise
        hash_function = lambda x: len(x) % 2
        hs = hashtable.HashTable(2, TYPE_SEPARATE_CHAINING, hash_function=hash_function)
        hs.put("Alexis", 3)
        hs.put('Jerome', 4)
        hs.put('Ast', 5)

        print str(hs.array)