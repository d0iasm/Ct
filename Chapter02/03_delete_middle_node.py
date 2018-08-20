import unittest
from LinkedList import LinkedList


def delete_middle_node(ll, n):
    if n is None or n.next is None:
        return False

    nx = n.next
    n.data = nx.data
    n.next = nx.next
    return True

class Test(unittest.TestCase):
    def test_delete_middle_node(self):
        ll = LinkedList()
        data = [1,2,3,4,5,6]
        expected = [1,2,3,5,6]
        for d in data:
            ll.append(d)
        
        n = ll.head
        for _ in range(3):
            n = n.next

        delete_middle_node(ll, n)
       
        n = ll.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next


if __name__ == '__main__':
    unittest.main()
