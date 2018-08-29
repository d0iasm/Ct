import unittest
from LinkedList import LinkedList


def intersection(ll1, ll2):
    pass
    # TODO: Implement

class Test(unittest.TestCase):
    def test_intersection(self):
        ll = LinkedList()
        data = [1,6,1,6,1,6]
        expected = [1,1,1,6,6,6]
        for d in data:
            ll.append(d)

        n = partition(ll, 6)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next


if __name__ == '__main__':
    unittest.main()
