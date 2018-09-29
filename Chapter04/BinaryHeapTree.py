import unittest


class BinaryHeapTree(object):
    def __init__(self, heap):
        self.heap = list(sorted(heap))

    def push(self, data):
        self.heap.append(data)
        self.siftup()

    def pop(self):
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftdown()
        return min_element

    def peek(self):
        return self.heap[0]

    def siftup(self):
        idx = len(self.heap) - 1
        while idx > 0:
            if self.heap[(idx-1) // 2] > self.heap[idx]:
                self.heap[idx], self.heap[(idx-1) // 2] = \
                    self.heap[(idx-1) // 2], self.heap[idx]
                idx = (idx-1) // 2
            else:
                return

    def siftdown(self):
        idx = 0
        while idx < len(self.heap):
            left = self.heap[idx*2 + 1]
            right = self.heap[idx*2 + 2]
            if left <= right and self.heap[idx] > left:
                self.heap[idx*2 + 1] = self.heap[idx]
                self.heap[idx] = left
                idx = idx*2 + 1
            
            if right < left and self.heap[idx] > right:
                self.heap[idx*2 + 2] = self.heap[idx]
                self.heap[idx] = right
                idx = idx*2 + 2


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
