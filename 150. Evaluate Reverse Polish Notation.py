# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution_1(object):
    # Time: O(n)
    # Space: O(n)
    # Runtime of all testcases: 47ms
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack_of_numbers=[]
        for token in tokens:
            if token in "+-*/":
                b = stack_of_numbers.pop()
                a = stack_of_numbers.pop()
                if token == "+":
                    stack_of_numbers.append(a+b)
                elif token == "-":
                    stack_of_numbers.append(a-b)
                elif token == "*":
                    stack_of_numbers.append(a*b)
                else:
                    if a*b<0:
                        stack_of_numbers.append(-int(-a/b)) # not just a/b
                                # because python's division is different from C++
                                # e.g. -1/2 = -1 in python, but -1/2 = 0 in C++
                    else:
                        stack_of_numbers.append(int(a/b))
            else:
                stack_of_numbers.append(int(token))
        return stack_of_numbers.pop()

class Solution_2(object):
    # Time: O(n)
    # Space: O(n)
    # Memory: 13.26MB -> Beats 99.25% of users with Python
    # Runtime of all testcases: 52ms
    def negative_sign_division(self, a, b):
        if a*b<0:
            return -int(-a/b)
        else:
            return int(a/b)
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: self.negative_sign_division(a, b), # not just a/b
                                # because python's division is different from C++
                                # e.g. -1/2 = -1 in python, but -1/2 = 0 in C++
            "*": lambda a, b: a * b
        }
        cur = 0
        while len(tokens) > 1:
            if tokens[cur] in operations:
                tokens[cur - 2] = operations[tokens[cur]](int(tokens[cur - 2]), int(tokens[cur - 1]))
                del tokens[cur - 1:cur + 1]
                cur -= 2
            cur += 1
        return int(tokens[0])

# Testing
solution = Solution_2()
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22
print(solution.evalRPN(["2","1","+","3","*"])) # 9
print(solution.evalRPN(["18"])) # 18