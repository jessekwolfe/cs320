import unittest
from dirtydeck import DirtyDeck


class Test_dirtydeck(unittest.TestCase):
    def test_cuckoo(self):
        d = DirtyDeck()
        self.assertTrue(isinstance(d, DirtyDeck))

    def test_shuffle(self):
        d = DirtyDeck()
        shuffle = DirtyDeck()
        shuffle.shuffle()
        print(str(shuffle))
        self.assertTrue(d != shuffle)


if __name__ == "__main__":
    unittest.main()
