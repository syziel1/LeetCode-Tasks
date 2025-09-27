""" Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""

from collections import Counter, defaultdict


class Solution_1:
    def minWindow(self, s: str, t: str) -> str:
        """Return the minimum window in ``s`` that contains all chars from ``t``."""

        if not t or not s:
            return ""

        target_counts = Counter(t)
        required_unique = len(target_counts)

        window_counts = defaultdict(int)
        formed = 0
        left = 0
        best_length = float("inf")
        best_bounds = (0, 0)
        best_window = ""

        for right, char in enumerate(s):
            window_counts[char] += 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            while left <= right and formed == required_unique:
                window_size = right - left + 1
                current_window = s[left : right + 1]
                if window_size < best_length or (
                    window_size == best_length and current_window < best_window
                ):
                    best_length = window_size
                    best_bounds = (left, right)
                    best_window = current_window

                left_char = s[left]
                window_counts[left_char] -= 1
                if (
                    left_char in target_counts
                    and window_counts[left_char] < target_counts[left_char]
                ):
                    formed -= 1
                left += 1

        if best_length == float("inf"):
            return ""
        return best_window
    
# Testing
test_cases = [
    ["ADOBECODEBANC", "ABC", "BANC"],
    ["a", "a", "a"],
    ["a", "aa", ""],
    ["aa", "aa", "aa"],
    ["aabaababb", "baba", "abab"]
]
print("Running test cases...")
result = True
for test in test_cases:
    s, t, expected = test
    actual = Solution_1().minWindow(s, t)
    if actual == expected:
        print("Passed.")
    else:
        result = False
        print(f"FAILED! Test case: {(s, t)}, expected: {expected}, got: {actual}")
        """ F-strings, introduced in Python 3.6, are a way to embed expressions inside string
            literals, using curly braces {}. The expressions will be replaced with their values
            when the string is created. The letter 'f' at the start of the string tells Python
            to allow embedded expressions.
        """
if result:
    print("All test cases passed!")
