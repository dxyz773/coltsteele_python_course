import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


c = Cat("Charles", "Tabby")

with open("cat.json", "w") as file:
    frozen = jsonpickle.encode(c)
    file.write(frozen)


with open("cat.json", "r") as file:
    content = file.read()
    unfrozen = jsonpickle.decode(content)
    print(unfrozen)
