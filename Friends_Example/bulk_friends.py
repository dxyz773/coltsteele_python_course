import sqlite3

conn = sqlite3.connect("my_friends.db")

c = conn.cursor()

# people = [
#     ("Ashley", "Fortier", "High School", 10),
#     ("Celina", "Guzman", "High School", 10),
#     ("Jason", "Coombs", "Acting School", 10),
#     ("Reema", "B.", "Acting School", 10),
#     ("Sarah", "Bufano", "College", 3),
# ]
c.execute("SELECT * FROM friends")
print(c.fetchall())
# for x in c:
#     print(x)
# c.executemany("INSERT INTO friends VALUES (?,?,?,?)", people)
conn.commit()
conn.close()
