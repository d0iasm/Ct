import unittest


class FixedMultiStack(object):
    def __init__(self, size):
        self.number_of_stack = 3
        self.stack_capacity = size
        self.values = [0 for _ in range(size * self.number_of_stack)]
        self.sizes = [0 for _ in range(self.number_of_stack)]

    def push(self, num, value):
        assert self.is_full(num) is False, "Stack is full"
        self.sizes[num] += 1
        self.values[self.index_top(num)] = value

    def pop(self, num):
        assert self.is_empty(num) is False, "Stack is empty"

        top_idx = self.index_top(num)
        value = self.values[top_idx]
        self.values[top_idx] = 0
        self.sizes[num] -= 1
        return value

    def peek(self, num):
        assert self.is_empty(num) is False, "Stack is empty"

        return self.values[self.index_top(num)]

    def is_empty(self, num):
        return self.sizes[num] == 0

    def is_full(self, num):
        return self.sizes[num] == self.stack_capacity

    def index_top(self, num):
        offset = num * self.stack_capacity
        size = self.sizes[num]
        return offset + size - 1


class Test(unittest.TestCase):
    def test_fixed_multi_stack_correct_push_pop(self):
        data = [0,0,1,1,2,2]
        expected = [2,2,1,1,0,0]
        stack = FixedMultiStack(2)
        for d in data:
            stack.push(d, d)

        for e in expected:
            self.assertEqual(e, stack.pop(e))

        for e in expected:
            self.assertTrue(stack.is_empty(e))

    def test_fixed_multi_stack_correct_push_peek(self):
        data = [0,0,1,1,2,2]
        expected = [2,2,1,1,0,0]
        stack = FixedMultiStack(2)
        for d in data:
            stack.push(d, d)

        for e in expected:
            self.assertEqual(e, stack.peek(e))
            self.assertTrue(stack.is_full(e))


if __name__ == '__main__':
    unittest.main()
