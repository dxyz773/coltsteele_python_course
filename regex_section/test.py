# name = "Bob"
# my_string = f"Hello {name}!"
# name = "Rolf"

# print(my_string)


"""
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
"""


# def add(a, b):
#     return a + b


# def once(fn):
#     run = 1

#     def inner(*args):
#         nonlocal run
#         if run > 0:
#             run -= 1
#             return fn(*args)

#     return inner


# oneAddition = once(add)

# print(oneAddition(2, 2))
# print(oneAddition(2, 2))
# print(oneAddition(2, 2))


"""
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
"""


# def running_average():
#     running_average.test = 0
#     running_average.size = 0

#     def inner(num):
#         running_average.test += num
#         running_average.size += 1
#         return running_average.test / running_average.size

#     return inner


# def running_average():
#     count = 0
#     average = 0

#     def inner(num):
#         nonlocal count
#         nonlocal average
#         average += num
#         count += 1
#         return average / count

#     return inner


# rAvg = running_average()
# print(rAvg(10))  # 10.0
# print(rAvg(11))  # 10.5
# print(rAvg(12))  # 11


def next_prime():
    num = 2
    while True:
        if len([x for x in range(num, 0, -1) if num % x == 0]) <= 2:
            yield num
        num += 1


primes = next_prime()
test = [next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(test)
