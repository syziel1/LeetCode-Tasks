// Given a matrix and a target, return the number of non-empty submatrices that sum to target.

#include <std>
#include <vector>

class Solution {
public:
    int numSubmatrixSumTarget(std::vector<std::vector<int>>& matrix, int target) {
        int min = matrix[0][0];
        int max = matrix[0][0];
        for (int x = 0; x < matrix.size(); x++) {
            for (int y = 0; y < matrix[0].size(); y++) {
                if (matrix[x][y] < min) {
                    min = matrix[x][y];
                } else if (matrix[x][y] > max) {
                    max = matrix[x][y];
                }
            }
        }
        bool is_not_negative = (min >= 0);
        bool is_not_positive = (max <= 0);
        int num = 0;
        for (int x1 = 0; x1 < matrix.size(); x1++) {
            for (int x2 = x1; x2 < matrix.size(); x2++) {
                // Calculating sum of each row from x1 to x2
                std::vector<int> sum_of_rows(matrix[0].size(), 0);
                for (int y = 0; y < matrix[0].size(); y++) {
                    int sum = 0;
                    for (int x = x1; x <= x2; x++) {
                        sum += matrix[x][y];
                    }
                    sum_of_rows[y] = sum;
                }
                for (int y1 = 0; y1 < matrix[0].size(); y1++) {
                    int sum = 0;
                    for (int y2 = y1; y2 < matrix[0].size(); y2++) {
                        // Adding row y2 to the sum
                        sum += sum_of_rows[y2];
                        if (sum == target) {
                            num += 1;
                        }
                        else if ((is_not_negative && sum > target)
                         || (is_not_positive && sum < target)) {
                            break;
                        }
                    }
                }
            }
        }
        return num;

    }
};