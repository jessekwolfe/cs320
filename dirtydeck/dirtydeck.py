from playingcard import PlayingCard, CardSuit, _valid_rank_, _convert_to_rank
from collections.abc import Container
import unittest
import random


_full_deck_ = [PlayingCard(s, r) for s in CardSuit for r in range(1, 14)]


class DirtyDeck(Container):
    DECK_SIZE = 52
    shuffle_end = 0

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

        if self.seed is not None:
            random.seed(self.seed)
        for i in range(len(self.deck) - 1, -1, -1):
            self.fisheryates(i)

    def fisheryates(self, i):
        deck = self.deck
        random_card = random.randint(0, len(deck) - 1 - self.shuffle_end)

        if deck[i].rank == self.hidden:
            shuffleStop = self.DECK_SIZE - 1 - self.shuffle_end
            self.index_card_swap(i, shuffleStop)
            self.shuffle_end += 1

        if deck[random_card].rank == self.hidden:
            shuffleStop = self.DECK_SIZE - 1 - self.shuffle_end
            self.index_card_swap(random_card, shuffleStop)
            self.shuffle_end += 1

        self.index_card_swap(i, random_card)

    def index_card_swap(self, index1, index2):
        self.deck[index1], self.deck[index2] = self.deck[index2], self.deck[index1]

    def deal(self):
        if len(self.deck) / 52 <= 0.25:
            raise ResourceWarning("low deck")
        return self.deck.pop(0)


def checkHide(hide):
    if hide is None:
        return
    if 0 <= hide <= 14:
        raise ValueError("invalid hidden rank")


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
