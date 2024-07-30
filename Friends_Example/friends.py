import sqlite3

conn = sqlite3.connect("my_friends.db")
"""
CREATE TABLE friends (fname TEXT, lname TEXT, meeting_place TEXT )
"""
c = conn.cursor()
# c.execute(
#     "CREATE TABLE friends (fname TEXT, lname TEXT, meeting_place TEXT, closeness INT);"
# )
form_first = "Ashley"
data = ("Lauren", "Iu", "High School", 10)
query = "INSERT INTO friends (fname,lname,meeting_place,closeness) VALUES (?,?,?,?)"
conn.execute(query, data)
conn.commit()
conn.close()
