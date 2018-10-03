"""
Linked List
"""

import unittest


class Node(object):
    """
    A node of a linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList(object):
    """
    A linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n

    def insert(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            return

        n.next = self.head
        self.head = n

    def delete(self, data):
        n = self.head
        if n.data == data:
            self.head = self.head.next
            return self.head

        while n.next:
            if n.next.data == data:
                n.next = n.next.next
                return self.head
            n = n.next
        return self.head

    def search(self, data):
        n = self.head
        if n == None: return None

        while n.next:
            if n.data == data:
                return n.data
            n = n.next

        if n.data == data:
            return n.data
        return None

    def is_empty(self):
        if self.head == None:
            return True
        return False


class Test(unittest.TestCase):
    data = [1,2,3,4,5]

    def test_append(self):
        ll = LinkedList()
        for d in self.data:
            ll.append(d)
        for d in self.data:
            self.assertEqual(d, ll.search(d))
        self.assertFalse(ll.is_empty())

    def test_append_delete_all(self):
        ll = LinkedList()
        for d in self.data:
            ll.append(d)
        for d in self.data:
            ll.delete(d)
        self.assertTrue(ll.is_empty())
        self.assertIsNone(ll.search(1))

    def test_append_nothing(self):
        ll = LinkedList()
        self.assertTrue(ll.is_empty())
        self.assertIsNone(ll.search(0))

    def test_insert(self):
        ll = LinkedList()
        for d in self.data:
            ll.insert(d)

        n = ll.head
        for d in reversed(self.data):
            self.assertEqual(d, n.data)
            n = n.next

    def test_search_none(self):
        ll = LinkedList()
        for d in self.data:
            ll.append(d)
        self.assertIsNone(ll.search(6))
        self.assertFalse(ll.is_empty())


if __name__ == '__main__':
    unittest.main()
