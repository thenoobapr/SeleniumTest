from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import names

nam = names.get_first_name()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:/Users/Prajay/Desktop/New folder/webdriver/chromedriver')
driver.maximize_window()
actions = ActionChains(driver)
driver.get('http://bit.ly/3t8xMEZ')
elem = driver.find_element_by_xpath('//*[@id="content"]/landing-event-details/div[2]/div[1]/div/div[1]/div').click()
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://mail.tm/en/')
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="address"]').click()
driver.switch_to.window(driver.window_handles[0])
elem = driver.find_element_by_xpath('//*[@id="phoneEmail"]')
actions.move_to_element(elem)
actions.click(elem)
elem.send_keys(Keys.CONTROL, 'v')
actions.perform()
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="landing-content"]/auth-auth-page/div/div/div/auth-login-signup/div/auth-initial-login-form/div/div[3]/section/div/form/div[2]/div/button').click()
elem = driver.find_element_by_xpath('//*[@id="mat-input-2"]').click()
elem.send_keys('ravi krishna')
elem = driver.find_element_by_xpath('/html/body/center/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr/td/div/div[1]/span/strong')
