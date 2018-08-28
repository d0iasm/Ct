import unittest
from LinkedList import LinkedList


def is_palindrome_reverse(ll):
    reverse = LinkedList()

    n = ll.head
    count = 0
    while n:
        reverse.insert(n.data)
        n = n.next
        count += 1

    n = ll.head
    r = reverse.head
    for _ in range(count//2):
        if n.data != r.data:
            return False
        n = n.next
        r = r.next
    return True


def is_palindrome_loop(ll):
    slow = ll.head
    fast = ll.head
    stack = []
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        if stack.pop(-1) != slow.data:
            return False
        slow = slow.next
    return True


def is_palindrome_recusively(ll):
    pass


class Test(unittest.TestCase):
    def test_is_palindrome_reverse_true(self):
        ll = LinkedList()
        data = [1,2,3,3,2,1]
        for d in data:
            ll.append(d)
        self.assertTrue(is_palindrome_reverse(ll))

    def test_is_palindrome_reverse_false(self):
        ll = LinkedList()
        data = [1,2,3,4,5,6]
        for d in data:
            ll.append(d)
        self.assertFalse(is_palindrome_reverse(ll))

    def test_is_palindrome_reverse_zero(self):
        ll = LinkedList()
        data = []
        for d in data:
            ll.append(d)
        self.assertTrue(is_palindrome_reverse(ll))

    def test_is_palindrome_loop_true(self):
        ll = LinkedList()
        data = [1,2,3,3,2,1]
        for d in data:
            ll.append(d)
        self.assertTrue(is_palindrome_loop(ll))

    def test_is_palindrome_loop_false(self):
        ll = LinkedList()
        data = [1,2,3,4,5,6,7]
        for d in data:
            ll.append(d)
        self.assertFalse(is_palindrome_loop(ll))

    def test_is_palindrome_loop_zero(self):
        ll = LinkedList()
        data = []
        for d in data:
            ll.append(d)
        self.assertTrue(is_palindrome_loop(ll))


if __name__ == '__main__':
    unittest.main()
