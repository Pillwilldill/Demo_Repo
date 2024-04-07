from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def findText(driver, keyword):
    if keyword.lower() in driver.page_source.lower():
        return True
    else:
        return False
    
def countTagElem(driver, tag_name)->int:
    count = 0
    for tags in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tags))
    return count

'''
Rewards via keyword or image based on action
action : KEYWORD, IMAGE, LINK
driver : wed driver
reward_time : value to wait on site
req_list : list of either keyword or element tag
'''
def userAction(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findText(driver, keyword):
                print("Found", keyword)
                time.sleep(reward_time)
                total_reward_time += reward_time
            else:
                print("Not found")
    elif action.upper() == "IMAGE":
        num_images = countTagElem(driver, req_list)
        total_reward_time = reward_time * num_images
        time.sleep(total_reward_time)

    return total_reward_time

# function to click link 
def clickLink(driver, href):
    # find link
    links = driver.find_elements(By.TAG_NAME, "a")
    # only clicks first link
    for link in links:
        link.click()

def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = userAction("KEYWORD", driver, reward_time, ["investing", "CSUSB"])
    tag_name = "img"
    total_reward_time += userAction("IMAGE", driver, reward_time, [tag_name])
    clickLink(driver)
    driver.quit()

    print("Presence Time", total_reward_time,"seconds")

if __name__ == "__main__":
    main()