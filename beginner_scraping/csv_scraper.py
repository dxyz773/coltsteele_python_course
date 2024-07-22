from bs4 import BeautifulSoup
import requests
from csv import DictReader, DictWriter
from random import choice

BASE_URL = "http://quotes.toscrape.com"


def add_quotes_to_csv(quotes):
    # Open/create quotes.csv file to add current page's worth of quotes

    with open("quotes.csv", "a") as file:
        headers = [
            "author",
            "quote",
            "first_initial",
            "last_initial",
            "birthday",
            "birth_place",
            "bio",
        ]

        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


def get_quotes(soup):

    # Get all quote elements on current page
    curr_page_quotes = soup.find_all("div", class_="quote")

    # Initialize empty list
    quotes = []

    # Compose quote and append quote to quotes list
    for quote_el in curr_page_quotes:
        # Parse quote div's bio url
        bio_url = quote_el.find(class_="author").find_next_sibling()["href"]

        # Request and parse author bio page
        bio = BeautifulSoup(requests.get(f"{BASE_URL}{bio_url}").text, "html.parser")

        # Construct quote object
        quote = {
            "author": quote_el.find("small", class_="author").text,
            "quote": quote_el.find("span", class_="text").text,
            "first_initial": quote_el.find("small", class_="author").text.split()[0][0],
            "last_initial": quote_el.find("small", class_="author").text.split()[-1][0],
            "birthday": bio.find(class_="author-born-date").text,
            "birth_place": bio.find(class_="author-born-location").text,
            "bio": bio.find("div", class_="author-description").text,
        }
        quotes.append(quote)

    # Pass list of quotes from current page to csv function
    add_quotes_to_csv(quotes)


# Calls get_quotes function
def scrape():
    req = requests.get(BASE_URL)
    # Parse HTML with beautiful soup
    soup = BeautifulSoup(req.text, "html.parser")

    get_quotes(soup)
    # Parse next button
    next_btn = soup.find("li", class_="next")

    while next_btn:
        # Parse next page url addition
        next_page = next_btn.findChild("a")["href"]
        new_soup = BeautifulSoup(
            requests.get(f"{BASE_URL}{next_page}").text, "html.parser"
        )
        get_quotes(new_soup)
        # print(next_page)
        next_btn = new_soup.find("li", class_="next")


# scrape()


def guess_the_quote_v2():
    quote = None

    # Read quotes from quotes csv file. Randomly choose quote. Set chosen_quote to randomly selected quote object

    with open("quotes.csv") as file:
        dict_reader = DictReader(file)
        quotes = list(dict_reader)
        quote = choice(quotes)

    author = quote.get("author")
    user_answer = None
    num = 4

    hints = [
        f'{quote.get("quote")}\nWhat author said this quote?\n',
        f'HINT: The author was born {quote.get("birthday")} {quote.get("birth_place")}\n',
        f'HINT: The author\'s first name starts with {quote.get("first_initial")}\n',
        f'HINT: The author\'s last name states with {quote.get("last_initial")}\n',
    ]

    for hint in hints:
        print(author)
        if num < 4:
            print(f"You have {num} guesses")
        user_answer = input(hint)
        num -= 1
        if user_answer.lower() == author.lower():
            break

    ending_response = (
        f"You are out of guesses! The author is {author}"
        if not user_answer.lower() == author.lower()
        else f"CORRECT! YOU GOT IT RIGHT! The author is {author} "
    )
    print(ending_response)

    replay = input("Do you want to play again? (y/n) ")

    if replay.lower() == "y" or replay.lower() == "yes":
        return guess_the_quote_v2()
    else:
        return


guess_the_quote_v2()
