from playingcard import PlayingCard, CardSuit, _valid_rank_, _convert_to_rank
from collections.abc import Container
import unittest
import random


_full_deck_ = [PlayingCard(s, r) for s in CardSuit for r in range(1, 14)]


class DirtyDeck(Container):
    deck_size = 52
    suit_count = 4

    def __init__(self, *, hide=None, seed=None):
        self.deck = _full_deck_.copy()
        self.hidden = None
        self.seed = None
        if hide is not None:
            if not _valid_rank_(hide):
                raise ValueError(f"{hide} is not a card rank")
            self.hidden = _convert_to_rank(hide)
        if seed is not None:
            if not isinstance(seed, int):
                raise ValueError(f"{seed} is not int")
            self.seed = seed

    def __str__(self):
        retstr = ""
        for c in self.deck:
            retstr += f"{str(c)} "
        return retstr

    def __contains__(self, c):
        return c in self.deck

    def __len__(self):
        return len(self.deck)

    def __iter__(self):
        return iter(self.deck)

    def shuffle(self):
        base_deck = self.deck
        shuffled_deck = []
        end_of_shuffle = self.deck_size -1
        shuffle_end = 0
        if self.seed is not None:
            random.seed(self.seed)
        for i in range(len(base_deck)-1, -1, -1):
            random_card = random.randint(0, len(base_deck) - 1 - shuffle_end)

            if base_deck[i].rank == self.hidden:
                self.index_card_swap( i, end_of_shuffle)
                end_of_shuffle -= 1
                shuffle_end += 1
            if base_deck[random_card].rank == self.hidden:
                self.index_card_swap(random_card, end_of_shuffle)
                end_of_shuffle -= 1
                shuffle_end += 1

            self.index_card_swap(i, random_card)

    def index_card_swap(self, index1, index2):
        self.deck[index1], self.deck[index2] = self.deck[index2], self.deck[index1]


if __name__ == "__main__":

    d = DirtyDeck()  # rework as unittests
    print(d)
    print(f"len={len(d)}")

    for rank in [10, "Jack", "Queen", "King", "Ace", "Joker", 2]:
        _ = DirtyDeck(hide=rank)

    try:
        _ = DirtyDeck(hide=15)
    except Exception:
        print("invalid hide fails")
