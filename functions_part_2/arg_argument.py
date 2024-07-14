def sum_all_values(*args):
    print(args)
    print(sum(x for x in args))


nums = [1, 2, 3, 4, 5]
sum_all_values(*nums)
