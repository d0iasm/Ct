import unittest


def check_permutation(a, b):
    if len(a) != len(b): return False

    chars = [0 for _ in range(128)] # Only Ascii
    for c in a:
        chars[ord(c)] += 1
    
    for c in b:
        asci = ord(c)
        chars[asci] -= 1
        if chars[asci] < 0:
            return False

    return True


def check_permutation_sorting(a, b):
    if len(a) != len(b): return False

    sorted_a = sorted(a)
    sorted_b = sorted(b)
    for i in range(len(a)):
        if sorted_a[i] != sorted_b[i]:
            return False

    return True
    

class Test(unittest.TestCase):
    dataT = [('abcd', 'cadb'), ('1571', '7511'), ('', '')]
    dataF = [('abcd', 'abc'), ('1436', '1537'), ('  ', ' !')]

    def test_ture(self):
        for d in self.dataT:
            self.assertTrue(check_permutation(d[0], d[1]))

    def test_false(self):
        for d in self.dataF:
            self.assertFalse(check_permutation(d[0], d[1]))

    def test_ture_sorting(self):
        for d in self.dataT:
            self.assertTrue(check_permutation_sorting(d[0], d[1]))

    def test_false_sorting(self):
        for d in self.dataF:
            self.assertFalse(check_permutation_sorting(d[0], d[1]))


if __name__ == '__main__':
    unittest.main()
