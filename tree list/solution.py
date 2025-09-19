def findKey(value, input_array):
    try:
        _isValidFindParams(value, input_array)
    except:
        raise  # re-raises recieved exception

    try:
        index = 0
        currentValue = input_array[index]
        while currentValue != value:
            index = _nextIndex(index, value, currentValue)
            currentValue = input_array[index]
    except:
        raise LookupError("not in tree")

    return index


def _nextIndex(index, testValue, currentValue):
    if testValue < currentValue:
        return (index * 2) + 1  # left
    else:
        return (index * 2) + 2  # right


def _isValidFindParams(key, input_array):
    if len(input_array) == 0:
        raise ValueError("no tree")
    if key is None:
        raise ValueError("null key")


def addKey(value, input_array):
    try:
        if value is None:
            raise ValueError("null key")
        if len(input_array) == 0:
            return [value]
        findKey(value, input_array)
        return input_array  # return existing array if value already exists
    except ValueError as err:
        raise
    except:
        pass  # Continue if findKey hits index error

    i = 0
    currentValue = input_array[i]
    try:
        while currentValue is not None:
            i = _nextIndex(i, value, currentValue)
            currentValue = input_array[i]
        return _insertToExistingArray(input_array, i, value)
    except:  # if we go over the current index we need to add empty
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


def deleteKey(key, array):
    pass


# returns leftmost child of position n
def _iOILeft(n, t):
    i = prev = n
    while (i < len(t)) and (t[i] is not None):
        prev = i
        i = (i * 2) + 1
    return prev if (prev != n) else None


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


# this is a generator routine that
# returns successive elements in the
# inorder traversal


def _iOI(t):
    # find leftmost child = start node
    if (inorder := _iOILeft(0, t)) is None:
        inorder = 0
    while inorder >= 0:
        yield t[inorder]
        inorder = _iOINext(inorder, t)


# Inorder traversal that is iterative and does
# not use a stack (similar to a Morris
# traversal)


def inOrderIter(t):
    if not len(t):
        return []
    return list(_iOI(t))


# helper routine for recursive traversal
# returns a list which is the in-order traversal
# of the subtree rooted at node


def _iOR(t, node):
    if (node >= len(t)) or (t[node] is None):
        return []
    left = _iOR(t, (2 * node) + 1)
    right = _iOR(t, (2 * node) + 2)
    return left + [t[node]] + right


# Classic inorder recursive traversal


def inOrderRecurse(t):
    return _iOR(t, 0)


# insert unit tests here
if __name__ == "__main__":

    t1 = [4, 2, 6, 1, 3, 5, 7]
    t2 = [4, 2, 6, 1, None, 5, 7]
    t3 = [1, None, 2, None, None, None, 4]
    t4 = [4, 2, None, 1]

    print(findKey(7, t1))
    # print(f"inOrderRecurse{t1} is {inOrderRecurse(t1)}")
    # print(f"inOrderIter{t1} is {inOrderIter(t1)}")
    # print(f"inOrderRecurse{t2} is {inOrderRecurse(t2)}")
    # print(f"inOrderIter{t2} is {inOrderIter(t2)}")
    # print(f"inOrderRecurse({t3}) is {inOrderRecurse(t3)}")
    # print(f"inOrderRecurse({t3}) is {inOrderIter(t3)}")
    # print(f"inOrderRecurse({t4}) is {inOrderRecurse(t3)}")
    # print(f"inOrderRecurse({t4}) is {inOrderIter(t3)}")
