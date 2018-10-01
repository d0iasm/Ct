import unittest


class BinaryHeapTree(object):
    def __init__(self, heap):
        self.heap = list(sorted(heap))

    def push(self, data):
        self.heap.append(data)
        self.up_heap()

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()

        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.down_heap()
        return min_element

    def peek(self):
        return self.heap[0]

    def up_heap(self):
        idx = len(self.heap) - 1
        while idx > 0:
            if self.heap[(idx-1) // 2] > self.heap[idx]:
                self.heap[idx], self.heap[(idx-1) // 2] = \
                    self.heap[(idx-1) // 2], self.heap[idx]
                idx = (idx-1) // 2
            else:
                return

    def down_heap(self):
        idx = 0
        while (idx*2+1) < len(self.heap):
            nextidx = idx*2 + 1
            if nextidx + 1 < len(self.heap):
                if self.heap[nextidx+1] < self.heap[nextidx]:
                    nextidx = nextidx + 1
           
            if self.heap[idx] > self.heap[nextidx]:
                self.heap[idx], self.heap[nextidx] = \
                    self.heap[nextidx], self.heap[idx]
            idx = nextidx


class Test(unittest.TestCase):
    def test_add_min_element(self):
        tree = BinaryHeapTree([4,5,6,7,2,1,3])
        tree.push(0)
        self.assertEqual(0, tree.peek())

    def test_add_middle_element(self):
        tree = BinaryHeapTree([4,8,6,7,2,1,5])
        tree.push(3)
        self.assertEqual(1, tree.peek())

    def test_get_min(self):
        tree = BinaryHeapTree([4,5,6,0,2,1,3])
        expected = [0,1,2,3,4,5,6]
        for e in expected:
            self.assertEqual(e, tree.pop())


if __name__ == '__main__':
    unittest.main()
