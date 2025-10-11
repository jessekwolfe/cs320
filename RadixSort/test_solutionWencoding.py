import unittest
from solutionWencoding import (
    radix_base,
    to_base_x,
    from_base_x,
    encode_list_by_base,
    decode_list_by_base,
    encoded_radix_sort,
    radix_sort_index,
    radix_sort,
)

import time


class TestRadixSortFunction(unittest.TestCase):
    def test_rad_sort_index(self):
        self.assertEqual(
            radix_sort_index([25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1], 10, 0),
            [21, 11, 1, 22, 12, 2, 13, 3, 25, 27, 29],
        )

    def test_rad_sort(self):
        self.assertEqual(
            radix_sort(
                [25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1],
                10,
            ),
            [1, 2, 3, 11, 12, 13, 21, 22, 25, 27, 29],
        )

    def test_ideal(self):
        self.assertEqual(
            radix_base([25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1], 10),
            [1, 2, 3, 11, 12, 13, 21, 22, 25, 27, 29],
        )

    def test_zero(self):
        self.assertEqual(
            radix_base([0, 0, 0, 0, 0, 0], 10),
            [0, 0, 0, 0, 0, 0],
        )

    def test_ideal(self):
        self.assertEqual(
            radix_base([0, 0, 0, 0, 0, 0], 10),
            [0, 0, 0, 0, 0, 0],
        )

    def test_ideal_base_4(self):
        self.assertEqual(
            radix_base([25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1], 4),
            [1, 2, 3, 11, 12, 13, 21, 22, 25, 27, 29],
        )

    def test_ideal_base_16(self):
        self.assertEqual(
            radix_base([25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1], 16),
            [1, 2, 3, 11, 12, 13, 21, 22, 25, 27, 29],
        )

    def test_ideal_base_4_encoded(self):
        self.assertEqual(
            radix_base([25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1], 4, False),
            [1, 2, 3, 11, 12, 13, 21, 22, 25, 27, 29],
        )

    def test_ideal_base_16(self):
        self.assertEqual(
            radix_base([25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1], 16, False),
            [1, 2, 3, 11, 12, 13, 21, 22, 25, 27, 29],
        )

    def test_ideal_base_2(self):
        self.assertEqual(
            radix_base([25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1], 2, False),
            [1, 2, 3, 11, 12, 13, 21, 22, 25, 27, 29],
        )

    def test_empty_array_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base([], 2)

    # def test_zero_exception(self):
    #     with self.assertRaises(ValueError) as err:
    #         radix_base([0, 0, 0, 0], 2)

    def test_bad_type(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, 2, "bad string", 4], 2)

    def test_bad_base(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, 2, 3, 4], 1)

    def test_bad_base_string(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, 2, 3, 4], "test")

    def test_bad_base_string(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, -2, 3, 4], 4)

    def test_none_array_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base(None, 2)

    def test_none_content_array_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base([None], 2)

    def test_base_too_low_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, 2], 1)

    def test_base_none_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, 2], None)

    def test_nonManthmatical_exception(self):
        with self.assertRaises(ValueError) as err:
            radix_base([1, "hello", 3], 2)

    def test_to_base_4_13(self):
        self.assertEqual(to_base_x(13, 4, 3), [0, 3, 1])

    def test_to_base_4_25(self):
        self.assertEqual(to_base_x(25, 4, 3), [1, 2, 1])

    def test_from_base_4_13(self):
        self.assertEqual(from_base_x([0, 3, 1], 4), 13)

    def test_from_base_4_25(self):
        self.assertEqual(from_base_x([1, 2, 1], 4), 25)

    def test_encode_list_by_base(self):
        self.assertEqual(
            encode_list_by_base([25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1], 4),
            [
                [1, 2, 1],
                [1, 2, 3],
                [1, 3, 1],
                [1, 1, 2],
                [1, 1, 1],
                [0, 2, 3],
                [0, 3, 0],
                [0, 3, 1],
                [0, 0, 3],
                [0, 0, 2],
                [0, 0, 1],
            ],
        )

    def test_decode_list_by_base(self):
        self.assertEqual(
            decode_list_by_base(
                [
                    [1, 2, 1],
                    [1, 2, 3],
                    [1, 3, 1],
                    [1, 1, 2],
                    [1, 1, 1],
                    [0, 2, 3],
                    [0, 3, 0],
                    [0, 3, 1],
                    [0, 0, 3],
                    [0, 0, 2],
                    [0, 0, 1],
                ],
                4,
            ),
            [25, 27, 29, 22, 21, 11, 12, 13, 3, 2, 1],
        )

    def test_encoded_radix_sort(self):
        self.assertEqual(
            encoded_radix_sort(
                [
                    [1, 2, 1],
                    [1, 2, 3],
                    [1, 3, 1],
                    [1, 1, 2],
                    [1, 1, 1],
                    [0, 2, 3],
                    [0, 3, 0],
                    [0, 3, 1],
                    [0, 0, 3],
                    [0, 0, 2],
                    [0, 0, 1],
                ],
                4,
            ),
            [
                [0, 0, 1],
                [0, 0, 2],
                [0, 0, 3],
                [0, 2, 3],
                [0, 3, 0],
                [0, 3, 1],
                [1, 1, 1],
                [1, 1, 2],
                [1, 2, 1],
                [1, 2, 3],
                [1, 3, 1],
            ],
        )

    def test_to_base_4_0(self):
        self.assertEqual(to_base_x(0, 4, 6), [0, 0, 0, 0, 0, 0])

    def test_from_base_4_0(self):
        self.assertEqual(from_base_x([0, 0, 0, 0, 0, 0], 4), 0)

    def test_to_base_4_13(self):
        self.assertEqual(to_base_x(1024, 4, 6), [1, 0, 0, 0, 0, 0])

    def test_from_base_4_25(self):
        self.assertEqual(from_base_x([1, 0, 0, 0, 0, 0], 4), 1024)

    def test_to_base_10_1000(self):
        self.assertEqual(to_base_x(1000, 10, 4), [1, 0, 0, 0])

    def test_from_base_10_1000(self):
        self.assertEqual(from_base_x([1, 0, 0, 0], 10), 1000)

    def test_edge_case_base_multiples(self):
        self.assertEqual(
            radix_base([16, 256, 64, 1024, 4], 4),
            [4, 16, 64, 256, 1024],
        )

    def test_edge_case_base_multiples_2(self):
        self.assertEqual(
            radix_base([1024, 32, 64, 128, 256, 8, 512, 4, 2, 16], 2, False),
            [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        )

    def test_edge_case_single_element(self):
        self.assertEqual(radix_base([4], 4), [4], False)

    def test_edge_case_single_element_0(self):
        self.assertEqual(radix_base([0], 4), [0], False)

    def test_edge_case_zeros(self):
        self.assertEqual(radix_base([0, 0, 0, 0, 0], 4), [0, 0, 0, 0, 0], False)

    # GPT tests
    def test_invalid_arguments_none(self):
        with self.assertRaises(ValueError) as context:
            radix_base(None, 2)
        self.assertEqual(str(context.exception), "invalid arguments")

    def test_invalid_arguments_empty_list(self):
        with self.assertRaises(ValueError) as context:
            radix_base([], 2)
        self.assertEqual(str(context.exception), "invalid arguments")

    def test_invalid_arguments_base_less_than_2(self):
        with self.assertRaises(ValueError) as context:
            radix_base([1, 2, 3], 1)
        self.assertEqual(str(context.exception), "invalid arguments")

    def test_invalid_list_element_negative(self):
        with self.assertRaises(ValueError) as context:
            radix_base([1, -2, 3], 2)
        self.assertEqual(str(context.exception), "invalid list element")

    def test_invalid_list_element_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            radix_base([1, "a", 3], 2)
        self.assertEqual(str(context.exception), "invalid list element")

    def test_invalid_list_element_object(self):
        with self.assertRaises(ValueError) as context:
            radix_base([1, object(), 3], 2)
        self.assertEqual(str(context.exception), "invalid list element")

    def test_valid_input_small(self):
        # This assumes radix_base correctly sorts numbers in base 2
        # You can adjust expected result depending on your implementation
        result = radix_base([3, 1, 2], 2, False)
        self.assertEqual(result, [1, 2, 3])

    def test_valid_input_large_base(self):
        result = radix_base([25, 27, 29, 22], 10)
        self.assertEqual(result, [22, 25, 27, 29])

    def test_single_element_list(self):
        result = radix_base([42], 10)
        self.assertEqual(result, [42])

    def test_two_elements_sorted(self):
        result = radix_base([1, 0], 2)
        self.assertEqual(result, [0, 1])

    def test_two_elements_unsorted(self):
        result = radix_base([2, 1], 3)
        self.assertEqual(result, [1, 2])

    def test_all_same_elements(self):
        result = radix_base([7, 7, 7, 7], 10)
        self.assertEqual(result, [7, 7, 7, 7])

    def test_large_numbers(self):
        result = radix_base([1000, 1_000_000, 100, 10], 10)
        self.assertEqual(result, [10, 100, 1000, 1_000_000])

    def test_many_digits_different_lengths(self):
        result = radix_base([5, 123, 45, 9, 1000, 67], 10)
        self.assertEqual(result, [5, 9, 45, 67, 123, 1000])

    def test_already_sorted(self):
        result = radix_base([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        result = radix_base([9, 8, 7, 6, 5, 4, 3, 2, 1], 10)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_large_base(self):
        # Should work fine even if base > max value
        result = radix_base([5, 1, 9, 3], 20)
        self.assertEqual(result, [1, 3, 5, 9])

    def test_base_equal_to_max_digit(self):
        # For base = 10, normal decimal sorting
        result = radix_base([19, 1, 3, 12], 10)
        self.assertEqual(result, [1, 3, 12, 19])

    def test_numbers_with_zeroes(self):
        result = radix_base([10, 100, 1000, 0, 5], 10)
        self.assertEqual(result, [0, 5, 10, 100, 1000])

    def test_stability_of_sort(self):
        # If radix sort is stable, equal keys preserve order of appearance
        values = [(3, "a"), (1, "b"), (3, "c"), (2, "d")]
        # extract first element for sorting
        sorted_values = radix_base([x[0] for x in values], 10)
        self.assertEqual(sorted_values, [1, 2, 3, 3])

    def test_very_large_list(self):
        import random

        nums = [random.randint(0, 1000) for _ in range(5000)]
        sorted_nums = sorted(nums)
        result = radix_base(nums, 10)
        self.assertEqual(result, sorted_nums)

    def test_values_containing_zero(self):
        result = radix_base([0, 5, 2, 9, 1], 2, False)
        self.assertEqual(result, [0, 1, 2, 5, 9])

    def test_powers_of_two(self):
        result = radix_base([1, 2, 4, 8, 16, 32, 64, 128], 10)
        self.assertEqual(result, [1, 2, 4, 8, 16, 32, 64, 128])

    def test_duplicate_large_numbers(self):
        result = radix_base([500, 1000, 500, 250, 1000], 10)
        self.assertEqual(result, [250, 500, 500, 1000, 1000])

    def test_time_large_array(self):
        import random

        nums = [random.randint(0, 1000) for _ in range(5000)]
        sorted_nums = sorted(nums)
        start_time = time.perf_counter()
        result = radix_base(nums, 10)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        self.assertEqual(result, sorted_nums)

        print(
            f"Execution time (large_array): {elapsed_time:.6f} seconds"
        )  # 0.000019 seconds

    def test_time_encode_large_array(self):
        import random

        nums = [random.randint(0, 1000) for _ in range(5000)]
        total_start_time = time.perf_counter()
        start_time = time.perf_counter()
        result = encode_list_by_base(nums, 10)
        end_time = time.perf_counter()
        elapsed_time_encode = end_time - start_time

        start_time = time.perf_counter()
        result = encoded_radix_sort(result, 10)
        end_time = time.perf_counter()
        elapsed_time_sort = end_time - start_time

        start_time = time.perf_counter()
        result = decode_list_by_base(result, 10)
        end_time = time.perf_counter()
        total_end_time = time.perf_counter()
        elapsed_time_decode = end_time - start_time
        total_elapsed_time = total_end_time - total_start_time

        print(f"Execution time (encode): {elapsed_time_encode:.6f} seconds")
        print(f"Execution time (sort): {elapsed_time_sort:.6f} seconds")
        print(f"Execution time (decode): {elapsed_time_decode:.6f} seconds")
        print(f"Execution time (total): {total_elapsed_time:.6f} seconds")

    def test_time_encoded_large_array(self):
        import random

        nums = [random.randint(0, 1000) for _ in range(5000)]

        start_time = time.perf_counter()
        result = radix_base(nums, 10, False)
        end_time = time.perf_counter()
        elapsed_time_sort = end_time - start_time

        print(f"Execution time (Large Encoded): {elapsed_time_sort:.6f} seconds")


if __name__ == "__main__":
    unittest.main()
