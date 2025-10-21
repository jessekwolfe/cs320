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

    def test_rank_shuffle(self):
        d = DirtyDeck()
        shuffle = DirtyDeck(hide=4)
        shuffle.shuffle()
        print(str(shuffle))
        self.assertTrue(d != shuffle)
        for i in range(0,4):
            self.assertTrue(shuffle.deck.pop().rank == 4)

    def test_rank_shuffle(self):
        d = DirtyDeck()
        shuffle = DirtyDeck(hide=4)
        shuffle.shuffle()
        print(str(shuffle))
        self.assertTrue(d != shuffle)
        for i in range(0, 4):
            self.assertTrue(shuffle.deck.pop().rank == 4)

    def test_rank_static_shuffle(self):
        d = DirtyDeck(hide=4, seed=0)
        d.shuffle()
        shuffle = DirtyDeck(hide=4, seed=0)
        shuffle.shuffle()
        print(str(shuffle))
        self.assertTrue(str(d) == str(shuffle))
        for i in range(0, 4):
            self.assertTrue(shuffle.deck.pop().rank == 4)


if __name__ == "__main__":
    unittest.main()
