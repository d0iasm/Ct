import unittest


def string_compression(string):
    compressed = []
    counter = 1

    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            compressed.append(string[i - 1])
            compressed.append(str(counter))
            counter = 0
        counter += 1

    compressed.append(string[-1])
    compressed.append(str(counter))

    return min(string, ''.join(compressed), key=len)


class Test(unittest.TestCase):
    dataT = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]
    dataF = [
        ('aabcccccaaa', 'a2bc5a3'),
        ('abcdef', 'a1b1c1d1e1f1')
    ]

    def test_true(self):
        for [test_string, expected] in self.dataT:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

    def test_false(self):
        for [test_string, expected] in self.dataF:
            actual = string_compression(test_string)
            self.assertNotEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
