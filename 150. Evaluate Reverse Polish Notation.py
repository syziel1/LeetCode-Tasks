# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution(object):
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
                        stack_of_numbers.append(-int(-a/b))
                    else:
                        stack_of_numbers.append(int(a/b))
            else:
                stack_of_numbers.append(int(token))
        return stack_of_numbers.pop()
    
# Testing
solution = Solution()
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22
print(solution.evalRPN(["2","1","+","3","*"])) # 9
print(solution.evalRPN(["4","13","5","/","+"])) # 6