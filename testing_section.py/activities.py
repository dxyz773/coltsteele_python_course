def eat(food, is_healthy):
    ending = "YOLO!"
    if is_healthy:
        ending = "my body is a temple."

    return f"I'm eating {food} because {ending}"


def nap(num_hrs):
    if num_hrs > 2:
        return f"Ugh I overslept. I didn't meant to nap for {num_hrs} hours!"
    else:
        return f"I'm feeling refreshed after my {num_hrs} hour nap"
