import unittest
from LinkedList import LinkedList, Node


def add_lists(l1, l2):
    n1 = l1.head
    n2 = l2.head
    result = LinkedList()
    carry = 0

    while n1 and n2:
        s = n1.data + n2.data
        result.append((s + carry) % 10)
        carry = 1 if (s + carry) >= 10 else 0
        n1 = n1.next
        n2 = n2.next

    while n1:
        if carry == 1:
            result.append((n1.data + carry) % 10)
            carry = 1 if n1.data + carry >= 10 else 0
        else:
            result.append(n1.data)
        n1 = n1.next

    while n2:
        if carry == 1:
            result.append((n2.data + carry) % 10)
            carry = 1 if n2.data + carry >= 10 else 0
        else:
            result.append(n2.data)
        n2 = n2.next

    if carry == 1:
        result.append(carry)

    return result


def add_lists_optimized(l1, l2):
    n1 = l1.head
    n2 = l2.head
    result = LinkedList()
    carry = 0
    val = 0

    while n1 or n2:
        if n1 != None:
            val += n1.data
            n1 = n1.next
        if n2 != None:
            val += n2.data
            n2 = n2.next

        result.append((val + carry) % 10)
        carry = 1 if (val + carry) >= 10 else 0
        val = 0
       
    if carry == 1:
        result.append(carry)

    return result


def add_lists_recursively(n1, n2, carry=0):
    if n1 is None and n2 is None and carry == 0:
        return None

    val = carry
    if n1 is not None:
        val += n1.data
    if n2 is not None:
        val += n2.data

    result_head = Node(val % 10)

    if n1 or n2:
        more = add_lists_recursively(n1.next if n1 else None,
                                     n2.next if n2 else None,
                                     1 if val >= 10 else 0)
        result_head.next = more

    return result_head


class Test(unittest.TestCase):
    def test_add_lists(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,6]
        l2_data = [5,9,2]
        expected = [2,1,9]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)

        result = add_lists(l1, l2)
        n = result.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_increasing_the_number_of_digits(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7]
        l2_data = [5,9,2]
        expected = [2,1,0,1]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)
        
        result = add_lists(l1, l2)
        n = result.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_different_length(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7,1]
        l2_data = [5,9,2]
        expected = [2,1,0,2]
        for l1d in l1_data:
            l1.append(l1d)
        for l2d in l2_data:
            l2.append(l2d)
        
        result = add_lists(l1, l2)
        n = result.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_optimized(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,6]
        l2_data = [5,9,2]
        expected = [2,1,9]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)
        
        result = add_lists_optimized(l1, l2)
        n = result.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_optimized_increasing_the_number_of_digits(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7]
        l2_data = [5,9,2]
        expected = [2,1,0,1]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)
        
        result = add_lists_optimized(l1, l2)
        n = result.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_optimize_different_length(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7,1]
        l2_data = [5,9,2]
        expected = [2,1,0,2]
        for l1d in l1_data:
            l1.append(l1d)
        for l2d in l2_data:
            l2.append(l2d)
        
        result = add_lists_optimized(l1, l2)
        n = result.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_recursively(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,6]
        l2_data = [5,9,2]
        expected = [2,1,9]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)
        
        n = add_lists_recursively(l1.head, l2.head)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_recursively_increasing_the_number_of_digits(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7]
        l2_data = [5,9,2]
        expected = [2,1,0,1]
        for l1d, l2d in zip(l1_data, l2_data):
            l1.append(l1d)
            l2.append(l2d)
        
        n = add_lists_recursively(l1.head, l2.head)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_recursively_different_length(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7,1]
        l2_data = [5,9,2]
        expected = [2,1,0,2]
        for l1d in l1_data:
            l1.append(l1d)
        for l2d in l2_data:
            l2.append(l2d)
        
        n = add_lists_recursively(l1.head, l2.head)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_add_lists_recursively_zero_length(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1_data = [7,1,7,1]
        l2_data = []
        expected = [7,1,7,1]
        for l1d in l1_data:
            l1.append(l1d)
        for l2d in l2_data:
            l2.append(l2d)
        
        n = add_lists_recursively(l1.head, l2.head)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next


if __name__ == '__main__':
    unittest.main()
