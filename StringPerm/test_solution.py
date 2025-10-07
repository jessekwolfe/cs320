import unittest
from solution import countPermStr

import time


class StringPermTestFunction(unittest.TestCase):

    def test_Exception_1(self):
        haystack = "test"
        needle = ""
        with self.assertRaises(ValueError):
            countPermStr(haystack, needle)

    def test_Exception_2(self):
        haystack = "test"
        needle = None
        with self.assertRaises(ValueError):
            countPermStr(haystack, needle)

    def test_Exception_2_2(self):
        haystack = None
        needle = "1"
        with self.assertRaises(ValueError):
            countPermStr(haystack, needle)

    def test_Exception_3(self):
        haystack = "t"
        needle = "test"
        with self.assertRaises(ValueError):
            countPermStr(haystack, needle)

    def test_easy_function(self):
        string1 = "test"
        string2 = "t"
        start_time = time.perf_counter()
        self.assertEqual(countPermStr(string1, string2), 2)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (Easy): {elapsed_time:.6f} seconds")  # 0.000035 seconds

    def test_mid_function(self):
        start_time = time.perf_counter()
        self.assertEqual(countPermStr("cab ca b", "ab "), 2)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (Mid): {elapsed_time:.6f} seconds")  # 0.000019 seconds

    def test_mid_function2(self):
        start_time = time.perf_counter()
        self.assertEqual(countPermStr("cbacab", "ab"), 2)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(
            f"Execution time (Mid2): {elapsed_time:.6f} seconds"
        )  # 0.000015 seconds seconds seconds

    def test_mid_function_double_count(self):
        start_time = time.perf_counter()
        self.assertEqual(countPermStr("abcbaacccaabbaab", "aba"), 4)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(
            f"Execution time (Mid double count): {elapsed_time:.6f} seconds"
        )  # 0.000037 seconds

    def test_start_function_double_count(self):
        start_time = time.perf_counter()
        self.assertEqual(countPermStr("aabcbaacccaabbaab", "aba"), 5)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(
            f"Execution time (Mid start): {elapsed_time:.6f} seconds"
        )  # 0.000037 seconds

    def test_superOverlap_count(self):
        start_time = time.perf_counter()
        self.assertEqual(countPermStr("aaaaaabaaaaa", "aaa"), 7)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(
            f"Execution time (superOverlap): {elapsed_time:.6f} seconds"
        )  # 0.000037 seconds

    def test_superOverlap2_count(self):
        start_time = time.perf_counter()
        self.assertEqual(countPermStr("abcdabcdabcd", "abcd"), 9)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(
            f"Execution time (superOverlap2): {elapsed_time:.6f} seconds"
        )  # 0.000037 seconds

    def test_superOverlap2_count(self):
        start_time = time.perf_counter()
        self.assertEqual(countPermStr("abcdabcdabcd", "abcd"), 9)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(
            f"Execution time (superOverlap2): {elapsed_time:.6f} seconds"
        )  # 0.000037 seconds

    def test_superlong_count(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(
                "a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit",
                "lorem ",
            ),
            24,
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(
            f"Execution time (superOverlap2): {elapsed_time:.6f} seconds"
        )  # 0.000037 seconds

    def test_supersuperlong_count(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(
                "a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit a lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet lorem lorem magna lorem lorem ipsum dolor sit amet consectetur lorem adipiscing elit",
                "lorem ",
            ),
            480,
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(
            f"Execution time (supersuperlong): {elapsed_time:.6f} seconds"
        )  # 0.000037 seconds

    def test_start_function_double_count(self):
        start_time = time.perf_counter()
        self.assertEqual(countPermStr("a abcba acccaabbaab ", "aba "), 3)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(
            f"Execution time (Mid start end blank): {elapsed_time:.6f} seconds"
        )  # 0.000037 seconds

    def test_hamlet_1(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(b"SCENE II. A room in the castle.", b"room in the castle"), 1
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (hamlet_1): {elapsed_time:.6f} seconds")

    def test_hamlet_2(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(b"SCENE I. A room in the castle.", b"room in the castle"), 1
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (hamlet_2): {elapsed_time:.6f} seconds")

    def test_hamlet_3(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(b"SCENE III. A room in the castle.", b"room in the castle"), 1
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (hamlet_3): {elapsed_time:.6f} seconds")

    def test_hamlet_4(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(b"SCENE I. A room in the castle.", b"room in the castle"), 1
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (hamlet_4): {elapsed_time:.6f} seconds")

    def test_hamlet_5(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(
                b"SCENE II. Another room in the castle.", b"room in the castle"
            ),
            1,
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (hamlet_5): {elapsed_time:.6f} seconds")

    def test_hamlet_6(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(
                b"SCENE III. Another room in the castle.", b"room in the castle"
            ),
            1,
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (hamlet_6): {elapsed_time:.6f} seconds")

    def test_hamlet_7(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(
                b"SCENE V. Elsinore. A room in the castle.", b"room in the castle"
            ),
            1,
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (hamlet_7): {elapsed_time:.6f} seconds")

    def test_hamlet_8(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(
                b"SCENE VI. Another room in the castle.", b"room in the castle"
            ),
            1,
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (hamlet_8): {elapsed_time:.6f} seconds")

    def test_hamlet_9(self):
        start_time = time.perf_counter()
        self.assertEqual(
            countPermStr(
                b"SCENE VII. Another room in the castle.", b"room in the castle"
            ),
            1,
        )
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time (hamlet_9): {elapsed_time:.6f} seconds")

    def test_hamlet_search(self):
        start_time = time.perf_counter()
        count = 0
        str4 = b"room in the castle"
        with open("./StringPerm/hamlet.txt") as hamlet:
            for line in hamlet:
                try:
                    count += countPermStr(line.encode(), str4)
                except ValueError:
                    continue
        end_time = time.perf_counter()

        self.assertEqual(count, 9)

        elapsed_time = end_time - start_time
        print(
            f"Execution time (Hamlet): {elapsed_time:.6f} seconds"
        )  # 0.000037 seconds


if __name__ == "__main__":
    unittest.main()
