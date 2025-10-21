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
        end_of_deck = []
        if self.seed is not None:
            random.seed(self.seed)
        while len(base_deck) > 0:
            random_card = random.randint(0, len(base_deck)-1)
            card = base_deck.pop(random_card)
            if card.rank == self.hidden:
                end_of_deck.append(card)
            else:
                shuffled_deck.append(card)

        self.deck = shuffled_deck + end_of_deck


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
