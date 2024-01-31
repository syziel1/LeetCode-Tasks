#include <utility>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        // Remove every letter from text1 that is not in text2
        // This is to reduce the size of the problem
        text1.erase(remove_if(text1.begin(), text1.end(), [&](char c) { return text2.find(c) == string::npos; }), text1.end());
        // Remove every letter from text2 that is not in text1
        // This is to reduce the size of the problem
        text2.erase(remove_if(text2.begin(), text2.end(), [&](char c) { return text1.find(c) == string::npos; }), text2.end());

        #include <algorithm>

                if (text1.empty() || text2.empty()) {
                    return 0;
                }

                if (text1 == text2) {
                    return text1.length();
                }

                // Solution using recursion
                if (text1.back() == text2.back()) {
                    return 1 + longestCommonSubsequence(text1.substr(0, text1.length() - 1), text2.substr(0, text2.length() - 1));
                } else {
                    return max(longestCommonSubsequence(text1.substr(0, text1.length() - 1), text2), longestCommonSubsequence(text1, text2.substr(0, text2.length() - 1)));
                }
    }
};
