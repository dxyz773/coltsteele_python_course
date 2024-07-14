def make_song(count=99, beverage="soda"):
    curr = count
    end = 0
    while curr >= end:
        try:
            if curr == end:
                yield f"No more {beverage}!"

            elif curr == 1:
                yield f"Only 1 bottle of {beverage} left!"
            else:
                yield f"{curr} bottles of {beverage} on the wall."
            curr = curr - 1 if not curr == 1 else 0
        except StopIteration():
            break


test = make_song(5)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
