import math


def radix_base(array, base):
    try:
        test_array(array)
        test_base(base)
    except ValueError:
        raise

    if len(array) == 1:
        return array

    return radix_sort(array, base)


def radix_sort(array, base):
    max_val = max(array)

    if max_val == 0 or max_val < base:
        max_digits = 1
    else:
        max_digits = math.floor(round(math.log(max_val, base), 2) + 1)

    for digit in range(0, max_digits):
        array = radix_sort_index(array, base, digit)

    return array


def radix_sort_index(array, base, index):
    radix_sort_tracker = [[] for i in range(base)]
    radix_sort_array = []

    for ele in array:
        val_at_index = (ele // base**index) % base
        if val_at_index < 0:
            val_at_index = 0

        radix_sort_tracker[val_at_index].append(ele)

    # collapse array
    for array in radix_sort_tracker:
        radix_sort_array.extend(array)

    return radix_sort_array


def test_array(array):
    if array is None or not array or len(array) <= 0:
        raise ValueError("invalid arguments")
    for element in array:
        if not isinstance(element, (int)) or element < 0:
            raise ValueError("invalid list element")


def test_base(base):
    if not base or not isinstance(base, (int)) or base < 2:
        raise ValueError("invalid arguments")
