import unittest


def string_rotation(a, b):
    if len(a) != len(b):
        return False
    
    if a in b + b:
        return True
    return False


class Test(unittest.TestCase):
    dataT = [('waterbottle', 'erbottlewat'), ('abc', 'bca'), ('a', 'a')]
    dataF = [('waterbottle', 'erbotltewat'), ('abc', 'abb'), ('', 'a')]

    def test_true(self):
        for d in self.dataT:
            self.assertTrue(string_rotation(d[0], d[1]))

    def test_false(self):
        for d in self.dataF:
            self.assertFalse(string_rotation(d[0], d[1]))


if __name__ == '__main__':
    unittest.main()
