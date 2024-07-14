def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print("All arguments must be of type int or float")


divide(1, 0)
