import unittest


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create_minimal_bst(array):
    return create_minimal_bst_helper(array, 0, len(array) - 1)


def create_minimal_bst_helper(array, start, end):
    if end < start:
        return None

    mid = (end + start) // 2
    node = Node(array[mid])
    node.left = create_minimal_bst_helper(array, start, mid - 1)
    node.right = create_minimal_bst_helper(array, mid + 1, end)
    return node


class Test(unittest.TestCase):
    def test_create_minimal_bst_odd_array(self):
        array = [0, 1, 2, 3, 4]
        bst = create_minimal_bst(array)
        self.assertEqual(2, bst.data)
        self.assertEqual(0, bst.left.data)
        self.assertEqual(3, bst.right.data)
        self.assertEqual(1, bst.left.right.data)
        self.assertEqual(4, bst.right.right.data)
        self.assertIsNone(bst.left.left)
        self.assertIsNone(bst.right.left)

    def test_create_minimal_bst_even_array(self):
        array = [0, 1, 2, 3, 4, 5]
        bst = create_minimal_bst(array)
        self.assertEqual(2, bst.data)
        self.assertEqual(0, bst.left.data)
        self.assertEqual(4, bst.right.data)
        self.assertEqual(1, bst.left.right.data)
        self.assertEqual(3, bst.right.left.data)
        self.assertEqual(5, bst.right.right.data)
        self.assertIsNone(bst.left.left)


if __name__ == '__main__':
    unittest.main()
