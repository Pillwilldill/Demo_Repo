import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def findKeyword(driver, keyword)->bool:
    print(driver.page_source)
    return keyword in driver.page_source

def countElem(driver, tag_name)->int:
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def main():
    # initialize browser
    driver = webdriver.Chrome()

    # navigate to your website
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0
    keyword = "major"
    if findKeyword(driver, keyword):
        total_reward_time += reward_time
        time.sleep(reward_time)

    tags = ["img"]
    for tag in tags:
        num_images = countElem(driver, tag)
        total_reward_time += reward_time * num_images

    driver.quit()
    print("Presence Time:", total_reward_time,"seconds")

if __name__ == "__main__":
    main()