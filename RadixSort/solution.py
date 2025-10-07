def radix_base(array, base):
    try:
        test_array(array)
        test_base(base)
    except ValueError:
        raise

    return 1


def test_array(array):
    if array is None or not array:
        raise ValueError("invalid␣arguments")
    for element in array:
        try:
            element += 0
        except:
            raise ValueError("invalid␣list␣element")


def test_base(base):
    if not base or base < 2:
        raise ValueError("invalid␣arguments")
