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


class SetOfStacks(object):
    def __init__(self):
        self.stacks = []
        initial_stack = Stack(3)
        self.stacks.append(initial_stack)
        self.index = 0

    def push(self, value):
        if self.stacks[self.index].is_full():
            self.index += 1
            new_stack = Stack(3)
            self.stacks.append(new_stack)
        self.stacks[self.index].push(value)

    def pop(self):
        if self.stacks[self.index].is_empty():
            self.index -= 1

        return self.stacks[self.index].pop()

    def peek(self):
        return self.stacks[self.index].peek()

    def is_empty(self):
        return self.index == 0 and self.stacks[0].index == 0

    def is_full(self):
        return False

    def pop_at(self, idx):
        # TODO: Implement
    

class Test(unittest.TestCase):
    def test_set_of_stacks(self):
        data = [1,2,3,4,5,6,7]
        expected = [7,6,5,4,3,2,1]
        stack = SetOfStacks()
        for d in data:
            stack.push(d)

        for e in expected:
            self.assertEqual(e, stack.pop())

        self.assertTrue(stack.is_empty())


    def test_set_of_stacks_not_all_pop(self):
        data = [1,2,3,4,5,6,7]
        expected = [7,6,5,4,3,2]
        stack = SetOfStacks()
        for d in data:
            stack.push(d)

        for e in expected:
            self.assertEqual(e, stack.pop())

        stack.push(8)
        self.assertEqual(8, stack.pop())

        self.assertFalse(stack.is_empty())


if __name__ == '__main__':
    unittest.main()
