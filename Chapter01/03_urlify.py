import unittest


def urlify(string, length):
    space_count = 0
    for c in string:
        if c == ' ':
            space_count += 1

    idx = len(string) + space_count * 2
    string = list(string) + [' ' for _ in range(space_count * 2)]
    for i in reversed(range(length)):
        if string[i] == ' ':
            string[idx-3:idx] = '%20'
            idx -= 3
        else:
            string[idx - 1] = string[i]
            idx -= 1

    return ''.join(string)


class Test(unittest.TestCase):
    dataT = [('Mr Jogn Smith', 'Mr%20Jogn%20Smith'), ('a b c', 'a%20b%20c'), (' ', '%20')]
    dataF = [('Mr Jogn Smith', 'MrJognSmith'), ('a b', '%20b'), (' ', ' ')]

    def test_ture(self):
        for d in self.dataT:
            self.assertEqual(d[1], urlify(d[0], len(d[0])))

    def test_false(self):
        for d in self.dataF:
            self.assertNotEqual(d[1], urlify(d[0], len(d[0])))


if __name__ == '__main__':
    unittest.main()
