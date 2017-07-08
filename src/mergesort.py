#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# MergeSort algorithm implementation
#
#
# Author: Alexis Vanacker
# Date: 2017/07/08
#


def merge_sort(int_array):
    """ A basic implementation that does not do the sort inplace."""
    size = len(int_array)
    if size == 1 or size == 0:
        return int_array
    else:
        # Cut the array in half
        first_half_max = (size / 2) - 1
        # take all from 0 to first_half_max
        # remembler in Python slices, the last index is excluded
        first_half = int_array[0: first_half_max + 1]
        second_half = int_array[first_half_max + 1: size]
        print 'First half: {}'.format(first_half)
        print 'Second half: {}'.format(second_half)

        # Sort both halves
        result_left = merge_sort(first_half)
        result_right = merge_sort(second_half)

        # Merge the results
        result = merge_sorted_arrays(result_left, result_right)

        return result


def merge_sorted_arrays(array1, array2):
    """ Merges two sorted arrays into a single sorted one.

    We maintain a pointer on each of the arrays, compare the value
    on that pointer, and pop the smaller one. We repeat until one
    of the arrays is empty. We then append the remaining values in
    the sorted array.
    """
    print 'Merging {} and {}'.format(array1, array2)
    pointer1 = 0
    pointer2 = 0

    result = []
    while pointer1 < len(array1) and pointer2 < len(array2):
        value1 = array1[pointer1]
        value2 = array2[pointer2]
        if value1 < value2:
            result.append(value1)
            pointer1 += 1
        else:
            result.append(value2)
            pointer2 += 1

    if pointer1 < len(array1):
        result.extend(array1[pointer1:])
    elif pointer2 < len(array2):
        result.extend(array2[pointer2:])

    return result


if __name__ == '__main__':
    main()
