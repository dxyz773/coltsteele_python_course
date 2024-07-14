def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Colt", "second": "Rusty"}
display_names(**names)
