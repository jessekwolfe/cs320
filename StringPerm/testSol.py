from collections import defaultdict


def countPermStr(string1, string2):
    n, m = len(string1), len(string2)
    if m > n:
        return 0

    target = defaultdict(int)
    window = defaultdict(int)

    # build counts for target and initial window
    for c in string2:
        target[c] += 1
    for c in string1[:m]:
        window[c] += 1

    # matches = number of distinct characters in target whose counts match in window
    matches = sum(1 for c in target if window.get(c, 0) == target[c])
    result = 1 if matches == len(target) else 0

    # slide the window
    for i in range(m, n):
        in_char = string1[i]
        out_char = string1[i - m]

        # incoming char: only affect matches if it's a target char
        if in_char in target:
            before = window.get(in_char, 0)
            window[in_char] = before + 1
            if window[in_char] == target[in_char]:
                matches += 1
            elif before == target[in_char]:
                matches -= 1
        else:
            window[in_char] = window.get(in_char, 0) + 1

        # outgoing char: only affect matches if it's a target char
        if out_char in target:
            before = window.get(out_char, 0)
            window[out_char] = before - 1
            if window[out_char] == target[out_char]:
                matches += 1
            elif before == target[out_char]:
                matches -= 1
            if window[out_char] == 0:
                del window[out_char]
        else:
            window[out_char] = window.get(out_char, 0) - 1
            if window[out_char] == 0:
                del window[out_char]

        if matches == len(target):
            result += 1

    return result


# Test (your case)
print(countPermStr("abcbaacccaabbaab", "aba"))  # -> 4
