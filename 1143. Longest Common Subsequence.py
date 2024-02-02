# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution_1(object):
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

# All letters in the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Remeber pairs of checked parts of teksts
checked = {}
class Solution_2(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if text1 == "" or text2 == "":
            return 0

        """ Count the number of times each letter appears in text1 and text2.
        Remeber the letter, if it apears in both text1 and text2 """
        letter_count_text1 = {}
        letter_count_text2 = {}
        letters_in_both = []
        for letter in alphabet:
            letter_count_text1[letter] = text1.count(letter)
            letter_count_text2[letter] = text2.count(letter)
            if letter_count_text1[letter] != 0 and letter_count_text2[letter] != 0:
                letters_in_both.append(letter)

        if len(letters_in_both) == 0: # If there are no instances of any letter in both texts
            return 0
        
        """ Remove every letter from text1 and text2 that is not in both texts """
        for letter in alphabet:
            if letter not in letters_in_both:
                text1 = text1.replace(letter, "")
                text2 = text2.replace(letter, "")
        
        if text1 == text2:
            return len(text1)
        
        if len(letters_in_both) == 1: # If there are anly instances of one letter in both texts
            return min(letter_count_text1[letters_in_both[0]], letter_count_text2[letters_in_both[0]])
        
        if len(text2) > len(text1): # Make sure that text1 is not the shortest text
            text1, text2 = text2, text1
        
        if (text1, text2) in checked: # If we have already checked this pair of texts
            return checked[(text1, text2)]
        
        """ Solution using recursion """
        max_length = 0
        for letter in letters_in_both:
            for i in range(letter_count_text1[letter]):
                for j in range(letter_count_text2[letter]):
                    letter_position_text1 = text1.find(letter, i)
                    letter_position_text2 = text2.find(letter, j)
                    res = 1 + self.longestCommonSubsequence(text1[letter_position_text1+1:], text2[letter_position_text2+1:])
                    + self.longestCommonSubsequence(text1[:letter_position_text1], text2[:letter_position_text2])
                    if res > max_length:
                        max_length = res
        checked[(text1, text2)] = max_length
        return max_length
    
# Testing
text1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
text2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(Solution_2().longestCommonSubsequence(text1, text2))
