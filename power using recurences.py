# My implementation of the power function with natural number exponents only using recursion

def power(base, exponent):
    # During each recursive call, the exponent is halved until it reaches 0
    # If the exponent is even, the base is squared and multiplied by itself
    # If the exponent is odd, the base is multiplied by itself and the exponent is decremented by 1
    # The base case is when the exponent is 0, in which case 1 is returned

    # The time complexity is O(log n) because the exponent is halved during each recursive call
    # The space complexity is O(log n) because the number of recursive calls is equal to the exponent
    # The space complexity can be reduced to O(1) by using a while loop instead of recursion

    # During tests, counting the number of multiplications
    multiplications = 0
    
    if exponent == 0:
        return 1
    elif exponent%2 == 0:
        sqrt = power(base, exponent/2)
        return sqrt*sqrt
    else:
        return base*power(base, exponent-1)
    
print(power(2, 3))
print(power(2, 4))
print(power(2, 5))
print(power(2, 6))
print(power(2, 7))
print(power(2, 8))
