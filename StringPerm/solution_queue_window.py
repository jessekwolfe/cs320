from collections import Counter


def countPermStr(haystack, needle):
    try:
        check_params(haystack, needle)
    except ValueError:
        raise
    if len(needle) == 1:
        return simple_perm(haystack, needle)
    return adv_perm(haystack, needle)


def check_params(haystack, needle):
    if haystack is None or needle is None:
        raise ValueError("Missing Parameter")
    if len(needle) <= 0:
        raise ValueError("No search String")
    if len(needle) > len(haystack):
        raise ValueError("Search string too long")


def adv_perm(haystack, needle):
    needle_len = len(needle)
    hay_len = len(haystack)
    needle = Counter(needle)
    count = 0
    i = needle_len

    # if haystack[i - 1] not in needle:
    #     while i < hay_len and haystack[i] not in needle:
    #         i += needle_len

    queue = Counter(haystack[i - needle_len : i])

    while i < hay_len:
        slide = queue - needle
        slide_amount = slide.total()

        if slide_amount == 0:
            count += 1
            slide_amount = 1

        if haystack[i] not in needle:  # if next isn't in needle slide full
            slide_amount = needle_len

        i = i + slide_amount

        queue = Counter(haystack[i - needle_len : i])
    #     slide = queue - needle
    #     slide_amount = slide.total()

    #     if slide_amount == 0:
    #         count += 1
    #         slide_amount = 1

    #     slide_out = list(haystack[i - needle_len : i - (needle_len - slide_amount)])
    #     queue.subtract(slide_out)
    #     queue = +queue  # remove zeros

    #     slide_in = list(haystack[i : i + slide_amount])
    #     queue.update(slide_in)

    #     i += slide_amount

    slide = queue - needle
    slide_amount = slide.total()

    if slide_amount == 0:
        count += 1

    return count


def simple_perm(haystack, needle):
    count = 0
    for i in range(0, len(haystack), 1):
        if haystack[i] == needle:
            count += 1
    return count


def is_solution(test_queue, needle):
    return test_queue == needle


# Complex solutions that didn't speed things up
# def is_solution(test_queue, needle):
#     test_string = needle
#     test_queue.sort()
#     while len(test_queue) > 0:
#         char = test_queue.pop()
#         index = findIndex(char, test_string)

#         if index is None:
#             return False

#         if len(test_string) <= 1:
#             test_string = ""
#         else:
#             test_string = test_string[:index] + test_string[index + 1 :]

#     if len(test_string) == 0:
#         return True
#     return False

# if index is None:
#     queue.clear()
# else:
#     queue.append(char)

# if len(queue) == needle_length:
#     if is_solution(queue.copy(), needle):
#         count += 1
#     if len(queue) > 1:
#         queue.popleft()
#     else:
#         queue.clear()


# def findIndex(char, array):  # remove sloppy exception caused by standard index find
#     for i in range(0, len(array), 1):
#         if array[i] == char:
#             return i
#     return None


# def investigateIndex(index, haystack, needle):
#     queue = []
#     queue.append(haystack[index])

#     count = 0

#     leftIndex = index - 1
#     rightIndex = index + 1
#     lastRightIndex = rightIndex

#     while leftIndex > -1:  # Investigate Left
#         index_char = haystack[leftIndex]
#         if findIndex(index_char, needle) is not None:
#             queue = [index_char] + queue
#             leftIndex -= 1
#         else:
#             leftIndex = -1

#     if check_for_solution(queue[:], needle):  # Check if full solution left
#         count += 1

#     while rightIndex > -1 and rightIndex < len(haystack):  # Check index right
#         index_char = haystack[rightIndex]
#         if findIndex(index_char, needle) is not None:
#             queue.append(index_char)
#             rightIndex += 1
#             lastRightIndex = rightIndex
#         else:
#             rightIndex = -1

#         if check_for_solution(queue[:], needle):
#             count += 1
#     return count, lastRightIndex

# if index is None:
#     queue.clear()
# else:
#     queue.append(char)

# if len(queue) == needle_length:
#     if is_solution(queue.copy(), needle):
#         count += 1
#     if len(queue) > 1:
#         queue.popleft()
#     else:
#         queue.clear()


# def check_for_solution(queue, needle):
#     flag = False
#     if len(queue) == len(needle):
#         if is_solution(queue, needle):
#             flag = True
#         if len(queue) > 1:
#             queue = queue[1:]
#         else:
#             queue.clear()
#     return flag
