from termcolor import colored

hey = colored(
    "HEY, I'M HERE!", color="magenta", on_color="on_cyan", attrs=["reverse", "blink"]
)
print(hey)
