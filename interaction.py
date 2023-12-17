from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# initialize web driver
driver = webdriver.Chrome()

# get site to scrap
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# find element using Xpath
# stats = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(stats.text)

# find element using css selector
article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")

# to make the link be clicked automatically
# article_count.click()

all_portals = driver.find_element(by=By.LINK_TEXT, value="projects")
# all_portals.click()

# to search for items using the search bar
search = driver.find_element(by=By.NAME, value="search")    # get hold of the search bar
search.send_keys("Python")      # types "Python" in the search bar field
search.send_keys(Keys.ENTER)    # presses the "Enter" key automatically

# close all tabs in driver
choice = input("Enter q to exit:")
if choice == 'q':
    driver.quit()
