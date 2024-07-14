class Pet:
    allowed = ["cat", "dog", "fish", "bird"]

    def __init__(self, name, species):
        self.name = name
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self.species = species


pet1 = Pet("Martini", "bunny")
