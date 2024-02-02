""" An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
"""

# Constraints:
# 10 <= low <= high <= 10^9

from typing import List

class Solution_1:
    # Loops with number as integer
    # Runtime: 34ms - 40ms
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequential_digits_numbers = []
        for number_of_digits in range(len(str(low)), 10): # 10 is not included
            for start in range(1, 11 - number_of_digits): # first digit of the number
                number = start
                for i in range(start + 1, start + number_of_digits):
                    number = number * 10 + i
                if number > high:
                    return sequential_digits_numbers
                if number >= low:
                    sequential_digits_numbers.append(number)
        return sequential_digits_numbers
    
class Solution_2:
    # Loops with number as string
    # Runtime: 34ms - 44ms
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequential_digits_numbers = []
        for number_of_digits in range(2, 10): # 10 is not included
            for start in range(1, 11 - number_of_digits): # first digit of the number
                number = str(start)
                digit = start + 1
                for i in range(1, number_of_digits):
                    number += str(digit)
                    digit += 1
                number = int(number)
                if number > high:
                    return sequential_digits_numbers
                if number >= low:
                    sequential_digits_numbers.append(number)
        return sequential_digits_numbers
    
# Testing
    
if __name__ == "__main__":
    print(Solution_1().sequentialDigits(100, 300)) # [123,234]