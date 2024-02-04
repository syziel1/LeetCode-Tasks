""" Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""

class Solution_1:
    def minWindow(self, s: str, t: str) -> str:
        # Create a dictionary to store the frequency of each character in t
        t_count = {}
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1
        # Create a dictionary to store the frequency of each character in s
        s_count = {}
        for char in s:
            s_count[char] = 0
        window_count = {}
    
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
    if Solution_1().minWindow(s, t) == expected:
        print("Passed.")
    else:
        result = False
        print(f"FAILED! Test case: {s, t}, expected: {expected}, got: {result}")
        """ F-strings, introduced in Python 3.6, are a way to embed expressions inside string
            literals, using curly braces {}. The expressions will be replaced with their values
            when the string is created. The letter 'f' at the start of the string tells Python
            to allow embedded expressions.
        """
if result:
    print("All test cases passed!")
