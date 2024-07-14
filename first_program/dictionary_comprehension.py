# numbers = dict(first=1, second=2, third=3)
# print(numbers)

# squared_nums = {key: value**2 for key, value in numbers.items()}
# print(squared_nums)

teacher = dict(name="colt", city="san francisco", color="purple")

teacher_yell = {value.upper() for value in teacher.values()}

teacher_purple_yell = {
    (num.upper() if num is "color" else num): (
        value.upper() if value is "purple" else value
    )
    for num, value in teacher.items()
}
print(teacher_purple_yell)
# num_list = [1, 2, 3, 4]

# dict_num_list = {num: "even" if num % 2 == 0 else "odd" for num in num_list}
# print(dict_num_list)
