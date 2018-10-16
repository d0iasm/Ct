import unittest


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None


def common_ancestor(p, q):
    diff = depth(p) - depth(q)
    first = q if diff > 0 else p
    second = p if diff > 0 else q
    second = go_up_by(second, abs(diff))

    while first is not second and second is not None:
        first = first.parent
        second = second.parent

    if first is None or second is None:
        return None
    return first


def go_up_by(n, diff):
    while diff > 0 and n is not None:
        n = n.parent
        diff -= 1
    return n


def depth(n):
    depth = 0
    while n is not None:
        n = n.parent
        depth += 1
    return depth


def covers(root, p):
    if root is None:
        return False
    if root is p:
        return True
    return covers(root.left, p) or covers(root.right, p)


def common_ancestor_without_parent(root, p, q):
    if covers(root, p) is False or covers(root, q) is False:
        return None
    return ancestor_helper(root, p, q)


def ancestor_helper(root, p, q):
    if root is None or root is p or root is q:
        return root

    p_is_on_left = covers(root.left, p)
    q_is_on_left = covers(root.left, q)
    if p_is_on_left is not q_is_on_left:
        return root

    child_side = root.left if p_is_on_left else root.right
    return ancestor_helper(child_side, p, q)


class Test(unittest.TestCase):
    def test_top_common_ancestor(self):
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

        self.assertEqual(4, common_ancestor(node_2, node_7).data)

    def test_middle_common_ancestor(self):
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

        self.assertEqual(6, common_ancestor(node_5, node_7).data)

    def test_same_common_ancestor(self):
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

        self.assertEqual(5, common_ancestor(node_5, node_5).data)

    def test_none_common_ancestor(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)

        node_4.left = node_2
        node_2.parent = node_4

        node_2.left = node_1
        node_2.right = node_3
        node_1.parent = node_2
        node_3.parent = node_2

        node_6.left = node_5
        node_6.right = node_7
        node_5.parent = node_6
        node_7.parent = node_6

        self.assertIsNone(common_ancestor(node_2, node_7))

    def test_top_common_ancestor_wo_parent(self):
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

        self.assertEqual(4, common_ancestor_without_parent(root, node_2, node_7).data)

    def test_middle_common_ancestor_wo_parent(self):
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

        self.assertEqual(6, common_ancestor_without_parent(root, node_5, node_7).data)

    def test_same_common_ancestor_wo_parent(self):
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

        self.assertEqual(5, common_ancestor_without_parent(root, node_5, node_5).data)

    def test_none_common_ancestor_wo_parent(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)
        node_4.left = node_2
        node_2.left = node_1
        node_2.right = node_3
        root = node_4

        node_6.left = node_5
        node_6.right = node_7

        self.assertIsNone(common_ancestor_without_parent(root, node_2, node_7))


if __name__ == '__main__':
    unittest.main()
