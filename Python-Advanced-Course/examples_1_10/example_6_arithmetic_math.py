# Example 6 - Arithmetic operations and math functions
import math

friends = 5
friends += 1    # same as friends = friends + 1
friends -= 1    # same as friends = friends - 1
friends *= 2    # same as friends = friends * 2
friends /= 2    # same as friends = friends / 2
friends //= 3   # same as friends = friends / 3 (floor division)
friends **= 2   # same as friends = friends ^ 2
friends %= 2    # same as friends = friends % 2

pi = 3.14
neg = -2

round(pi)   # = 3
abs(neg)    # = 2
pow(neg, 4) # = 16 (base, power)
max(friends, round(pi), neg)   # = 5 (accepts only ints)
min(friends, round(pi), neg)   # = -2 (accepts only ints)

print(math.pi)
print(math.e)
print(math.sqrt(friends))
print(math.floor(pi))
print(math.ceil(pi))
