import unittest
from cuckoo import CuckooSet


class Test_cuckoo(unittest.TestCase):

    def test_cuckoo(self):
        s = CuckooSet()
        self.assertEqual(len(s), 0)


if __name__ == "__main__":
    unittest.main()
