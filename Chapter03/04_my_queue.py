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


class MyQueue(object):
    def __init__(self):
        self.newest = Stack(10)
        self.oldest = Stack(10)

    def add(self, value):
        self.newest.push(value)

    def shift_stacks(self):
        if self.oldest.is_empty():
            while not self.newest.is_empty():
                self.oldest.push(self.newest.pop())

    def peek(self):
        self.shift_stacks()
        return self.oldest.peek()

    def remove(self):
        self.shift_stacks()
        return self.oldest.pop()

    def is_empty(self):
        return self.newest.is_empty() and self.oldest.is_empty()


class Test(unittest.TestCase):
    def test_set_of_stacks(self):
        data = [1,2,3,4,5,6,7]
        queue = MyQueue()
        for i in range(4):
            queue.add(data[i])

        for i in range(4):
            self.assertEqual(data[i], queue.remove())

        for i in range(4, 7):
            queue.add(data[i])

        for i in range(4, 7):
            self.assertEqual(data[i], queue.remove())

        self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    unittest.main()
