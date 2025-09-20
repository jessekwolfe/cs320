def findKey(value, input_array):
    try:
        _isValidParams(value, input_array)
    except ValueError or TypeError:
        raise  # re-raises recieved exception

    if len(input_array) == 0:
        raise LookupError("not in tree")

    try:
        index = 0
        currentValue = input_array[index]
        while currentValue and currentValue != value:
            index = _nextIndex(index, value, currentValue)
            currentValue = input_array[index]
    except LookupError:
        raise LookupError("not in tree")
    except Exception or TypeError:
        raise

    return index


def _nextIndex(index, testValue, currentValue):
    try:
        if testValue < currentValue:
            return (index * 2) + 1  # left
        else:
            return (index * 2) + 2  # right
    except TypeError:  # if items uncomparable
        raise Exception("tree error")


def _isValidParams(key, input_array):
    if input_array is None:
        raise ValueError("no tree")
    if key is None:
        raise ValueError("null key")


def addKey(value, input_array):
    try:
        _isValidParams(value, input_array)
    except ValueError or TypeError:
        raise  # re-raises recieved exception

    try:
        if len(input_array) == 0:
            return [value]
        findKey(value, input_array)
        return input_array  # return existing array if value already exists
    except ValueError or TypeError or Exception:
        raise
    except LookupError:
        pass  # Continue if findKey hits index error

    i = 0
    currentValue = input_array[i]
    try:
        while currentValue is not None:
            i = _nextIndex(i, value, currentValue)
            currentValue = input_array[i]
        return _insertToExistingArray(input_array, i, value)
    except TypeError:
        raise
    except Exception:  # if we go over the current index we need to add empty
        # values to the array, plus the value to be added
        return _addToExistingArray(i, input_array, value)


def _insertToExistingArray(input_array, index, value):
    new_array = input_array.copy()
    new_array[index] = value
    return new_array


def _addToExistingArray(addition_index, original_array, value):
    list_addidtion = []
    additions = addition_index - len(original_array)
    for index in range(0, additions + 1, 1):
        if index == additions:
            list_addidtion.append(value)
        else:
            list_addidtion.append(None)
    return original_array + list_addidtion


def deleteKey(value, input_array):
    try:
        _isValidParams(value, input_array)
    except ValueError or TypeError:
        raise  # re-raises recieved exception

    func_array = input_array.copy()

    try:
        index_key = findKey(value, func_array)
        replacementKey = _iOINext(index_key, func_array)
        if replacementKey is not None:
            func_array[index_key] = func_array[replacementKey]
            func_array[replacementKey] = None
        else:
            func_array[index_key] = None
        if func_array[len(func_array) - 1] is None:
            func_array = _trimArrayNone(func_array)
        return func_array
    except ValueError:
        raise


def _trimArrayNone(func_array):
    while len(func_array) != 0 and func_array[-1] is None:
        func_array.pop()
    return func_array


# returns next inorder node to position n
# core idea is to move right one position
# there are three cases
#   parent -> leftmost of right child
#   left child -> parent
#   right child -> leftmost child of ancestor above parent
#       with right child


def _iOINext(n, t):
    r = (n * 2) + 2  # right

    if (r < len(t)) and (t[r] is not None):
        # parent with right child
        # move to leftmost child of right (or right
        # if no child)
        if (n := _iOILeft(r, t)) is not None:
            return n
        return r
    elif n % 2:
        # left leaf or left parent with no
        # right child, go to parent
        n = (n - 1) // 2  # left child -> parent
        return n
    else:
        # at this point, right leaf with
        # no right children.  So node's
        # parent's subtree is completed.

        # so next is first ancestor
        # above parent who is parent
        # of a left node
        p = (n - 2) // 2  # parent
        leftp = p % 2
        gp = (p - 1) // 2  # grandparent
        while gp and (not leftp):
            leftp = gp % 2
            gp = (gp - 1) // 2

        if leftp:
            return gp

    return -1


def _iOILeft(n, t):
    i = prev = n
    while (i < len(t)) and (t[i] is not None):
        prev = i
        i = (i * 2) + 1
    return prev if (prev != n) else None
