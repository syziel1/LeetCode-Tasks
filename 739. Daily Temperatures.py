# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait
# after the ith day to get a warmer temperature. If there is no future day for which
# this is possible, keep answer[i] == 0 instead.

# Constraints:

# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100

class Solution_1(object):
    # Solution 1: brute force
    # Time: O(n^2)
    # Space: O(1)
    # Time Limit Exceeded (34 / 48 testcases passed)
    # Runtime of cases 1,2,3,35 -> 4072ms
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    temperatures[i] = j - i
                    break
            else:
                temperatures[i] = 0
        return temperatures
            
class Solution_2(object):
    # Solution 2: stack
    # Time: O(n)
    # Space: O(n)
    # Runtime of all testcases -> 1071ms
    # Runtime of cases 1,2,3,35 -> 124ms
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res

class Solution_3(object):
    # Solution 3: stack
    # Time: O(n)
    # Space: O(n)
    # Runtime of all testcases -> 1010ms
    # Runtime of cases 1,2,3,35 -> 130ms
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Go through the array from the end to the beginning
        # and keep in the stack the indexes of the temperatures
        # that are greater than the current one in decreasing order.
        # When we find a temperature that is greater than the one
        # in the top of the stack, we pop the stack until we find
        # a temperature that is greater than the current one or
        # the stack is empty. If the stack is empty, it means that
        # there is no greater temperature after the current one.
        # Otherwise, the top of the stack is the index of the next
        # greater temperature.
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            cur = temperatures[i]
            while stack and cur >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# Testing
if __name__ == '__main__':
    sol = Solution_3()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(sol.dailyTemperatures([30,40,50,60]))
    print(sol.dailyTemperatures([30,60,90]))