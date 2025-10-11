import math


def radix_base(array, base, preEncoded=True):
    try:
        test_array(array)
        test_base(base)
    except ValueError:
        raise

    if len(array) == 1:
        return array

    if preEncoded:
        return radix_sort(array, base)
    else:
        encoded_array = encode_list_by_base(array, base)

        sorted_array = encoded_radix_sort(encoded_array, base)

        return decode_list_by_base(sorted_array, base)


def radix_sort(array, base):
    max_val = max(array)

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
        val_at_index = math.floor(ele / (base**index)) % base
        if val_at_index < 0:
            val_at_index = 0

        radix_sort_tracker[val_at_index].append(ele)

    # collapse array
    for array in radix_sort_tracker:
        radix_sort_array = radix_sort_array + array

    return radix_sort_array


def test_array(array):
    if array is None or not array or len(array) <= 0:
        raise ValueError("invalid arguments")
    for element in array:
        try:
            if element < 0 or not isinstance(element, (int)):
                raise ValueError
            if element != 0:
                (100 / element) + (100 % element)
        except (ValueError, ZeroDivisionError, TypeError):
            raise ValueError("invalid list element")


def test_base(base):
    if not base or not isinstance(base, (int)) or base < 2:
        raise ValueError("invalid arguments")


# -------------------------------------------------------
# Additional code that does encoding from base 10 to a base if the array isn't already.
# This is run when the optional third param is False.
# -------------------------------------------------------


def encode_list_by_base(array, base):
    encoded_array = [[] for i in range(len(array))]

    max_val = max(array)
    if max_val == 0 or max_val < base:
        max_digits = 1
    else:
        max_digits = math.floor(round(math.log(max_val, base), 2) + 1)

    for index, ele in enumerate(array):
        encoded_array[index] = to_base_x(ele, base, max_digits)

    return encoded_array


def to_base_x(number, base, digits):
    base_encoded = [0] * digits
    count = digits - 1

    if number == 0:
        return [0] * digits

    while number > 0:
        number, base_encoded[count] = divmod(number, base)
        count -= 1

    return base_encoded


def decode_list_by_base(array, base):
    decoded = [0] * len(array)

    for index, ele in enumerate(array):
        decoded[index] = from_base_x(ele, base)

    return decoded


def from_base_x(encoded, base):
    number = 0

    for index, ele in enumerate(encoded):
        number += ele * math.pow(base, len(encoded) - index - 1)

    return math.floor(number)


def encoded_radix_sort(array, base):
    digits = len(array[0])

    for digit in range(digits, 0, -1):
        array = encoded_radix_sort_index(array, base, digit)

    return array


def encoded_radix_sort_index(array, base, index):
    # Was having a hard time with list in a list creation when
    # adding a list to the inner. Had to look it up here:
    # https://www.freecodecamp.org/news/list-within-a-list-in-python-initialize-a-nested-list/
    radix_sort_tracker = [[] for i in range(base)]
    radix_sort_array = []

    # sort for index
    for ele in array:
        val_at_index = ele[index - 1]
        radix_sort_tracker[val_at_index].append(ele)

    # collapse array
    for array in radix_sort_tracker:
        radix_sort_array = radix_sort_array + array

    return radix_sort_array
