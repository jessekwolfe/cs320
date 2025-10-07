from collections import Counter
from collections import deque


def countPermStr(haystack, needle):
    try:
        check_params(haystack, needle)
    except ValueError:
        raise
    if isinstance(haystack, str):
        haystack.encode()
    if isinstance(needle, str):
        needle.encode()
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
    queue = deque()
    i = needle_len - 1

    while i < hay_len:
        if haystack[i] not in needle:
            queue.clear()
        else:
            queue.append(haystack[i])
            j = i - 1

            while j >= 0 and haystack[j] in needle:  # Check Left
                queue.appendleft(haystack[j])
                j -= 1

            if len(queue) == needle_len:
                if is_solution(queue, needle):
                    count += 1
                    queue.popleft()

            j = i + 1

            while j < hay_len and haystack[j] in needle:  # Check Right
                queue.append(haystack[j])
                j += 1

                if len(queue) == needle_len:
                    if is_solution(queue, needle):
                        count += 1
                    queue.popleft()
            queue.clear()
            i = j

        i += needle_len - 1

    return count


def simple_perm(haystack, needle):
    return Counter(haystack).get(needle, 0)


def is_solution(test_queue, needle):
    check_queue = Counter(test_queue)
    return check_queue == needle
