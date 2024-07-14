import pyfiglet as pyfig
from termcolor import colored

f = pyfig.figlet_format("1", font="slant")


colors = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "light_grey",
    "dark_grey",
    "light_red",
    "light_green",
    "light_yellow",
    "light_blue",
    "light_magenta",
    "light_cyan",
)

try:
    display = pyfig.figlet_format(
        str(input("What message do you want to print? ")), font="slant"
    )
    color_choice = input("What color? ")
    if not color_choice.lower() in colors:
        color_choice = "green"

    colorful_display = colored(display, color=color_choice)
    print(colorful_display)
except:
    print("Unable to print selected color")
