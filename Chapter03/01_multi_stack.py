import unittest


class FixedMultiStack(object):
    pass
def fixed_multi_stack():
    pass


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
