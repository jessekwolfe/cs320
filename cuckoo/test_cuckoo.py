import unittest
from cuckoo import CuckooSet


class Test_cuckoo(unittest.TestCase):

    def setUp(self):
        # small table to force collisions easily
        self.s = 8
        self.cs = CuckooSet(s=self.s)

    def test_cuckoo(self):
        s = CuckooSet()
        self.assertEqual(len(s), 0)

    def test_add(self):
        s = CuckooSet()
        s.add(5)
        self.assertEqual(len(s), 1)

    def test_basic_insertion(self):
        """Basic add() should store elements without error."""
        self.cs.add("apple")
        self.assertIn("apple", list(self.cs))
        self.assertEqual(len(self.cs), 1)

    def test_duplicate_insertion(self):
        """Adding a duplicate should not increase set size."""
        self.cs.add("apple")
        self.cs.add("apple")
        self.assertEqual(len(self.cs), 1)

    def test_collision_and_swap(self):
        """When collisions occur, cuckoo swapping should still succeed."""
        # Artificially control hash collisions
        # Use small table to trigger collisions quickly
        data = ["A", "B", "C", "D"]
        for item in data:
            self.cs.add(item)
        # All inserted items should be in the table
        for item in data:
            self.assertIn(item, list(self.cs))

    def test_resize(self):
        """If too many swaps happen, table should resize."""
        old_size = self.cs._size_
        # Force resize by filling table
        self.cs._resize_()
        self.assertGreater(self.cs._size_, old_size)

    def test_max_swaps_trigger_resize(self):
        """If too many swaps happen, table should resize."""
        old_size = self.cs._size_ * 2
        # Force resize by filling table
        for i in range(old_size):
            self.cs.add(f"item{i}")
        # Add another to exceed MAXSWAPS and trigger resize
        self.cs.add("overflow")
        self.assertGreater(self.cs._size_, old_size)

    def test_all_items_accessible_after_resize(self):
        """After resize, all inserted items remain accessible."""
        items = [f"item{i}" for i in range(50)]
        for i in items:
            self.cs.add(i)
        for i in items:
            self.assertIn(i, list(self.cs))

    def test_str_output(self):
        """__str__ should include inserted items."""
        self.cs.add("apple")
        self.cs.add("banana")
        s = str(self.cs)
        self.assertIn("apple", s)
        self.assertIn("banana", s)

    def test_iteration(self):
        """__iter__ should yield all members."""
        items = {"x", "y", "z"}
        for i in items:
            self.cs.add(i)
        self.assertEqual(set(self.cs), items)

    def test_contains(self):
        old_size = self.cs._size_
        # Force resize by filling table
        for i in range(old_size):
            self.cs.add(f"item{i}")
        # Add another to exceed MAXSWAPS and trigger resize
        self.assertTrue(self.cs.__contains__("item1"))

    def test_remove(self):
        old_size = self.cs._size_
        # Force resize by filling table
        for i in range(old_size):
            self.cs.add(f"item{i}")
        # Add another to exceed MAXSWAPS and trigger resize
        self.assertTrue(self.cs.__contains__("item1"))
        self.cs.remove("item1")
        self.assertFalse(self.cs.__contains__("item1"))

    def test_remove_exception(self):
        old_size = self.cs._size_
        # Force resize by filling table
        for i in range(old_size):
            self.cs.add(f"item{i}")
        # Add another to exceed MAXSWAPS and trigger resize
        with self.assertRaises(ValueError) as context:
            self.cs.remove("Non-Existant")
        self.assertEqual(str(context.exception), "key may not be None")


if __name__ == "__main__":
    unittest.main()
