""" 100183. Maximum Good Subarray Sum
Difficulty:Medium

You are given an array nums of length n and a positive integer k.

A subarray of nums is called good if the absolute difference between its first and last element is exactly k, in other words, the subarray nums[i..j] is good if |nums[i] - nums[j]| == k.

Return the maximum sum of a good subarray of nums. If there are no good subarrays, return 0.

Constraints:
2 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
1 <= k <= 10^9
"""

from calendar import c
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        found_good = False
        max_sum = 0  # Initialize max_sum with the value for no good subarray
        cur_sum = 0
        for i in range(n):
            cur_sum = nums[i]
            for j in range(i+1, n):
                cur_sum += nums[j]
                if abs(nums[i] - nums[j]) == k:
                    if found_good: # If a good subarray has been found, update max_sum
                        if cur_sum > max_sum:
                            max_sum = cur_sum
                    else: # If it's the first good subarray found, initialize max_sum
                        max_sum = cur_sum
                        found_good = True
        return max_sum

# Testing
print(Solution().maximumSubarraySum([1,4,5,2,3], 1)) # Output: 14
print(Solution().maximumSubarraySum([1,2,3,4,5], 1)) # Output: 9
print(Solution().maximumSubarraySum([3,2,1,5,4], 2)) # Output: 12
print(Solution().maximumSubarraySum([1,2,3,4,5], 10)) # Output: 0
print(Solution().maximumSubarraySum([5,2,3,4,5], 0)) # Output: 19
print(Solution().maximumSubarraySum([1,2,3,4,5,6], 1)) # Output: 11
print(Solution().maximumSubarraySum([-1,3,2,4,5], 3)) # Output: 11
print(Solution().maximumSubarraySum([-1,-2,-3,-4], 2)) # Output: -6
