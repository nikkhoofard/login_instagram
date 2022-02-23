from time import sleep
from selenium import webdriver

browser = webdriver.Chrome('D:\\c++ project\\pythonProject\\login_instagram\\chromedriver\\chromedriver.exe')


browser.implicitly_wait(1)

browser.get('https://www.instagram.com/')

sleep(1)
username = browser.find_element_by_css_selector("input[name='username']")
password = browser.find_element_by_css_selector("input[name='password']")

username.send_keys("mohammad_hosseinn110")
password.send_keys("//9811126100//")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(9999999)

browser.close()
