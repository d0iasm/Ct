import unittest


def is_replace(a, b):
    is_diff_found = False
    for a_c, a_b in zip(a, b):
        if a_c != a_b:
            if is_diff_found:
                return False
            is_diff_found = True

    return True


def is_char_added(a, b):
    is_diff_found = False
    idxa = 0
    idxb = 0
    for _ in range(len(a)):
        if a[idxa] != b[idxb]:
            if is_diff_found:
                return False
            idxb += 1
            is_diff_found = True
        idxa += 1
        idxb += 1

    return True


def one_away(a, b):
    if len(a) == len(b):
        return is_replace(a, b)
    elif len(a) + 1 == len(b):
        return is_char_added(a, b)
    elif len(a) == len(b) + 1:
        return is_char_added(b, a)

    return False


class Test(unittest.TestCase):
    dataT = [('pale', 'ple'), ('ple', 'pale'), ('pales', 'pale'), ('pale', 'bale'), ('', '')]
    dataF = [('pale', 'bake'), ('ple', 'pala'), ('pala', 'ple'), ('  ', '')]

    def test_ture(self):
        for d in self.dataT:
            self.assertTrue(one_away(d[0], d[1]))

    def test_false(self):
        for d in self.dataF:
            self.assertFalse(one_away(d[0], d[1]))


if __name__ == '__main__':
    unittest.main()
