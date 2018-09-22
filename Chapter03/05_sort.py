import unittest
import sys


class Stack(object):
    def __init__(self, size):
        self.index = 0
        self.capacity = size
        self.values = [0 for _ in range(self.capacity)]

    def push(self, value):
        assert self.is_full() is False, "Stack is full"
        self.values[self.index] = value
        self.index += 1

    def pop(self):
        assert self.is_empty() is False, "Stack is empty"

        self.index -= 1
        value = self.values[self.index]
        self.values[self.index] = sys.maxsize

        return value

    def peek(self):
        assert self.is_empty() is False, "Stack is empty"

        return self.values[self.index - 1]

    def is_empty(self):
        return self.index == 0

    def is_full(self):
        return self.index == self.capacity


def sort(stack):
    sorted_stack = Stack(10)
    while stack.is_empty() == False:
        tmp = stack.pop()
        while sorted_stack.is_empty() == False and sorted_stack.peek() > tmp:
            stack.push(sorted_stack.pop())
        sorted_stack.push(tmp)

    while sorted_stack.is_empty() == False:
        stack.push(sorted_stack.pop())


class Test(unittest.TestCase):
    def test_sort(self):
        data = [3,4,1,6,3,8,2]
        expected = [1,2,3,3,4,6,8]
        stack = Stack(10)
        for d in data:
            stack.push(d)

        sort(stack)

        for e in expected:
            self.assertEqual(e, stack.pop())
        self.assertTrue(stack.is_empty())

    def test_sort_same_elements(self):
        data = [1,1,1,1,1]
        expected = [1,1,1,1,1]
        stack = Stack(10)
        for d in data:
            stack.push(d)

        sort(stack)

        for e in expected:
            self.assertEqual(e, stack.pop())
        self.assertTrue(stack.is_empty())

    def test_sort_already_sorted_stack(self):
        data = [5,4,3,2,1]
        expected = [1,2,3,4,5]
        stack = Stack(10)
        for d in data:
            stack.push(d)

        sort(stack)

        for e in expected:
            self.assertEqual(e, stack.pop())
        self.assertTrue(stack.is_empty())

    def test_sort_reverse_sorted_stack(self):
        data = [1,2,3,4,5]
        expected = [1,2,3,4,5]
        stack = Stack(10)
        for d in data:
            stack.push(d)

        sort(stack)

        for e in expected:
            self.assertEqual(e, stack.pop())
        self.assertTrue(stack.is_empty())


if __name__ == '__main__':
    unittest.main()
