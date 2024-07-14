instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "python",
    "is_hilarious": False,
    44: "my favorite number",
}

# for key, value in instructor.items():
#     print(key, value)

# print(4 in instructor.values())
# print("job" in instructor)

d = instructor.copy()

# print(d == instructor)
# print(d is instructor)

# new_user = dict.fromkeys(["name", "score", "email", "profile_bio"], None)
# print(new_user)

# print(instructor.get("name"))
# print(instructor.get("love", "Wow"))

# name = instructor.pop("name")
# print(name)

# print(dict.fromkeys(["aeiou", "test"], 0))
