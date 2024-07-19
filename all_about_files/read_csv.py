from csv import reader, DictReader

# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)

#     for x in data:
#         print(x)


with open("fighters.csv") as file:
    dict_reader = DictReader(file)
    for row in dict_reader:
        print(type(row))

test = ["a", "b", "c", "d", "e"]
for i, letter in enumerate(test):
    print(f"index: {i}, letter:{letter}")
