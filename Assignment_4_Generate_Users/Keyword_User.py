import time
from selenium import webdriver

'''
Returns true or false on whether keyword exists
Capitalization should not matter (e.g. will detect "Robinhood" on a page as "robinhood" and vice versa
Will detect super word in page (e.g. will detect "robinhoods" on a page as "robinhood" 
'''

def findKeyword(driver, keyword)->bool:
    print(driver.page_source.lower())
    return keyword.lower() in driver.page_source.lower()

def main():
    # initialize browser
    driver = webdriver.Chrome()

    # navigate to your website
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0
    keyword = "robinhood"
    if findKeyword(driver, keyword):
        total_reward_time += reward_time
        time.sleep(reward_time)

    driver.quit()
    print("Presence Time:", total_reward_time,"seconds")

if __name__ == "__main__":
    main()