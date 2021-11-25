from selenium import webdriver
import time
import random

browser = webdriver.Chrome(executable_path="/Users/yusufs/bin/chromedriver")
r_entry = []
for i in range(10):
    numb_for_page = random.randint(1, 407)
    numb_for_entry = random.randint(1, 9)
    url = "https://eksisozluk.com/elon-musk--1573334?p=" + str(numb_for_page)

    browser.get(url)
    content = browser.find_elements_by_css_selector('.content')
    r_entry.append(content[i].text)
    print("****************************************************")
    print(content[numb_for_entry].text)
    time.sleep(3)

browser.close()

with open("random_entries.txt", "w", encoding="utf-8") as file:
    for e in r_entry:
        file.write("\n---------------------------------------------\n")
        file.write(e)

