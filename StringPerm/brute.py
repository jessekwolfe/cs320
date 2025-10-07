import time


# Brute force byte string search
def find_pat(text, pat):
    pat_len = len(pat)
    text_len = len(text)
    for i in range(0, text_len - pat_len):
        if text[i : i + pat_len] == pat:
            return i
    return -1


str1 = b"efg"
txt1 = b"abcdefghijk"
print(f"{str1} in {txt1} is {find_pat(txt1, str1)}")
str2 = b"cde"
print(f"{str2} in {txt1} is {find_pat(txt1, str2)}")
str3 = b"nope"
print(f"{str3} in {txt1} is {find_pat(txt1, str3)}")
# now use something big
# scan a file, line by line, and count the lines containing our pattern
str4 = b"room in the castle"


def hamlet(pattern):
    count = 0
    with open("./StringPerm/hamlet.txt") as hamlet:
        for line in hamlet:
            if (find_pat(line.encode("utf-8"), pattern)) != -1:
                count = count + 1
    return count


start_time = time.perf_counter()
total = hamlet(str4)
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Execution time (Mid2): {elapsed_time:.6f} seconds")

print(f"{str4} appears on {total} lines in hamlet.txt")
