from bs4 import BeautifulSoup
import requests
from random import randint, choice


def guess_the_quote():
    # Request random page of quotes
    BASE_URL = "http://quotes.toscrape.com"
    page_num = randint(1, 10)
    req = requests.get(f"{BASE_URL}/page/{page_num}")

    # Parse HTML with beautiful soup
    soup_html = BeautifulSoup(req.text, "html.parser")
    # * Should be check right here to see if page has quotes on it and what to do if not
    random_quote_div = choice(soup_html.find_all("div", class_="quote"))

    # Parse quote, author and bio URL
    quote = random_quote_div.find("span", class_="text").text
    author = random_quote_div.find("small", class_="author").text
    fn_initial = author.split()[0][0]
    ln_initial = author.split()[-1][0]
    bio_url = random_quote_div.find(class_="author").find_next_sibling()["href"]

    # Request and parse author bio details with beautiful soup
    bio_req = requests.get(f"{BASE_URL}{bio_url}")
    bio_html = BeautifulSoup(bio_req.text, "html.parser")
    author_birthdate = bio_html.find(class_="author-born-date").text
    author_birth_place = bio_html.find(class_="author-born-location").text
    author_place_date_str = f"They were born {author_birthdate} {author_birth_place}."

    hints = [
        f"{quote}\nWhat author said this quote?\n",
        f"HINT: {author_place_date_str}\n",
        f"HINT: The author's first name starts with {fn_initial}\n",
        f"HINT: The author's last name states with {ln_initial}\n",
    ]

    user_answer = None
    for hint in hints:
        user_answer = input(hint)
        if user_answer.lower() == author.lower():
            break

    ending_response = (
        f"You didn't get it! The author is {author}"
        if not user_answer == author
        else f"CORRECT! YOU GOT IT RIGHT! The author is {author} "
    )
    print(ending_response)
    replay = input("Do you want to play again? (y/n) ")
    if replay == "y":
        return guess_the_quote()
    else:
        return


guess_the_quote()
