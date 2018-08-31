import unittest
from LinkedList import LinkedList, Node


def get_length_and_tail(ll):
    n = ll.head
    count = 0
    if n is None:
        return None, count

    while n.next:
        count += 1
        n = n.next

    return n, count

def find_intersection(ll1, ll2):
    t1, c1 = get_length_and_tail(ll1)
    t2, c2 = get_length_and_tail(ll2)
    if t1 is not t2:
        return None

    shorter = ll1.head if c1 < c2 else ll2.head
    longer = ll2.head if c1 < c2 else ll1.head

    for _ in range(abs(c1-c2)):
        longer = longer.next

    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    return shorter


class Test(unittest.TestCase):
    def test_find_intersection(self):
        ll1 = LinkedList()
        ll2 = LinkedList()
        data1 = [1,2]
        data2 = [2]
        data_shared = [3,4,5]

        n5 = Node(data_shared[2], None)
        n4 = Node(data_shared[1], n5)
        n3 = Node(data_shared[0], n4)
        n21 = Node(data1[1], n3)
        n11 = Node(data1[0], n21)
        n12 = Node(data2[0], n3)

        ll1.head = n11
        ll2.head = n12

        self.assertEqual(n3, find_intersection(ll1, ll2))


    def test_find_intersection_samelength(self):
        ll1 = LinkedList()
        ll2 = LinkedList()
        data1 = [1,2]
        data2 = [1,2]
        data_shared = [3,4,5]

        n5 = Node(data_shared[2], None)
        n4 = Node(data_shared[1], n5)
        n3 = Node(data_shared[0], n4)
        n21 = Node(data1[1], n3)
        n11 = Node(data1[0], n21)
        n22 = Node(data2[1], n3)
        n12 = Node(data2[0], n22)

        ll1.head = n11
        ll2.head = n12

        self.assertEqual(n3, find_intersection(ll1, ll2))


    def test_find_intersection_not_found(self):
        ll1 = LinkedList()
        ll2 = LinkedList()
        data = [1,2,3,4,5]

        for d in data:
            ll1.append(d)
            ll2.append(d)

        self.assertIsNone(find_intersection(ll1, ll2))


if __name__ == '__main__':
    unittest.main()
