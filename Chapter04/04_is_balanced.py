import unittest
import sys
MIN = -sys.maxsize - 1


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_height(root):
    if root is None:
        return -1
    return max(get_height(root.left), get_height(root.right)) + 1


def is_balanced(root):
    if root is None:
        return True

    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


def check_height(root):
    if root is None:
        return -1

    left_height = check_height(root.left)
    if left_height == MIN:
        return MIN

    right_height = check_height(root.right)
    if right_height == MIN:
        return MIN

    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return MIN
    else:
        return max(left_height, right_height) + 1


def is_balanced2(root):
    return check_height(root) != MIN


class Test(unittest.TestCase):
    def test_true_balanced(self):
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
        self.assertTrue(is_balanced(root))

    def test_false_balanced(self):
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
        self.assertFalse(is_balanced(root))

    def test_true_balanced2(self):
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
        self.assertTrue(is_balanced2(root))

    def test_false_balanced2(self):
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
        self.assertFalse(is_balanced2(root))


if __name__ == '__main__':
    unittest.main()
