# Functions

## Function One: `twoSum`

# `twoSum` is a function which finds which two numbers in a list of numbers add up to the given target.

# ```py
# def twoSum(n, t):
#     counter = 0
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             num1 = n[i]
#             num2 = n[j]

#             if num1 + num2 == t:
#                 counter += 1
#         return counter
# print(twoSum([3, 5, 8, 1, 9], 17))


def twoSum(n, t):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[j] == t - n[i]:
                return [i, j]
        
print(twoSum([3, 5, 8, 1, 9], 17))

