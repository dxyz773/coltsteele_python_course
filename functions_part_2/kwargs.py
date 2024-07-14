def fave_colors(**kwargs):
    print(kwargs)
    for x, y in kwargs.items():
        print(f"{x.capitalize()}'s favorite color is {y}")


fave_colors(colt="purple", ruby="red", ethel="teal")
