import unittest


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None


def inorder_succ(n):
    if n is None:
        return None
   
    if n.right is not None:
        return left_most_child(n.right)
    else:
        q = n
        x = q.parent
        while x is not None and x.left is not q:
            q = x
            x = x.parent
        return x


def left_most_child(n):
    if n is None:
        return None
    while n.left is not None:
        n = n.left
    return n


class Test(unittest.TestCase):
    def test_true_has_right_node(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)

        node_4.left = node_2
        node_4.right = node_6
        node_2.parent = node_4
        node_6.parent = node_4

        node_2.left = node_1
        node_2.right = node_3
        node_1.parent = node_2
        node_3.parent = node_2

        node_6.left = node_5
        node_6.right = node_7
        node_5.parent = node_6
        node_7.parent = node_6

        self.assertEqual(3, inorder_succ(node_2).data)

    def test_true_no_right_node(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)

        node_4.left = node_2
        node_4.right = node_6
        node_2.parent = node_4
        node_6.parent = node_4

        node_2.left = node_1
        node_2.right = node_3
        node_1.parent = node_2
        node_3.parent = node_2

        node_6.left = node_5
        node_6.right = node_7
        node_5.parent = node_6
        node_7.parent = node_6

        self.assertEqual(4, inorder_succ(node_3).data)

    def test_true_rightmost(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)

        node_4.left = node_2
        node_4.right = node_6
        node_2.parent = node_4
        node_6.parent = node_4

        node_2.left = node_1
        node_2.right = node_3
        node_1.parent = node_2
        node_3.parent = node_2

        node_6.left = node_5
        node_6.right = node_7
        node_5.parent = node_6
        node_7.parent = node_6

        self.assertIsNone(inorder_succ(node_7))

    def test_true_leftmost(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)

        node_4.left = node_2
        node_4.right = node_6
        node_2.parent = node_4
        node_6.parent = node_4

        node_2.left = node_1
        node_2.right = node_3
        node_1.parent = node_2
        node_3.parent = node_2

        node_6.left = node_5
        node_6.right = node_7
        node_5.parent = node_6
        node_7.parent = node_6

        self.assertEqual(2, inorder_succ(node_1).data)


if __name__ == '__main__':
    unittest.main()
