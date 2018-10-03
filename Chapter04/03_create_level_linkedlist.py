import unittest
from LinkedList import LinkedList


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create_level_linkedlist(root, lists, level):
    if root is None:
        return

    li = None
    if len(lists) == level:
        li = LinkedList()
        lists.append(li)
    else:
        li = lists[level]

    li.append(root.data)
    create_level_linkedlist(root.left, lists, level+1)
    create_level_linkedlist(root.right, lists, level+1)


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)
        node_4.left = node_2
        node_4.right = node_6
        node_2.left = node_1
        node_2.right = node_3
        node_6.left = node_5
        node_6.right = node_7
        self.bst = node_4

    def test_create_level_linkedlist(self):
        lists = []
        create_level_linkedlist(self.bst, lists, 0)
        expected = [[4], [2, 6], [1, 3, 5, 7]]
        for lidx in range(len(expected)):
            node = lists[lidx].head
            for e in expected[lidx]:
                self.assertEqual(e, node.data)
                node = node.next


if __name__ == '__main__':
    unittest.main()
