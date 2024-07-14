class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        split_data = data_str.split(",")
        first_name, last_name, age = split_data
        return cls(first_name, last_name, int(age))

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.active_users += 1

    def __repr__(self) -> str:
        return f"<User:{self.first_name} {self.last_name}>"

    def logout(self):
        User.active_users -= 1
        return f"{self.first_name} logged out"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def likes(self, liked):
        return f"{self.first} liked {liked}"

    def birthday(self):
        self.age += 1
        print(self.age)
        print(f"Happy {self.age}th Birthday, {self.first_name}!")

    def is_senior(self):
        return self.age >= 65


user1 = User("Mary", "Jane", 42)
user2 = User("Jerry", "Wilde", 23)


class Moderator(User):
    total_mods = 0

    @classmethod
    def display_total_mods(cls):
        return f"There are {cls.total_mods} total mods"

    def __init__(self, first_name, last_name, age, community):
        super().__init__(first_name, last_name, age)
        self.community = community
        Moderator.total_mods += 1

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community}"


jasmine = Moderator("Jasmine", "Ryan", 25, "soccer community")
jasmine = Moderator("Jasmine", "Ryan", 25, "soccer community")
jasmine = Moderator("Jasmine", "Ryan", 25, "soccer community")
jasmine = Moderator("Jasmine", "Ryan", 25, "soccer community")
print(Moderator.display_total_mods())
print(User.display_active_users())
