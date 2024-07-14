nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list[0][1]
nested_list[1][-1]
# print(nested_list[-1][-2])

# for num in nested_list:
#     for nested in num:
#         print(nested)

[[print(internal) for internal in group] for group in nested_list]


board = [[num for num in range(1, 4)] for val in range(1, 4)]


board2 = [["X" if num % 2 == 0 else "0" for num in range(1, 4)] for row in range(1, 4)]
print(board2)
