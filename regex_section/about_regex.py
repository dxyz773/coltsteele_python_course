import re

# # Validating Email example
# email = "colt@gmail.com"
# email2 = "carly.simon@yahoo.com"
# email3 = "rosa-98@meals.org"
# email4 = "shoe_queen91@helllo.net"
# email5 = "david+lee+roth@hotmail.com"

pattern = re.compile(r"\d{3} \d{3}-\d{4}")
# res = pattern.search("Call me at 310 445-9876 or 310 445-945")
res = pattern.findall("Call me at 310 445-9876 or 310 445-9456")
print(res)
res2 = re.search(r"\d{3} \d{3}-\d{4}", "203 317-1786")
print(res2.group())
