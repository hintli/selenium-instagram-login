from selenium import webdriver
import time
browser = webdriver.Firefox()

browser.get("https://www.instagram.com")
#time.sleep(10)
#sign_in = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a")
#sign_in.click()
time.sleep(5)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("username")
password.send_keys("password")

login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a")
login.click()

time.sleep()


time.sleep(5)
browser.close()
