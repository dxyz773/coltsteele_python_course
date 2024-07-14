def get_multiples(num=1, count=10):
    curr = num
    while curr < count:
        yield from range(num, count + 1, num)


test = get_multiples(2, 3)
print(next(test))
print(next(test))
print(next(test))
