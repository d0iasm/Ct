import unittest
from LinkedList import LinkedList, Node


def length(n):
    result = 0
    while n:
        result += 1
        n = n.next
    return result


def pad_zero(n, num):
    new_head = n
    next_node = n
    for _ in range(num):
        new_head = Node(0)
        new_head.next = next_node
        next_node = new_head
    return new_head


def add_lists_from_front(n1, n2):
    len1 = length(n1)
    len2 = length(n2)
    if len1 > len2:
        n2 = pad_zero(n2, len1-len2)
    else:
        n1 = pad_zero(n1, len2-len1)

    result = 0
    while n1 and n2:
        result = (result * 10) + n1.data + n2.data
        n1 = n1.next
        n2 = n2.next

    ll = LinkedList()
    for c in str(result):
        ll.append(int(c))

    return ll


def add_lists_from_front_recursively(n1, n2):
    len1 = length(n1)
    len2 = length(n2)
    if len1 > len2:
        n2 = pad_zero(n2, len1-len2)
    else:
        n1 = pad_zero(n1, len2-len1)

    result, carry = add_lists_helper(n1, n2)

    if carry > 0:
        n = Node(carry)
        n.next = result
        return n
    return result


def add_lists_helper(n1, n2):
    if n1 is None and n2 is None:
        return None, 0

    n, carry = add_lists_helper(n1.next, n2.next)
    val = carry + n1.data + n2.data
    new = Node(val % 10)
    new.next = n

    return new, 1 if val >= 10 else 0


class Test(unittest.TestCase):
    def test_add_lists(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,6]
        l2_data = [5,9,2]
        expected = [1,3,0,8]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)
        
        result = add_lists_from_front(l1.head, l2.head)
        n = result.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_increasing_the_number_of_digits(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7]
        l2_data = [5,9,2]
        expected = [1,3,0,9]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)
        
        result = add_lists_from_front(l1.head, l2.head)
        n = result.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_different_length(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7,1]
        l2_data = [5,9,2]
        expected = [7,7,6,3]
        for l1d in l1_data:
            l1.append(l1d)
        for l2d in l2_data:
            l2.append(l2d)
        
        result = add_lists_from_front(l1.head, l2.head)
        n = result.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_recursively(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,6]
        l2_data = [5,9,2]
        expected = [1,3,0,8]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)
        
        n = add_lists_from_front_recursively(l1.head, l2.head)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_recursively_increasing_the_number_of_digits(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7]
        l2_data = [5,9,2]
        expected = [1,3,0,9]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)
        
        n = add_lists_from_front_recursively(l1.head, l2.head)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_recursively_different_length(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7,1]
        l2_data = [5,9,2]
        expected = [7,7,6,3]
        for l1d in l1_data:
            l1.append(l1d)
        for l2d in l2_data:
            l2.append(l2d)
        
        n = add_lists_from_front_recursively(l1.head, l2.head)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next


if __name__ == '__main__':
    unittest.main()
