import unittest
import sys


class StackWithMinByDoubleStack(object):
    def __init__(self, size):
        self.index = 0
        self.capacity = size
        self.values = [0 for _ in range(self.capacity)]
        self.mins = []

    def push(self, value):
        assert self.is_full() is False, "Stack is full"
        self.values[self.index] = value
        self.index += 1

        if len(self.mins) == 0:
            self.mins.append(value)

        if value <= self.get_min():
            self.mins.append(value)

    def pop(self):
        assert self.is_empty() is False, "Stack is empty"

        self.index -= 1
        value = self.values[self.index]
        self.values[self.index] = sys.maxsize

        if value == self.get_min() and len(self.mins) > 1:
            self.mins.pop()

        return value

    def peek(self):
        assert self.is_empty() is False, "Stack is empty"

        return self.values[self.index - 1]

    def is_empty(self):
        return self.index == 0

    def is_full(self):
        return self.index == self.capacity

    def get_min(self):
        if len(self.mins) == 0:
            return sys.maxsize
        return self.mins[len(self.mins) - 1]


class StackWithMin(object):
    def __init__(self, size):
        self.index = 0
        self.min = sys.maxsize
        self.capacity = size
        self.values = [0 for _ in range(self.capacity)]

    def push(self, value):
        assert self.is_full() is False, "Stack is full"
        self.values[self.index] = value
        self.index += 1

        if value < self.min:
            self.min = value

    def pop(self):
        assert self.is_empty() is False, "Stack is empty"

        self.index -= 1
        value = self.values[self.index]
        self.values[self.index] = sys.maxsize

        if value <= self.min:
            new_min = sys.maxsize
            for v in self.values:
                if v < new_min:
                    new_min = v
            self.min = new_min

        return value

    def peek(self):
        assert self.is_empty() is False, "Stack is empty"

        return self.values[self.index - 1]

    def is_empty(self):
        return self.index == 0

    def is_full(self):
        return self.index == self.capacity

    def get_min(self):
        return self.min


class Test(unittest.TestCase):
    def test_stack_min_correct_push_pop(self):
        data = [0,0,1,1,2,2]
        expected = [2,2,1,1,0,0]
        stack = StackWithMin(6)
        for d in data:
            stack.push(d)

        for e in expected:
            self.assertEqual(0, stack.get_min())
            self.assertEqual(e, stack.pop())

        self.assertTrue(stack.is_empty())

    def test_stack_min_correct_push_peek(self):
        data = [0,0,1,1,2,2]
        stack = StackWithMin(6)
        for d in data:
            stack.push(d)

        self.assertEqual(2, stack.peek())
        self.assertEqual(0, stack.get_min())
        self.assertTrue(stack.is_full())

    def test_stack_min_correct_push_pop_reverse(self):
        data = [2,2,1,1,0,0]
        expected = [0,0,1,1,2,2]
        stack = StackWithMin(6)
        for d in data:
            stack.push(d)

        for i in range(len(expected)):
            self.assertEqual(expected[i], stack.get_min())
            self.assertEqual(expected[i], stack.pop())

        self.assertTrue(stack.is_empty())

    def test_stack2_min_correct_push_pop(self):
        data = [0,0,1,1,2,2]
        expected = [2,2,1,1,0,0]
        stack = StackWithMinByDoubleStack(6)
        for d in data:
            stack.push(d)

        for e in expected:
            self.assertEqual(0, stack.get_min())
            self.assertEqual(e, stack.pop())

        self.assertTrue(stack.is_empty())

    def test_stack2_min_correct_push_peek(self):
        data = [0,0,1,1,2,2]
        stack = StackWithMinByDoubleStack(6)
        for d in data:
            stack.push(d)

        self.assertEqual(2, stack.peek())
        self.assertEqual(0, stack.get_min())
        self.assertTrue(stack.is_full())

    def test_stack2_min_correct_push_pop_reverse(self):
        data = [2,2,1,1,0,0]
        expected = [0,0,1,1,2,2]
        stack = StackWithMinByDoubleStack(6)
        for d in data:
            stack.push(d)

        for e in expected:
            self.assertEqual(e, stack.get_min())
            self.assertEqual(e, stack.pop())


if __name__ == '__main__':
    unittest.main()
