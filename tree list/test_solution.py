import unittest
from solution import findKey, deleteKey, addKey


class TestTreeListFunction(unittest.TestCase):

    t1 = [4, 2, 6, 1, 3, 5, 7]
    t2 = [4, 2, 6, 1, None, 5, 7]
    t3 = [1, None, 2, None, None, None, 4]
    t4 = [4, 2, None, 1]

    def test_findKey_non(self):
        with self.assertRaises(ValueError) as err:
            findKey(None, [1, 2, 3])
        with self.assertRaises(LookupError) as err:
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

        self.assertEqual(
            addKey(-7, [1, None, 2, None, None, None, 4]),
            [1, -7, 2, None, None, None, 4],
        )

    def test_except_addKey(self):
        input = [4, 2, 6, 1, 3, 5, 7]
        with self.assertRaises(ValueError) as err:
            addKey(None, [1, 2, 3])

    def test_except_deleteKey(self):
        input = [4, 2, 6, 1, 3, 5, 7]
        with self.assertRaises(ValueError) as err:
            deleteKey(None, [1, 2, 3])
        with self.assertRaises(LookupError) as err:
            deleteKey(5, [1, 2, 3])
        with self.assertRaises(LookupError) as err:
            deleteKey(5, [])

    def test_valid_deleteKey(self):
        input2 = [4, 2, 6, 1, 3, 5, 7]
        self.assertEqual(
            deleteKey(7, input2),
            [4, 2, 6, 1, 3, 5],
        )
        self.assertEqual(deleteKey(7, [7]), [])
        self.assertEqual(deleteKey(20, [20, 10, 30]), [30, 10])
        self.assertEqual(
            deleteKey(50, [50, 30, 70, 20, 40, 60, 80]), [60, 30, 70, 20, 40, None, 80]
        )
        self.assertEqual(
            deleteKey(30, [50, 30, 70, 20, 40, 60, 80]), [50, 40, 70, 20, None, 60, 80]
        )
        self.assertEqual(
            deleteKey(70, [50, 30, 70, 20, 40, 60, 80]), [50, 30, 80, 20, 40, 60]
        )
        # self.assertEqual(deleteKey(1, [1, None, 2, None, None, None, 4]), [2, None, 4])
        # self.assertEqual(deleteKey(2, [1, None, 2, None, None, None, 4]), [1, None, 4])


if __name__ == "__main__":
    unittest.main()
