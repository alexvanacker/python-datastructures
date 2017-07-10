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
        print str(hs.array)