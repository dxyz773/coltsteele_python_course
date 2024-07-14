# f = open("../../../story.txt")
# print(f.read())
# f.seek(0)
# lines = f.readlines()
# print(lines)
# print(f.closed)
# f.close()
# print(f.closed)


with open("../../../story.txt") as file:
    story = file.read()

    print(file)
    print(story)


print(file.closed)
