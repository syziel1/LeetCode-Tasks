""" You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

We define the right direction as positive x-axis (increasing x-coordinate) and the left direction as negative x-axis (decreasing x-coordinate). Similarly, we define the up direction as positive y-axis (increasing y-coordinate) and the down direction as negative y-axis (decreasing y-coordinate)

You have to place n people, including Chisato and Takina, at these points such that there is exactly one person at every point. Chisato wants to be alone with Takina, so Chisato will build a rectangular fence with Chisato's position as the upper left corner and Takina's position as the lower right corner of the fence (Note that the fence might not enclose any area, i.e. it can be a line). If any person other than Chisato and Takina is either inside the fence or on the fence, Chisato will be sad.

Return the number of pairs of points where you can place Chisato and Takina, such that Chisato does not become sad on building the fence.

Constraints:
2 <= n <= 50
points[i].length == 2
0 <= points[i][0], points[i][1] <= 50
All points[i] are distinct.
"""

import random
from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    if x1 <= x2 and y1 >= y2:
                        # Check if there isn't any point inside the rectangle
                        inside = False
                        for k in range(n):
                            if k != i and k != j:
                                x, y = points[k]
                                if x1 <= x <= x2 and y2 <= y <= y1:
                                    inside = True
                                    break
                        if not inside:
                            count += 1
        return count
    
# Testing
print(Solution().numberOfPairs([[1,1],[2,2],[3,3]])) # Output: 0
print(Solution().numberOfPairs([[6,2],[4,4],[2,6]])) # Output: 2
print(Solution().numberOfPairs([[3,1],[1,3],[1,1]])) # Output: 2
print(Solution().numberOfPairs([[1,2],[3,4],[5,6]])) # Output: 0
# Exaple with 50 randomly generated points
x = random.sample(range(50), 50)
y = random.sample(range(50), 50)
points = [[x[i], y[i]] for i in range(50)]
print(points, Solution().numberOfPairs(points))
