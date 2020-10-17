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



# //*[contains(@class,'grid-item')]/a)[1]
# <input type="text" class="b-2PkghU" value="" placeholder="Search for products or gift cards...">
# <a href="https://www.bitrefill.com/buy/?hl=en" class="css-go5ba4">Get Started<svg width="15" height="17"><use href="#arrow_fill" transform="translate(-.97 -.603)"></use><defs><path fill="#fff" id="arrow_fill" d="M15.812 9.214c0-.341-.13-.673-.372-.904L8.901 1.771a1.301 1.301 0 0 0-.914-.381c-.342 0-.663.14-.904.381l-.753.754a1.26 1.26 0 0 0 0 1.808l2.943 2.953H2.2c-.723 0-1.175.602-1.175 1.285v1.286c0 .683.452 1.286 1.175 1.286h7.072L6.33 14.086a1.301 1.301 0 0 0-.382.914c0 .341.14.673.382.914l.753.753c.241.231.562.372.904.372.342 0 .673-.14.914-.372l6.54-6.539c.24-.24.37-.572.37-.914z"></path></defs></svg></a>
# self.driver.find_element_by_xpath("//form[@class='search-box-inner']//input[@class='typeahead search-box-input left' and starts-with(@placeholder, 'Search ratings')]").send_keys("HSBC Bank plc")
# self.driver.find_element_by_css_selector("form.search-box-inner input.typeahead.search-box-input.left[placeholder^='Search ratings']").send_keys("HSBC Bank plc")
# <input type="text" class="typeahead search-box-input left" autocomplete="off" placeholder="Search ratings, research, analysts, and more..." maxlength="900"></div>

# <svg class="b-3_sV2I" id="downshift-9861-toggle-button" tabindex="-1" width="24" height="24" viewBox="0 0 24 24"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path><path d="M0 0h24v24H0z" fill="none"></path></svg>
# <input type="text" class="b-1spj1v" id="downshift-9860-input" tabindex="-1" aria-autocomplete="list" aria-controls="downshift-9861-menu" aria-labelledby="downshift-9861-label" autocomplete="off" value="Worldwide" placeholder="Worldwide" style="padding:12px 40px">