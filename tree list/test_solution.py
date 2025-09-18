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


if __name__ == "__main__":
    unittest.main()
