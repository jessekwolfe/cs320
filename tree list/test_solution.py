import unittest
from solution import findKey, deleteKey, addKey


class TestTreeListFunction(unittest.TestCase):
    def test_findKey_non(self):
        with self.assertRaises(ValueError) as err:
            findKey(None, [1, 2, 3])
        with self.assertRaises(ValueError) as err:
            findKey(-1, [1, 2, 3])
        with self.assertRaises(ValueError) as err:
            findKey(3, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
