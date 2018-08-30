import unittest
from LinkedList import LinkedList, Node


def loop_detection(ll):
    n = ll.head
    node_hash = {}
    while n:
        if n not in node_hash:
            node_hash[n] = True
        else:
            return True
        n = n.next
    
    return False


def loop_detection_runner(ll):
    slow = ll.head
    fast = ll.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast


class Test(unittest.TestCase):
    def test_loop_detection_true(self):
        ll = LinkedList()
        head = Node(0)
        ll.head = head
        n = ll.head
        for i in range(1, 5):
            n.next = Node(i)
            n = n.next
        n.next = ll.head
            
        self.assertTrue(loop_detection(ll))


    def test_loop_detection_false(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)
            
        self.assertFalse(loop_detection(ll))


    def test_loop_detection_runner_find_first_element(self):
        ll = LinkedList()
        head = Node(0)
        ll.head = head
        n = ll.head
        for i in range(1, 5):
            n.next = Node(i)
            n = n.next
        n.next = ll.head
            
        self.assertEqual(0, loop_detection_runner(ll).data)


    def test_loop_detection_runner_find_second_element(self):
        ll = LinkedList()
        head = Node(0)
        ll.head = head
        n = ll.head
        second = Node(1)
        n.next = second
        n = n.next
        for i in range(2, 5):
            n.next = Node(i)
            n = n.next
        n.next = second
            
        self.assertEqual(1, loop_detection_runner(ll).data)


    def test_loop_detection_runner_false(self):
        ll = LinkedList()
        data = [1,2,3,4,5]
        for d in data:
            ll.append(d)
            
        self.assertIsNone(loop_detection_runner(ll))


if __name__ == '__main__':
    unittest.main()
