import unittest


def palindrome_permutation(string):
    asc_table = [0 for _ in range(128)] # Only Ascii
    odd_count = 0

    for c in string:
        asc_table[ord(c)] += 1
        if (asc_table[ord(c)] % 2 == 1):
            odd_count += 1
        else:
            odd_count -= 1

    return True if odd_count <= 1 else False


class Test(unittest.TestCase):
    dataT = ['tacocat', 'atcocta', '', ' ', 'aaa']
    dataF = ['tacocaa', 'atcoctt', ' a', 'ab', 'aaba']

    def test_ture(self):
        for d in self.dataT:
            self.assertTrue(palindrome_permutation(d))

    def test_false(self):
        for d in self.dataF:
            self.assertFalse(palindrome_permutation(d))


if __name__ == '__main__':
    unittest.main()
