import unittest
from dirtydeck import DirtyDeck


class Test_dirtydeck(unittest.TestCase):
    def test_cuckoo(self):
        d = DirtyDeck()
        self.assertTrue(isinstance(d, DirtyDeck))


if __name__ == "__main__":
    unittest.main()
