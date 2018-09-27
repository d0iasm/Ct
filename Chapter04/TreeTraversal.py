import unittest


class Node(object):
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node


pre_order_result = []
def pre_order(node):
    if node is not None:
        pre_order_result.append(node.name)
        pre_order(node.left)
        pre_order(node.right)


in_order_result = []
def in_order(node):
    if node is not None:
        in_order(node.left)
        in_order_result.append(node.name)
        in_order(node.right)


post_order_result = []
def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        post_order_result.append(node.name)


bfs_result = []
def bfs(node):
    bfs_result.append(node.name)
    queue = [node.left, node.right]
    while queue:
        n = queue.pop(0)
        if n is not None:
            bfs_result.append(n.name)
            queue.append(n.left)
            queue.append(n.right)


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        root = Node(0)
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_1.add_left(node_3)
        node_1.add_right(node_4)
        node_2.add_left(node_5)
        root.add_left(node_1)
        root.add_right(node_2)
        self.tree = root

    def test_pre_order(self):
        expected = [0, 1, 3, 4, 2, 5]
        pre_order(self.tree)
        self.assertEqual(expected, pre_order_result)

    def test_in_order(self):
        expected = [3, 1, 4, 0, 5, 2]
        in_order(self.tree)
        self.assertEqual(expected, in_order_result)

    def test_post_order(self):
        expected = [3, 4, 1, 5, 2, 0]
        post_order(self.tree)
        self.assertEqual(expected, post_order_result)

    def test_bfs(self):
        expected = [0, 1, 2, 3, 4, 5]
        bfs(self.tree)
        self.assertEqual(expected, bfs_result)


if __name__ == '__main__':
    unittest.main()
