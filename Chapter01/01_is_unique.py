import unittest


def is_unique(string):
    if len(string) > 128: return False

    chars = [0 for _ in range(128)]
    for c in string:
        asci = ord(c)
        chars[asci] += 1
        if chars[asci] > 1:
            return False
    return True


def is_unique_sorting(string):
    sorted_string = sorted(string)
    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i+1]:
            return False

    return True


class Test(unittest.TestCase):
    dataT = ['abcd', '?>41g', '']
    dataF = ['abad', 'abc 11', '  ']

    def test_ture(self):
        for d in self.dataT:
            self.assertTrue(is_unique(d))

    def test_false(self):
        for d in self.dataF:
            self.assertFalse(is_unique(d))

    def test_ture_sorting(self):
        for d in self.dataT:
            self.assertTrue(is_unique_sorting(d))

    def test_false_sorting(self):
        for d in self.dataF:
            is_unique_sorting(d)
            self.assertFalse(is_unique_sorting(d))


if __name__ == '__main__':
    unittest.main()
