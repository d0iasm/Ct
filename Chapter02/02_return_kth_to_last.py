import unittest
from LinkedList import LinkedList


def return_kth_to_last(ll, k):
    cur = runner = ll.head

    for _ in range(k):
        if runner is None:
            raise ValueError('Invalid K argument')
        runner = runner.next

    while runner:
        cur = cur.next
        runner = runner.next

    return cur.data


def return_kth_node_to_last_recursively(head, k):
    if head is None: return (head, 0)

    nd, idx = return_kth_node_to_last_recursively(head.next, k)
    idx += 1

    if idx == k:
        return (head, idx)
    return (nd, idx)


def return_kth_to_last_recursively(ll, k):
    nd, _ = return_kth_node_to_last_recursively(ll.head, k)
    if nd == None:
        return None
    return nd.data


class Test(unittest.TestCase):
    def test_return_kth(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertEqual(4, return_kth_to_last(ll, 2))

    def test_return_first(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertEqual(5, return_kth_to_last(ll, 1))

    def test_return_last(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertEqual(1, return_kth_to_last(ll, 5))

    def test_return_invalid_kth(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        with self.assertRaises(ValueError):
            return_kth_to_last(ll, 10)

    def test_return_kth_recursively(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertEqual(4, return_kth_to_last_recursively(ll, 2))

    def test_return_first_recursively(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertEqual(5, return_kth_to_last_recursively(ll, 1))


    def test_return_last_recursively(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertEqual(1, return_kth_to_last_recursively(ll, 5))

    def test_return_invalid_kth_recursively(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertIsNone(return_kth_to_last_recursively(ll, 10))


if __name__ == '__main__':
    unittest.main()
