# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        
        min = matrix[0][0]
        max = matrix[0][0]
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] < min:
                    min = matrix[x][y]
                elif matrix[x][y] > max:
                    max = matrix[x][y]
        is_not_negative = (min >= 0)
        is_not_positive = (max <= 0)

        num = 0
        for x1 in range(len(matrix)):
            for x2 in range(x1, len(matrix)):
                # Calculating sum of each row from x1 to x2
                sum_of_rows = []
                for y in range(len(matrix[0])):
                    sum = 0
                    for x in range(x1, x2+1):
                        sum += matrix[x][y]
                    sum_of_rows.append(sum)
                for y1 in range(len(matrix[0])):
                    sum = 0
                    for y2 in range(y1, len(matrix[0])):
                        # Adding row y2 to the sum
                        sum += sum_of_rows[y2]
                        if is_not_negative and sum > target:
                            break
                        if is_not_positive and sum < target:
                            break
                        if sum == target:
                            num += 1
        return num
    
# Tests
matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
print(Solution().numSubmatrixSumTarget(matrix, target)) # 4
matrix = [[1,-1],[-1,1]]
target = 0
print(Solution().numSubmatrixSumTarget(matrix, target)) # 5
matrix = [[904]]
target = 0
print(Solution().numSubmatrixSumTarget(matrix, target)) # 0