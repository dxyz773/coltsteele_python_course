def colorize(text, color):
    if type(text) != str or type(color) != str:
        raise TypeError("Text and color must be of type string")
    print(f"Printed {text} in {color}")


colorize("hello", 2)
colorize("hello", "red")
