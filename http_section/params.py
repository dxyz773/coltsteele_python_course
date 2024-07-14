import requests
from random import choice

url = "https://icanhazdadjoke.com/search"

searched_joke = str(input("What dad joke topic would you like? "))
if not searched_joke:
    searched_joke = "cat"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": searched_joke, "limit": 10},
)
data = res.json()

if data and data["status"] == 200:
    total_jokes = data["total_jokes"]

    if total_jokes:
        chosen_joke = choice(data["results"])["joke"]
        print(f"There are {total_jokes} jokes for {searched_joke}\nHere is one:")
        print(chosen_joke)
    else:
        print(f"Sorry, I don't have any jokes about {searched_joke}")
else:
    print("Something went wrong with your search. Please search again")
