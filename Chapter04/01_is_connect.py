import unittest


def is_connect(graph, start, end):
    if start == end:
        return True

    queue = graph[start]
    is_visitied = []
    while queue:
        node = queue.pop()
        if node == end:
            return True

        if node in is_visitied:
            continue
        else:
            is_visitied.append(node)

        queue += graph[node]

    return False


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.graph = {'A': ['B', 'C'],
                      'B': ['C', 'D'],
                      'C': ['D'],
                      'D': ['C'],
                      'E': ['F'],
                      'F': ['C']}

    def test_is_connect_short_path(self):
        self.assertTrue(is_connect(self.graph, 'A', 'B'))

    def test_is_connect_long_path(self):
        self.assertTrue(is_connect(self.graph, 'E', 'D'))

    def test_is_not_connect_short_path(self):
        self.assertFalse(is_connect(self.graph, 'B', 'A'))
   
    def test_is_not_connect_long_path(self):
        self.assertFalse(is_connect(self.graph, 'D', 'E'))

    def test_is_connect_same(self):
        self.assertTrue(is_connect(self.graph, 'A', 'A'))


if __name__ == '__main__':
    unittest.main()
