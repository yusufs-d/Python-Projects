import requests
from bs4 import BeautifulSoup
import time

url = "https://www.imdb.com/chart/top/"
r = requests.get(url)
html_content = r.content
parser = BeautifulSoup(html_content, "html.parser")
titles = parser.find_all("td", {"class": "titleColumn"})
rates = parser.find_all("td", {"class": "ratingColumn imdbRating"})

while True:
    print("************************************************\n"
          "Welcome to imdb top 250 film !\n1-Show all top 250 movies\n"
          "2-Show movies higher than a certain imdb\npress q to quit\n"
          "************************************************")
    op = input("")
    if op == "1":
        for title, rating in zip(titles, rates):
            title = title.text
            rating = rating.text

            title = title.strip()
            title = title.replace("\n", "")

            rating = rating.strip()
            rating = rating.replace("\n", "")

            print("{}  Rating:{}".format(title, rating))
        time.sleep(2)
    elif op == "2":
        a = float(input("Enter at least imdb rating: "))
        print("Wait a sec...")
        time.sleep(2)
        for title, rating in zip(titles, rates):
            title = title.text
            rating = rating.text

            title = title.strip()
            title = title.replace("\n", "")

            rating = rating.strip()
            rating = rating.replace("\n", "")

            if float(rating) > a:
                print("{}  Rating:{}".format(title, rating))
        time.sleep(2)
    elif op == "q":
        print("Exiting...")
        time.sleep(2)
        break
    else:
        print("Invalid request ! Try again...")
        time.sleep(2)
        continue
