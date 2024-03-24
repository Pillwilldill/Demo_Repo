from selenium import webdriver
from selenium.webdriver.common.by import By

# begin session
driver = webdriver.Chrome()

# take action on browser (navigate to website)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# request information from browser (cookies, alerts, window handles, etc)
title = driver.title

# synchronize code with current browser state (very difficult)
driver.implicitly_wait(0.5)

# find element to interact with Selenium commands
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# take action on element
text_box.send_keys("Selenium")
submit_button.click()

# request information from element
message = driver.find_element(by=By.ID, value="message")
text = message.text

# while loop to prevent site from closing prematurely
while True:
    print()
# end session and close browser
# driver.quit()