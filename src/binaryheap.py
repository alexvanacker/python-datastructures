#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Binary Heap implementation
#
# author: Alexis Vanacker - 2017/07/09


class BinaryHeap():
    """ Binary heap implementation based on a binary tree.
    We consider here the root as always the "largest" element.
    We only build integer-based binary heaps here.

    The internal representation is an array, and for a given node at
    index i, its children are located in indexes 2*i and 2*i + 1. Note
    that for this to work, we cannot start at index 0. Instead, we leave
    the first element of the array empty.

    Note from the author: we could put the size of the tree there
    or some other relevant information. For now I'm keeping it empty by
    pure laziness (see: definition of a Software Engineer)."""

    def __init__(self):
        self.array = [None]
        self.size = 0

    def add_value(self, value):
        self.array.append(value)
        index = self.size
        self.size += 1
        self.reorder_bottom_up(index)

    def delete_max(self):
        """ Returns and removes the max value in the heap, then reorders the
        heap."""

        # By definition, the maximum is the root
        max_value = self.array[1]
        print 'Deleting value {}'.format(max_value)
        if max_value is None:
            # Empty heap case
            return None

        # Note: self.size is used here, because the array is of
        # size self.size + 1!
        self.exchange(1, self.size)
        # Remove the previous max value which we just inserted at size - 1
        del self.array[self.size]
        self.size = self.size - 1
        # Reorder by top down on 1
        self.reorder_top_down(1)
        return max_value

    def reorder_top_down(self, i):
        while 2 * i <= self.size:
            j = 2 * i
            if j < self.size and self.array[j] < self.array[j + 1]:
                j += 1

            if self.array[i] > self.array[j]:
                # Already well placed
                return
            else:
                self.exchange(i, j)
                i = j

    def reorder_bottom_up(self, i):
        """ Reorders the value at index i if its value is bigger than
        that of its parent. Keeps doing so until the parent has a
        larger value or is None (then it has become the root)."""

        value = self.array[i]
        parent_index = i / 2
        parent_value = self.array[parent_index]
        if parent_value is not None and parent_value < value:
            self.exchange(i, parent_index)
            self.reorder_bottom_up(parent_index)

    def exchange(self, i, j):
        """ Exchange elements with index i and j in the heap."""
        print 'Exchanging ({},{}) with ({},{})'.format(i, self.array[i], j, self.array[j])
        copy_i = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = copy_i



