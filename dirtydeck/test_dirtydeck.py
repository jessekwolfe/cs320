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
        self.assertTrue(d != shuffle)

    def test_rank_shuffle(self):
        print("test_rank_shuffle:")
        d = DirtyDeck()
        shuffle = DirtyDeck(hide=4)
        shuffle.shuffle()
        print(str(shuffle))
        self.assertTrue(d != shuffle)
        for i in range(0,4):
            self.assertTrue(shuffle.deck.pop().rank == 4)

    def test_rank_static_shuffle(self):
        print("test_rank_static_shuffle:")
        d = DirtyDeck(hide=4, seed=0)
        d.shuffle()
        shuffle = DirtyDeck(hide=4, seed=0)
        shuffle.shuffle()
        print(str(shuffle))
        self.assertTrue(str(d) == str(shuffle))
        for i in range(0, 4):
            self.assertTrue(shuffle.deck.pop().rank == 4)

    def test_pop(self):
        d = DirtyDeck()
        deltCard = d.deal()
        self.assertTrue(deltCard.rank == 1)

    def test_pop_exception(self):
        d = DirtyDeck()
        with self.assertRaises(ResourceWarning) as context:
            for _ in range(0,40):
                d.deal()
        self.assertEqual(str(context.exception), "low deck")

    def test_shuffle_pop(self):
        shuffle = DirtyDeck()
        shuffle.shuffle()
        self.assertTrue(len(shuffle) == 52)

    def test_rank_shuffle_class1(self):
        for rank in [10, "Jack", "Queen", "King", "Ace", "Joker", 2]:
            _ = DirtyDeck(hide=rank)
            self.assertTrue(isinstance(_, DirtyDeck))

    def test_invalidRank_class2(self):
        print("test_rank_shuffle:")
        with self.assertRaises(ValueError) as context:
            _ = DirtyDeck(hide=15)
        self.assertEqual(str(context.exception), "15 is not a card rank")

if __name__ == "__main__":
    unittest.main()