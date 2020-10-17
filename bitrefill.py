from selenium import webdriver
from time import sleep
from instapy_chromedriver import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.implicitly_wait(5)

# Get the bitrefill website
driver.get('https://www.bitrefill.com/?hl=en')
sleep(5)

# navigate to homepage
click_start = driver.get('https://www.bitrefill.com/buy/?hl=en')
sleep(5)

# Select option for worldide
location_select= driver.find_element_by_xpath ("//input[@class='b-1spj1v' and starts-with(@placeholder, 'Nigeria')]").send_keys("Worldwide" + "\n")
sleep(5)

# Search for spotify Uk
search_select = driver.find_element_by_xpath ("//input[@class='b-2PkghU']").send_keys("Spotify  " + Keys.ENTER)
sleep (10)

# Select first option from search list
first_option = driver.find_elements_by_xpath ("//*[contains(@class,'b-2hD7la')]/a")[0]
sleep(10)
first_option.send_keys(Keys.ENTER)
sleep(10)

# click the purchase button
purchase = driver.find_element_by_css_selector ('span.content')
sleep(5)
purchase.click()

# Fill details for buy
recipient_name = driver.find_element_by_name ('gift_recipient_name').send_keys('jason')
recipient_email = driver.find_element_by_name ('gift_recipient_email').send_keys('jason@example.com')
your_name = driver.find_element_by_name ('gift_sender_name').send_keys('jane')
message = driver.find_element_by_name ('gift_message').send_keys('Enjoy')
# theme = driver.find_elements_by_xpath ("//input[@name='gift_theme']")[3].click()
# theme = driver.find_element_by_xpath ("//*[contains(@class,'b-2MMBnm')]/a")[4].click()

cart = driver.find_elements_by_xpath ("//input[@class='b-F9sjT7']")[2]
sleep(3)
cart.click()


sleep(10)
driver.close() 



