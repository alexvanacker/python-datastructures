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

        if node.key > key:
            node.left = self.add_value_to_node(key, value, node.left)
        elif node.key < key:
            node.right = self.add_value_to_node(key, value, node.right)
        else:
            # Overwrite the previous value
            node.value = value
        return node

    def get(self, key):
        return self.get_from_node(key, self.rootNode)

    def min(self):
        # TODO handle case for non initialized BST
        return self.rootNode.min()

    def get_from_node(self, key, node):
        if node is None:
            return None

        if node.key == key:
            return node

        if key < node.key:
            return self.get_from_node(key, node.left)
        else:
            return self.get_from_node(key, node.right)

    def delete(self, key):
        self.rootNode = self.delete_from_node(key, self.rootNode)

    def delete_from_node(self, key, node):
        if key < node.key:
            node.left = self.delete_from_node(key, node.left)
            return node
        elif key > node.key:
            node.right = self.delete_from_node(key, node.right)
            return node
        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left
            else:
                # We find the minimum node in the right subtree
                # we will replace the deleted node by that node
                copy_node = node
                node = copy_node.right.min()
                print 'Min in right tree found: {}'.format(node.key)
                # delete that one from the right tree
                node.right = self.delete_from_node(node.key, copy_node.right)
                node.left = copy_node.left
                return node

    def print_tree(self):
        """ Debug function, very raw, based on BSF algorithm."""

        visited = {}
        # List of list of node keys belonging to the same layer
        layers = []
        layers.append([self.rootNode])
        layer_index = 0
        while len(layers[layer_index]) > 0:
            #  Init next layer
            next_layer = layer_index + 1
            layers.insert(next_layer, [])
            for node in layers[layer_index]:
                if node.key not in visited:
                    # Process that node
                    visited[node.key] = True
                    if node.left is not None:
                        print 'adding {} to layer {}'.format(node.left.key,
                                                             next_layer)
                        layers[layer_index + 1].append(node.left)

                    if node.right is not None:
                        print 'adding {} to layer {}'.format(node.right.key,
                                                             next_layer)
                        layers[layer_index + 1].append(node.right)

            # Increment layer index
            layer_index += 1

        for layer in layers:
            layer_string = ''
            for node in layer:
                layer_string += str(node.key) + '  '
            print layer_string


class Node():
    """ A node in the Binary Search Tree, with a key, value and
    pointers to a left and right subtree."""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def print_node(self, index=0):
        tab = ''
        for x in xrange(index):
            tab += ' '
        print tab + str(self.key)
        print tab + '[]' if self.left is None else self.left.print_node(index=index+1)
        print tab + '[]' if self.right is None else self.right.print_node(index=index+1)

    def size(self):
        if self is None:
            return 0
        else:
            size_left = 0 if self.left is None else self.left.size()
            size_right = 0 if self.right is None else self.right.size()
            return 1 + size_left + size_right

    def min(self):
        if self.left is None:
            return self
        else:
            return self.left.min()

    def __eq__(self, other):
        return self.key == other.key and \
            self.value == other.value
