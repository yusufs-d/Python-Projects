from selenium import webdriver
import time
import random

browser = webdriver.Chrome(executable_path="/Users/yusufs/bin/chromedriver")

browser.get("https://www.instagram.com/")

time.sleep(2)

login_button = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[5]/button/span[2]")
login_button.click()
username = "yusufsalih.2363.demir@gmail.com"
password = "*"
email_field = browser.find_element_by_name("email")
password_field = browser.find_element_by_name("pass")
email_field.send_keys(username)
password_field.send_keys(password)
login_button_2 = browser.find_element_by_name("login")
login_button_2.click()
time.sleep(8)
browser.get("https://www.instagram.com/yusufsalihdemir/")
followers_button = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
followers_button.click()
jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage = followers.scrollHeight;
return lenOfPage;
"""
time.sleep(5)
lenOfPage = browser.execute_script(jscommand)
match = False
while match==False:
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
followers_list = list()
followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")

for follower in followers:
    followers_list.append(follower)

with open("followers.txt", "w", encoding="utf-8") as file:
    r_number = random.randint(0, len(followers_list))
    lucky_account = followers_list[r_number]
    for follower in followers:
        file.write(follower.text + "\n")
    file.write("Lucky Account is : "+lucky_account.text+"\n")
browser.close()


