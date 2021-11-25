import requests
from bs4 import BeautifulSoup
import time
import sys

urls = {
    "istanbul": "https://tr.hotels.com/search.do?destination-id=1341107&q-check-in=2021-08-17&q-check-out=2021-08-18&q-rooms=1&q-room-0-adults=1&q-room-0-children=0&sort-order=BEST_SELLER",
    "ankara": "https://tr.hotels.com/search.do?destination-id=1344642&q-check-in=2021-08-17&q-check-out=2021-08-18&q-rooms=1&q-room-0-adults=1&q-room-0-children=0&sort-order=BEST_SELLER",
    "izmir": "https://tr.hotels.com/search.do?destination-id=1342706&q-check-in=2021-08-17&q-check-out=2021-08-18&q-rooms=1&q-room-0-adults=1&q-room-0-children=0&sort-order=BEST_SELLER",
    "eskisehir": "https://tr.hotels.com/search.do?destination-id=1335913&q-check-in=2021-08-17&q-check-out=2021-08-18&q-rooms=1&q-room-0-adults=1&q-room-0-children=0&sort-order=BEST_SELLER",
    "antalya": "https://tr.hotels.com/search.do?destination-id=1355047&q-check-in=2021-08-17&q-check-out=2021-08-18&q-rooms=1&q-room-0-adults=1&q-room-0-children=0&sort-order=BEST_SELLER"
}




def hotel_finder(city):
    r = requests.get(urls[city])
    html_content = r.content
    parser = BeautifulSoup(html_content, "html.parser")
    names = parser.find_all("h2", {"class": "_3zH0kn"})
    j = 0
    print("The best hotels for you: ")
    for i in names:
        if j < 5:
            i = i.text
            print(i)
            j += 1



print("""
******************************************************************************
Welcome to best hotel finder. Choose your city and see the best hotels for you
Istanbul
Ankara
Izmir
Eskisehir
Antalya
******************************************************************************
""")
try:
    op = input("City: ")
    op = op.lower()
    print("Wait a sec...")
    time.sleep(1)
    hotel_finder(op)

except KeyError:
    sys.stderr.write("Please enter city name correctly !")






