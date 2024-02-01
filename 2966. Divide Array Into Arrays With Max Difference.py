# You are given an integer array nums of size n and a positive integer k.

# Divide the array into one or more arrays of size 3 satisfying the following conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

# Constraints:
# n == nums.length
# 1. n is a multiple of 3.
# 2. 1 <= n <= 105
# 3. 1 <= nums[i] <= 105
# 4. 1 <= k <= 105

class Solution_1(object):
    # Time complexity: O(n log n)
    # Runtime: 721ms. Beats over 99% of users with Python
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
    
# Testing
if __name__ == "__main__":
    print(Solution_1().divideArray([1,3,4,8,7,9,3,5,1], 2))
    print(Solution_1().divideArray([1,3,3,2,7,3], 3))
