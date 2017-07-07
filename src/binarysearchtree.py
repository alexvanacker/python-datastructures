#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Binary Search Tree implementation
#
# author: Alexis Vanacker - 2017/07/15


class BinarySearchTree():

    def __init__(self):
        self.rootNode = None

    def add_value(self, key, value):
        # print 'Adding <' + str(key) + ', ' + str(value) + '>'
        self.rootNode = self.add_value_to_node(key, value, self.rootNode)

    def add_value_to_node(self, key, value, node):
        """ Recursive function for adding a  key and value to a Node. Compares the
        node's key to the given key. If it equal, do nothing. If it
        is either superior or equal, check for the existence of a node in
        that direction. if the Node does not exist, add it with the value.
        Otherwise, recurse in that direction."""

        if node is None:
            # print 'Added Node<' + str(key) + ', ' + str(value) + '>'
            node = Node(key, value)
            return node

        if node.value > value:
            node.left = self.add_value_to_node(key, value, node.left)
        elif node.value < value:
            node.right = self.add_value_to_node(key, value, node.right)
        else:
            # Overwrite the previous value
            node.value = value
        return node

    def get(self, key):
        return self.get_from_node(key, self.rootNode)

    def get_from_node(self, key, node):
        if node is None:
            return None

        if node.key == key:
            return node

        if key < node.key:
            return self.get_from_node(key, node.left)
        else:
            return self.get_from_node(key, node.right)

    def delete_value(self, value):
        pass


class Node():
    """ A node in the Binary Search Tree, with a key, value and
    pointers to a left and right subtree."""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def size(self):
        if self is None:
            return 0
        else:
            size_left = 0 if self.left is None else self.left.size()
            size_right = 0 if self.right is None else self.right.size()
            return 1 + size_left + size_right

    def __eq__(self, other):
        return self.key == other.key and \
            self.value == other.value

