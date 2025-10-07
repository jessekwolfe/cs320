def countPermStr(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return 0

    # Step 1: build frequency counts
    from collections import defaultdict

    def freq_hash(counter):
        # Simple hash: sum of prime^char * count
        h = 0
        prime = 257  # prime base
        mod = 2**61 - 1  # large prime modulus
        for ch, count in counter.items():
            h = (h + (hash(ch) % mod) * count) % mod
        return h

    target = defaultdict(int)
    window = defaultdict(int)

    for c in pattern:
        target[c] += 1
    for c in text[:m]:
        window[c] += 1

    target_hash = freq_hash(target)
    window_hash = freq_hash(window)

    result = 0
    if target_hash == window_hash and window == target:
        result += 1

    # Step 2: slide the window
    for i in range(m, n):
        in_char = text[i]
        out_char = text[i - m]

        window[in_char] += 1
        window[out_char] -= 1
        if window[out_char] == 0:
            del window[out_char]

        window_hash = freq_hash(window)

        if window_hash == target_hash and window == target:
            result += 1

    return result
