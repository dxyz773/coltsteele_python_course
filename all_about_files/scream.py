from csv import reader, writer


with open("fighters.csv") as file:
    the_reader = reader(file)
    with open("screaming_fighters.csv", "w") as scream:
        scream_writer = writer(scream)
        for fighter in the_reader:
            scream_writer.writerow([s.capitalize() for s in fighter])
