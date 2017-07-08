#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# QuickSort algorithm implementation.algorithm
#
#
#
# Author: Alexis Vanacker
# Date: 2017/07/08
#

import random


def quicksort_simple(array):
    """ A simple implementation where we select a random pivot without
    checking whether the sub arrays are balanded or not. A way to do this
    is to check the left and right arrays' size, and ensure none of the two
    has a size inferior to the array's size / 4.
    This is not the inplace implementation, hence has a space complexity of
    O(n).
    """

    if len(array) < 3:
        return simple_sort(array)

    # Choose a pivot at random
    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]

    left = []
    right = []
    for x in array:
        # put all elements inferior or equal to the pivot
        # to the left, the others to the right
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    # sort left and right, then join the results
    left_sorted = quicksort_simple(left)
    right_sorted = quicksort_simple(right)

    # We do not put the pivot in the middle because it has been added to the left
    result = left_sorted + right_sorted
    return result


def simple_sort(array):
    """ Used for sorting arrays with size less than 3. """
    if len(array) > 2:
        raise Exception('Cannot handle arrays with size superior to 2')
    if len(array) < 2:
        return array

    if array[0] > array[1]:
        return [array[1], array[0]]
    else:
        return array


if __name__ == '__main__':
    quicksort_simple([12, 5, 4, 9, 145, 46, 9, 18])
