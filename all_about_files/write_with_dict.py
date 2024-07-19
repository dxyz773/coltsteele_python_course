from csv import DictWriter

with open("ashleys_pets.csv", "w") as file:
    headers = ["Name", "Age", "Nickname", "Personality"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow(
        {
            "Name": "Martini",
            "Age": 14,
            "Nickname": "Martini Weeney",
            "Personality": "The king of the house",
        }
    )
