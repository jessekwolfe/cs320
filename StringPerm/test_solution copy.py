import unittest
from brute import find_pat

import time


class StringPermBruteTestFunction(unittest.TestCase):

    def test_easy_function(self):
        haystack = "test"
        needle = "t"
        start_time = time.perf_counter()
        self.assertEqual(find_pat(haystack, needle), 2)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (Easy): {elapsed_time:.6f} seconds")  # 0.000052 seconds

    def test_mid_function(self):
        start_time = time.perf_counter()
        self.assertEqual(find_pat("cabcab", "ab"), 2)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (Mid): {elapsed_time:.6f} seconds")  # 0.000019 seconds


if __name__ == "__main__":
    unittest.main()
