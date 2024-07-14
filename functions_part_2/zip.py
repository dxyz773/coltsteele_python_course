# five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# print(list(zip(*five_by_two)))
# print(list(zip(five_by_two)))


midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["dan", "ang", "kate"]
# print({zip(students,max(zip()))})


# scores = list(zip(midterms, finals))
# highscores = [max(x) for x in scores]
# print(highscores)
# print(dict(zip(students, highscores)))

final_grades = [max(pair) for pair in zip(midterms, finals)]
student_grades = dict(zip(students, final_grades))
print(student_grades)
