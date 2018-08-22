import unittest
from LinkedList import LinkedList


def partition(ll, k):
    head = ll.head
    tail = ll.head
    n = ll.head

    while n != None:
        nex = n.next
        if n.data < k:
            n.next = head
            head = n
        else:
            tail.next = n
            tail = n
        n = nex

    tail = None
    return head


def partition_stable(ll, k):
    n = ll.head
    bs = be = None
    afs = afe = None

    while n != None:
        if n.data < k:
            if bs == None:
                bs = n
                be = n
            else:
                be.next = n
                be = n
        else:
            if afs == None:
                afs = n
                afe = n
            else:
                afe.next = n
                afe = n
        n = n.next
    
    if be == None:
        return afs

    be.next = afs
    return bs


class Test(unittest.TestCase):
    def test_partition(self):
        ll = LinkedList()
        data = [1,6,1,6,1,6]
        expected = [1,1,1,6,6,6]
        for d in data:
            ll.append(d)

        n = partition(ll, 6)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_partition_allafter(self):
        ll = LinkedList()
        data = [5,5,5,5,5,5]
        expected = [5,5,5,5,5]
        for d in data:
            ll.append(d)

        n = partition(ll, 3)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_partition_allbefore(self):
        ll = LinkedList()
        data = [1,1,1,1,1,1]
        expected = [1,1,1,1,1,1]
        for d in data:
            ll.append(d)

        n = partition(ll, 3)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next
    
    def test_partition_stable(self):
        ll = LinkedList()
        data = [1,6,1,6,1,6]
        expected = [1,1,1,6,6,6]
        for d in data:
            ll.append(d)

        n = partition_stable(ll, 6)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_partition_stable_allafter(self):
        ll = LinkedList()
        data = [5,5,5,5,5,5]
        expected = [5,5,5,5,5]
        for d in data:
            ll.append(d)

        n = partition_stable(ll, 3)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_partition_stable_allbefore(self):
        ll = LinkedList()
        data = [1,1,1,1,1,1]
        expected = [1,1,1,1,1,1]
        for d in data:
            ll.append(d)

        n = partition_stable(ll, 3)
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next


if __name__ == '__main__':
    unittest.main()
