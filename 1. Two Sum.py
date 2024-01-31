# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        index_1 = 0
        index_2 = len(sorted_nums) - 1
        while index_1 < index_2:
            if sorted_nums[index_1] + sorted_nums[index_2] == target:
                original_index_1 = nums.index(sorted_nums[index_1])
                original_index_2 = nums.index(sorted_nums[index_2])
                if original_index_1 == original_index_2:
                    nums.pop(original_index_1)
                    original_index_2 = nums.index(sorted_nums[index_2]) + 1
                return [original_index_1, original_index_2]
            elif sorted_nums[index_1] + sorted_nums[index_2] > target:
                index_2 -= 1
            else:
                index_1 += 1

        return [-1, -1] # If no solution found, return [-1, -1]
    
TestExample1 = [[2,7,11,15], 9]   # Output: [0,1]
TestExample2 = ([3,2,3], 6)       # Output: [0,2]
TestExample3 = ([3,3], 6)         # Output: [0,1]

# Testing
print("Example 1:\n Input: ", TestExample1[0], TestExample1[1], "\n Output: ", Solution().twoSum(TestExample1[0], TestExample1[1]))
print("Example 2:\n Input: ", TestExample2[0], TestExample2[1], "\n Output: ", Solution().twoSum(TestExample2[0], TestExample2[1]))
print("Example 3:\n Input: ", TestExample3[0], TestExample3[1], "\n Output: ", Solution().twoSum(TestExample3[0], TestExample3[1]))