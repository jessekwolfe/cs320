from collections.abc import Collection
from math import e, modf, floor, sqrt
from itertools import filterfalse, chain
from copy import copy
import unittest


# DO NOT CHANGE ANY CODE BETWEEN LINE X AND LINE Y
# ******* THIS IS LINE X ******************

GOLDEN = (1.0 + 5.0 * 0.5) / 2.0


def swap(a, b):
    return b, a


# ***************************************************
# why do we inherit from Collection rather than Set?
# because Set requires too many methods to be defined


class CuckooSet(Collection):

    # *** course helper routines *******
    def _hash2_(self, obj, table_size):
        try:
            h = hash(obj)  # may raise exception
        except Exception:
            raise TypeError("unhashable key")

        h %= table_size

        f1, _ = modf(h * e)
        f2, _ = modf(h * GOLDEN)
        h1 = floor(table_size * f1)
        h2 = floor(table_size * f2)
        if h1 == h2:
            h2 = (h2 + 7) % table_size
        return h1, h2

    def _members_(self, tab):  # returns iterator
        return filterfalse((lambda x: x is None), tab)

    def _allmembers_(self):
        return chain(self._members_(self.htab1), self._members_(self.htab2))

    # ** course methods ****

    def __init__(self, iter=[], *, s=128):
        if s < 4:
            raise ValueError("set size too small")
        self._size_ = s
        self._MAXSWAPS_ = floor(s * 0.6)
        self.htab1 = [None] * s
        self.htab2 = [None] * s
        for i in iter:
            self.add(i)

    def __len__(self):
        count1 = len(list(self._members_(self.htab1)))
        count2 = len(list(self._members_(self.htab2)))
        return count1 + count2

    def _resize_(self):
        oldself = copy(self)
        self.__init__(oldself, s=oldself._size_ * 2)

    def __str__(self):
        fstr = ""
        for v in self._allmembers_():
            if len(fstr):
                fstr += ", "
            fstr += str(v)
        return fstr

    def __iter__(self):
        return self._allmembers_()
# ******* THIS IS LINE Y ******************

    def __contains__(self, x):
        self.check_valid_value(x)
        locations = self._hash2_(x, self._size_)
        if self.htab1[locations[0]] == x or self.htab2[locations[1]] == x:
            return True
        return False

    def add(self, x):
        self.check_valid_value(x)
        if self.__contains__(x):
            return

        swapCount = 0
        currentTable = self.htab1
        currentObj = x
        currentHash = self._hash2_(currentObj, self._size_)

        if currentTable[currentHash[0]] is None:
            currentTable[currentHash[0]] = x
        else:
            while swapCount < self._MAXSWAPS_:
                currentObj = self.attemptToAddToTable(currentTable, currentObj)

                if currentObj is None:  # Set to none if added without swap
                    break
                else:
                    currentTable = self.swapCurrentTable(currentTable)
                    swapCount += 1

            if swapCount >= self._MAXSWAPS_:
                self._resize_()
                self.add(currentObj)

    def swapCurrentTable(self, currTable):
        if currTable is self.htab1:
            return self.htab2
        else:
            return self.htab1

    def attemptToAddToTable(self, currTable, val):
        hash_index = 0
        if currTable is not self.htab1:
            hash_index = 1

        hash_val = self._hash2_(val, self._size_)[hash_index]

        if currTable[hash_val] is None:
            currTable[hash_val] = val
            return None
        else:
            temp = currTable[hash_val]
            currTable[hash_val] = val
            return temp

    def remove(self, x):
        if self.__contains__(x) is not True:
            raise ValueError("key may not be None")
        self.discard(x)

    def discard(self, x):
        self.check_valid_value(x)
        locations = self._hash2_(x, self._size_)
        if self.htab1[locations[0]] == x:
            self.htab1[locations[0]] = None
        if self.htab2[locations[1]] == x:
            self.htab2[locations[1]] = None

    def check_valid_value(self, x):
        if x is None:
            raise ValueError("key may not be None")
