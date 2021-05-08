import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json


driver = webdriver.Chrome(executable_path='C:/Users/Prajay/Desktop/New folder/webdriver/chromedriver')

driver.maximize_window()

driver.get('https://www.python.org')
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_xpath('//*[@id="content"]/div/section/form/ul/li[1]/h3/a')
elem.send_keys(Keys.RETURN)
#driver.switch_to_window("New Window")
