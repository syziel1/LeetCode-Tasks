/* 100183. Maximum Good Subarray Sum
Difficulty:Medium
You are given an array nums of length n and a positive integer k.

A subarray of nums is called good if the absolute difference between its first and last element is exactly k, in other words, the subarray nums[i..j] is good if |nums[i] - nums[j]| == k.

Return the maximum sum of a good subarray of nums. If there are no good subarrays, return 0.

Constraints:
2 <= nums.length <= 10^5
-109 <= nums[i] <= 10^9
1 <= k <= 10^9
*/

#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long ans = 0;
        long long sum = 0;
        map<long long, long long> mp;
        mp[0] = -1;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            if (mp.count(sum - k)) {
                ans = max(ans, sum - mp[sum - k]);
            }
            if (!mp.count(sum)) {
                mp[sum] = i;
            }
        }
        return ans;        
    }
};