""" You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.
"""

# Constraints:
# n == nums.length
# 1. n is a multiple of 3.
# 2. 1 <= n <= 10^5
MAX_LENGTH = 10 ** 5
# 3. 1 <= nums[i] <= 10^5
# 4. 1 <= k <= 10^5

class Solution_1(object):
    # With sorting
    # Time complexity: O(n log n)
    # Runtime: 721ms. Beats over 99% of users with Python
    # Memory: 27.78 MB. Beats 97% of users with Python
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort() # Time complexity of sort is O(n log n)
        res = []
        i = 0
        while i < len(nums):
            if nums[i+2] - nums[i] <= k:
                res.append(nums[i:i+3])
                i += 3 # not an error, because n is a multiple of 3 (Constraint 1)
            else:
                return []
        return res

class Solution_2(object):
    # Without sorting
    # Time complexity: O(n)
    # Runtime: 920ms
    # Memory: 27.48 MB. Beats 97% of users with Python
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # Counting the quantity of each number in nums
        quantity_of_numbers = [0] * (MAX_LENGTH + 1)
        # Additionally, searching for the first and the last numbers in nums
        first = last = nums[0]
        for num in nums:
            quantity_of_numbers[num] += 1
            if num < first:
                first = num
            elif num > last:
                last = num

        res = []

        first_of_trinity = first
        trinity = [first_of_trinity]
        j = 1
        quantity_of_numbers[first_of_trinity] -= 1

        i = first
        while i <= last:
            while quantity_of_numbers[i] > 0:
                if j < 3:
                    if i - first_of_trinity > k:
                        return []
                    trinity.append(i)
                    j += 1
                else:
                    res.append(trinity)
                    first_of_trinity = i
                    trinity = [first_of_trinity]
                    j = 1
                quantity_of_numbers[i] -= 1
            i += 1
        res.append(trinity) # adding the last trinity
        return res

# Testing
if __name__ == "__main__":
    print(Solution_2().divideArray([23,2,15,20,18,14,20,7,2,22,4,14,7,9,15,14,2,7], 8))
    print(Solution_2().divideArray([1,3,3,2,7,3], 3))
