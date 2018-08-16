import unittest
from LinkedList import LinkedList


def return_kth_data_from_back(ll, k):
    cur = runner = ll.head

    for _ in range(k):
        if runner is None:
            raise ValueError('Invalid K argument')
        runner = runner.next

    while runner:
        cur = cur.next
        runner = runner.next

    return cur.data


class Test(unittest.TestCase):
    def test_return_kth(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertEqual(4, return_kth_data_from_back(ll, 2))

    def test_return_first(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertEqual(5, return_kth_data_from_back(ll, 1))


    def test_return_last(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        self.assertEqual(1, return_kth_data_from_back(ll, 5))

    def test_return_invalid_kth(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)

        with self.assertRaises(ValueError):
            return_kth_data_from_back(ll, 10)


if __name__ == '__main__':
    unittest.main()
