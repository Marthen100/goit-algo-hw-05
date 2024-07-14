import timeit
import pandas as pd

# Load the text files with specified encoding
with open('article1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

with open('article2.txt', 'r', encoding='utf-8') as file:
    text2 = file.read()

# Use smaller portions of the texts for testing
text1_sample = text1[:10000]
text2_sample = text2[:10000]

# Define substrings
substring_existing = "algorithms"
substring_non_existing = "nonexistentpattern"

# Boyer-Moore Algorithm
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0:
        return 0

    bad_char = {}

    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

    return -1

# Knuth-Morris-Pratt Algorithm
def kmp(text, pattern):
    m = len(pattern)
    n = len(text)

    lps = [0] * m
    j = 0

    compute_lps(pattern, m, lps)

    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1

def compute_lps(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Rabin-Karp Algorithm
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == m:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return -1

# Measure execution time
def measure_time(text, pattern, algorithm):
    return timeit.timeit(lambda: algorithm(text, pattern), number=10)

# Results for article 1 sample
bm_time_existing1 = measure_time(text1_sample, substring_existing, boyer_moore)
kmp_time_existing1 = measure_time(text1_sample, substring_existing, kmp)
rk_time_existing1 = measure_time(text1_sample, substring_existing, rabin_karp)

bm_time_non_existing1 = measure_time(text1_sample, substring_non_existing, boyer_moore)
kmp_time_non_existing1 = measure_time(text1_sample, substring_non_existing, kmp)
rk_time_non_existing1 = measure_time(text1_sample, substring_non_existing, rabin_karp)

# Results for article 2 sample
bm_time_existing2 = measure_time(text2_sample, substring_existing, boyer_moore)
kmp_time_existing2 = measure_time(text2_sample, substring_existing, kmp)
rk_time_existing2 = measure_time(text2_sample, substring_existing, rabin_karp)

bm_time_non_existing2 = measure_time(text2_sample, substring_non_existing, boyer_moore)
kmp_time_non_existing2 = measure_time(text2_sample, substring_non_existing, kmp)
rk_time_non_existing2 = measure_time(text2_sample, substring_non_existing, rabin_karp)

# Create a dataframe to present the results
data = {
    "Algorithm": ["Boyer-Moore", "KMP", "Rabin-Karp"],
    "Article 1 - Existing": [bm_time_existing1, kmp_time_existing1, rk_time_existing1],
    "Article 1 - Non-existing": [bm_time_non_existing1, kmp_time_non_existing1, rk_time_non_existing1],
    "Article 2 - Existing": [bm_time_existing2, kmp_time_existing2, rk_time_existing2],
    "Article 2 - Non-existing": [bm_time_non_existing2, kmp_time_non_existing2, rk_time_non_existing2],
}

df = pd.DataFrame(data)

print(df)
