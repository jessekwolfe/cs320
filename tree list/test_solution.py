import unittest
from solution import findKey, deleteKey, addKey


class TestTreeListFunction(unittest.TestCase):
    def test_findKey_non(self):
        with self.assertRaises(ValueError) as err:
            findKey(None, [1, 2, 3])
        with self.assertRaises(ValueError) as err:
            findKey(2, [])
        with self.assertRaises(LookupError) as err:
            findKey(5, [1, 2, 3])

    def test_valid_findKey(self):
        input = [4, 2, 6, 1, 3, 5, 7]
        self.assertEqual(findKey(4, input), 0)
        self.assertEqual(findKey(1, input), 3)
        self.assertEqual(findKey(7, input), 6)

    def test_valid_addKey(self):
        input2 = [4, 2, 6, None, 3, 5, 7]
        self.assertEqual(
            addKey(9, input2),
            [4, 2, 6, None, 3, 5, 7, None, None, None, None, None, None, None, 9],
        )
        self.assertEqual(addKey(1, input2), [4, 2, 6, 1, 3, 5, 7])
        self.assertEqual(input2, [4, 2, 6, None, 3, 5, 7])
        self.assertEqual(
            addKey(2000, input2),
            [4, 2, 6, None, 3, 5, 7, None, None, None, None, None, None, None, 2000],
        )
        self.assertEqual(
            addKey(2, input2),
            input2,
        )
        self.assertEqual(
            addKey(2, []),
            [2],
        )

    def test_except_addKey(self):
        input = [4, 2, 6, 1, 3, 5, 7]
        with self.assertRaises(ValueError) as err:
            addKey(None, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
