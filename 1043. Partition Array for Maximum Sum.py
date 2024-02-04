""" Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.
Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 10^9
1 <= k <= arr.length
"""

from typing import List

class Solution_1:
    """ Dynamic Programming
    Optimized Copilot's solution is the same as GPT 3.5's solution
    Time complexity: O(n*k)
    Space complexity: O(n)
    Runtime: 264ms - 270ms. Beats 95% of users with Python3
    Memory: 16.6MB - 16.7MB. Beats 78% - 84% of users with Python3
    """
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            curMax = 0
            for j in range(1, min(i, k) + 1):
                curMax = max(curMax, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + curMax * j)
        
        return dp[n]

class Solution_2:
    """ Dynamic Programming
    Bard's solution
    Time complexity: O(n*k)
    Space complexity: O(n)
    Runtime: 1504ms - 1527ms. Beats 16% - 18% of users with Python3
    Memory: 16.6 MB - 16.7 MB. Beats 78% - 84% of users with Python3
    """
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                dp[i] = max(dp[i], dp[i - j] + j * max(arr[i - j:i]))

        return dp[n]

# Testing

if __name__ == "__main__":
    print(Solution_1().maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)) # 84
    print(Solution_1().maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], 4)) # 83
