# from random import random


# def flip_coin():
#     if random() > 0.5:
#         return "Heads"
#     else:
#         return "Tails"


# # print(flip_coin())
# def generate_evens():
#     return [x for x in range(1, 50) if x % 2 == 0]


# print(generate_evens())


def exponent(num, power=2):
    """exponent(num, power) raises num to specified power. Power defaults to 2."""
    return num**power


print(exponent.__doc__)
