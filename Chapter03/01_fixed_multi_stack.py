import unittest


class FixedMultiStack(object):
    
    def __init__(self, size):
        self.number_of_stack = 3
        self.stack_capacity = size
        self.values = [0 for _ in range(size * self.number_of_stack)]
        self.sizes = [0 for _ in range(self.number_of_stack)]

    def push(self, num, value):
        assert self.is_full(num), "Stack is full"

        self.sizes[num] += 1
        self.values[self.index_top(num)] = value

    def pop(self, num):
        assert self.is_empty(num), "Stack is empty"

        top_idx = self.index_top(num)
        value = self.values[top_idx]
        self.values[top_idx] = 0
        self.sizes[num] -= 1
        return value


class Test(unittest.TestCase):
    def test_fixed_multi_stack(self):
        data = [1,1,2,2,3,3]
        expected = [1,2,3]
        for d in data:
            ll.append(d)
        

        n = ll.head
        for e in expected:
            self.assertEqual(e, n.data)
            n = n.next


if __name__ == '__main__':
    unittest.main()
