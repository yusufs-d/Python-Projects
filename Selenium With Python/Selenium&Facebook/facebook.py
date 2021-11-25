from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="/Users/yusufs/bin/chromedriver")
url = "https://www.facebook.com/"

browser.get(url)
sleep(3)

username = "yusufsalih.2363.demir@gmail.com"
password = "*"
username_field = browser.find_element_by_xpath("//*[@id='email']")
password_field = browser.find_element_by_xpath("//*[@id='pass']")
username_field.send_keys(username)
password_field.send_keys(password)
sleep(2)
password_field.send_keys(Keys.RETURN)
sleep(10)
browser.close()
