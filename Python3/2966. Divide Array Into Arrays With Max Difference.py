# You are given an integer array nums of size n and a positive integer k.

# Divide the array into one or more arrays of size 3 satisfying the following conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

# Constraints:
# n == nums.length
# 1. n is a multiple of 3.
# 2. 1 <= n <= 10^5
MAX_LENGTH = 10 ** 5
# 3. 1 <= nums[i] <= 10^5
# 4. 1 <= k <= 10^5

from typing import List

class Solution:
    # With sorting
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
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

# Tests
if __name__ == "__main__":
    print(Solution().divideArray([23,2,15,20,18,14,20,7,2,22,4,14,7,9,15,14,2,7], 8))
    print(Solution().divideArray([1,3,3,2,7,3], 3))
