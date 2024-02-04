""" You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

Constraints:
nums.length == 3
1 <= nums[i] <= 100
"""

from typing import List
triangle_type = ["equilateral", "isosceles", "scalene", "none"]

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            if nums[0] == nums[1] == nums[2]:
                return triangle_type[0]
            elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
                return triangle_type[1]
            else:
                return triangle_type[2]
        else:
            return triangle_type[3]
        