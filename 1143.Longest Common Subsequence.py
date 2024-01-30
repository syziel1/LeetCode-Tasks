# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Remove every letter from text1 that is not in text2
        # This is to reduce the size of the problem
        text1 = "".join([letter for letter in text1 if letter in text2])
        # Remove every letter from text2 that is not in text1
        # This is to reduce the size of the problem
        text2 = "".join([letter for letter in text2 if letter in text1])

        if text1 == "" or text2 == "":
            return 0

        if text1 == text2:
            return len(text1)
                
        # Solution using recursion
        if text1[-1] == text2[-1]:
            return 1 + self.longestCommonSubsequence(text1[:-1], text2[:-1])
        else:
            return max(self.longestCommonSubsequence(text1[:-1], text2), self.longestCommonSubsequence(text1, text2[:-1]))
        
# Testing
text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"
print(Solution().longestCommonSubsequence(text1, text2))
