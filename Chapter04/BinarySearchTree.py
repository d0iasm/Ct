import unittest


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self, root):
        self.root = root

    def insert(self, data):
        n = self.root
        while n:
            if data < n.data:
                if n.left:
                    n = n.left
                else:
                    n.left = Node(data)
                    return
            else:
                if n.right:
                    n = n.right
                else:
                    n.right = Node(data)
                    return

    def delete(self, data):
        pass

    def find(self, data):
        pass


in_order_result = []
def in_order_for_test(node):
    if node is not None:
        in_order_for_test(node.left)
        in_order_result.append(node.data)
        in_order_for_test(node.right)


class Test(unittest.TestCase):
    def test_insert_bst(self):
        data = [5,1,6,3,2]
        bst = BinarySearchTree(Node(4))
        for d in data:
            bst.insert(d)
        in_order_for_test(bst.root)
        self.assertEqual([1,2,3,4,5,6], in_order_result)


if __name__ == '__main__':
    unittest.main()
