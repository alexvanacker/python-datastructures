#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Linked List implementation
#
# author: Alexis Vanacker - 2017/07/09


class LinkedList():
    """ A singly linked list implementation. The fun is mostly
    in the delete function. """

    def __init__(self):
        self.first = None
        self.size = 0

    def get_size(self):
        return self.size

    def add_value(self, value):
        new_node = Node(value)
        node = self.first
        if self.first is None:
            # Empty list edge case
            self.first = new_node
            self.size = 1
            return

        while node.next is not None:
            node = node.next
        node.next = new_node
        self.size += 1

    def delete_value(self, value):
        """ Deletes the first occurence of a value
        from the linked list."""

        if self.first is None:
            # DUMMY TEST
            print 'Cannot remove a value from an empty list'
            return

        if self.first.value == value:
            self.first = self.first.next
            self.size -= 1
            return

        node = self.first
        while node.next is not None:
            # Iterate until we find the value in the next node.next
            # If it is found, then update the current's node link
            # to the next "next" node.
            if node.next.value == value:
                print "Deleting value {}".format(value)
                # We update the node's link to it's "grandchild" node
                node.next = node.next.next
                self.size -= 1
                break

            node = node.next


    def get_all(self):
        """ Returns an array with all of the list's values.
        Debugging function."""
        node = self.first
        all_values = []
        while node is not None:
            all_values.append(node.value)
            node = node.next
        return all_values


    def remove_duplicates_no_buffer(self):
        """ A method for removing duplicates without using a buffer.
        We rely on two pointers: a current, which iterates on the list,
        and a prev_runner, which will iterate on all nodes that are located
        before the current node. The pointer prev_runner will be used to
        detect duplicates. It only detects one, but since we progress in the
        list, any other duplicates that were prior to current would already
        have been removed.
        previous is a pointer used for deletion. """

        if self.first is None:
            return

        previous = self.first
        current = previous.next
        while current is not None:
            runner = self.first
            while runner != current:
                if runner.value == current.value:
                    # Then we remove current
                    tmp = current.next
                    previous.next = tmp
                    current = tmp
                    # All other duplicates have been removed in a previous
                    # pass.
                    break

                runner = runner.next

            # Update current and previous
            if runner == current:
                previous = current
                current = current.next

    def pop(self):
        if self.first is not None:
            value = self.first.value
            self.first = self.first.second
            self.size -= 1
            return value
        else:
            return None

    def get_first(self):
        return self.first


class Node():
    """ An item of the linked list which contains
    a value and a pointer to the next element of the list."""

    def __init__(self, value):
        self.value = value
        self.next = None

    # def __eq__(self, other):
    #     if self is None and other is None:
    #         return True
    #     if self.value != other.value:
    #         return False
    #     else:
    #         return self.next == other.next
