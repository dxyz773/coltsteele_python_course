from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"< Human named {self.first} {self.last} >"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            baby = Human("Baby", self.last, 0)
            return baby
        else:
            raise ValueError("Cannot add human to non-human")

    def __mul__(self, multiple):
        if isinstance(multiple, int):
            return [copy(self) for i in range(multiple)]

        else:
            raise ValueError("Cannot multiply with non-int type")


j = Human("Jenny", "Larson", 47)
k = Human("Kenny", "Jones", 48)
newborn = j + k
print(newborn)

triplets = k * 3
triplets[1].first = "Jessica"
print(triplets)
