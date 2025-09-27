"""100183. Maximum Good Subarray Sum
Difficulty: Medium

You are given an array nums of length n and a positive integer k.

A subarray of nums is called good if the absolute difference between its first and last element is exactly k, in other words,
the subarray nums[i..j] is good if |nums[i] - nums[j]| == k.

Return the maximum sum of a good subarray of nums. If there are no good subarrays, return 0.

Constraints:
2 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
1 <= k <= 10^9
"""

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        value_to_min_prefix = {}
        best_sum = None

        for num in nums:
            prefix_sum += num

            for target in {num - k, num + k}:
                if target in value_to_min_prefix:
                    candidate = prefix_sum - value_to_min_prefix[target]
                    if best_sum is None or candidate > best_sum:
                        best_sum = candidate

            start_prefix = prefix_sum - num
            if num in value_to_min_prefix:
                if start_prefix < value_to_min_prefix[num]:
                    value_to_min_prefix[num] = start_prefix
            else:
                value_to_min_prefix[num] = start_prefix

        return best_sum if best_sum is not None else 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSubarraySum([1, 4, 5, 2, 3], 1))  # Output: 14
    print(solution.maximumSubarraySum([1, 2, 3, 4, 5], 1))  # Output: 9
    print(solution.maximumSubarraySum([3, 2, 1, 5, 4], 2))  # Output: 12
    print(solution.maximumSubarraySum([1, 2, 3, 4, 5], 10))  # Output: 0
    print(solution.maximumSubarraySum([5, 2, 3, 4, 5], 0))  # Output: 19
    print(solution.maximumSubarraySum([1, 2, 3, 4, 5, 6], 1))  # Output: 11
    print(solution.maximumSubarraySum([-1, 3, 2, 4, 5], 3))  # Output: 11
    print(solution.maximumSubarraySum([-1, -2, -3, -4], 2))  # Output: -6
