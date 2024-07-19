from csv import writer, DictWriter


with open("cats.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "age"])
    csv_writer.writerow(["Martini", 14])
    csv_writer.writerow(["Cosmo", 14])
