import unittest


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

last_printed = None
def check_bst(node):
    global last_printed
    if node is None:
        return True

    if check_bst(node.left) is False:
        return False

    if last_printed is not None and node.data <= last_printed:
        return False
    last_printed = node.data

    if check_bst(node.right) is False:
        return False

    return True


class Test(unittest.TestCase):
    def test_true_balanced_bst(self):
        global last_printed
        last_printed = None
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
        root = node_4
        self.assertTrue(check_bst(root))

    def test_true_unbalanced_bst(self):
        global last_printed
        last_printed = None
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)
        node_2.left = node_1
        node_2.right = node_4
        node_4.left = node_3
        node_4.right = node_6
        node_6.left = node_5
        node_6.right = node_7
        root = node_2
        self.assertTrue(check_bst(root))

    def test_false_unbalanced_bst(self):
        global last_printed
        last_printed = None
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)
        node_2.left = node_1
        node_2.right = node_3
        node_3.left = node_4
        node_3.right = node_5
        node_5.left = node_6
        node_5.right = node_7
        root = node_2
        self.assertFalse(check_bst(root))


if __name__ == '__main__':
    unittest.main()
