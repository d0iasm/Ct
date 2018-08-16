import unittest
from LinkedList import LinkedList


def remove_deps_with_buffer(ll):
    dic = {}
    n = ll.head
    if n == None or n.next == None:
        return ll
    dic[n.data] = True

    while n.next:
        if n.next.data in dic:
            n.next = n.next.next
        else:
            dic[n.next.data] = True
            n = n.next
    return ll


def remove_deps_without_buffer(ll):
    cur = ll.head

    while cur:
        runner = cur
        while runner.next:
            if cur.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next


class Test(unittest.TestCase):
    def test_remove_deps_with_buffer(self):
        ll = LinkedList()
        data = [1,1,2,2,3,3]
        expected = [1,2,3]
        for d in data:
            ll.append(d)
        
        remove_deps_with_buffer(ll)

        n = ll.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_unremove_deps_with_buffer(self):
        ll = LinkedList()
        data = [1,2,3,4,5,6]
        expected = [1,2,3,4,5,6]
        for d in data:
            ll.append(d)
        
        remove_deps_with_buffer(ll)

        n = ll.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_remove_deps_without_buffer(self):
        ll = LinkedList()
        data = [1,1,2,2,3,3]
        expected = [1,2,3]
        for d in data:
            ll.append(d)
        
        remove_deps_without_buffer(ll)

        n = ll.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_unremove_deps_without_buffer(self):
        ll = LinkedList()
        data = [1,2,3,4,5,6]
        expected = [1,2,3,4,5,6]
        for d in data:
            ll.append(d)
        
        remove_deps_without_buffer(ll)

        n = ll.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next

    def test_empty_with_buffer(self):
        ll = LinkedList()
        remove_deps_with_buffer(ll)
        self.assertIsNone(ll.head)

    def test_empty_without_buffer(self):
        ll = LinkedList()
        remove_deps_without_buffer(ll)
        self.assertIsNone(ll.head)


if __name__ == '__main__':
    unittest.main()
