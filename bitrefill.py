from selenium import webdriver
from time import sleep
from instapy_chromedriver import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver.get('https://www.bitrefill.com/?hl=en')
sleep(5)

click_start = driver.get('https://www.bitrefill.com/buy/?hl=en')
sleep(5)

# location_dropdown = driver.find_element_by_xpath ('//*[@id="downshift-9861-toggle-button"]')
location_select= driver.find_element_by_xpath ("//input[@class='b-1spj1v' and starts-with(@placeholder, 'Nigeria')]").send_keys("Worldwide" + "\n")
sleep(10)
search_select = driver.find_element_by_xpath ("//input[@class='b-2PkghU']").send_keys("Spotify" + Keys.ENTER)
sleep(10)

first_option = driver.find_elements_by_xpath ("//*[contains(@class,'b-2hD7la')]/a")[0]
sleep(10)
first_option.send_keys(Keys.ENTER)
sleep(10)

purchase = driver.find_element_by_css_selector ('span.content')
sleep(5)
purchase.click()

#Switch the control to the Alert window
# obj = driver.switch_to.alert()
# name_prompt = Alert(driver) 
# name_prompt.send_keys("")
recipient_name = driver.find_element_by_name ('gift_recipient_name').send_keys('jason')
recipient_email = driver.find_element_by_name ('gift_recipient_email').send_keys('jason@example.com')
your_name = driver.find_element_by_name ('gift_sender_name').send_keys('jane')
message = driver.find_element_by_name ('gift_message').send_keys('Enjoy')
# theme = driver.find_elements_by_xpath ("//input[@name='gift_theme']")[3].click()
# theme = driver.find_element_by_xpath ("//*[contains(@class,'b-2MMBnm')]/a")[4].click()

cart = driver.find_elements_by_xpath ("//input[@class='b-F9sjT7']")[2]
sleep(3)
cart.click()

#b-5M3qcw b-3JEhMz

# sleep(5)
# location.send_keys = ('worldwide')

sleep(10)

driver.close() 



