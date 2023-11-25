from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import URL, NUM_PAGES
# intialise the webdriver to automatize the use of Chrome
driver = webdriver.Chrome()
# create - if doesn't exist - the link.txt file
with open("link.txt", 'a') as file:
    # navigate among the pages
    for i in range(1,NUM_PAGES+1):
        # starting from the website's URL, update for each page the link
        edit_URL = URL + '?PG=' + str(i)
        driver.get(edit_URL) # navigate to the link
        # use the find_elements(..) to look up for the links, given their class (with 'class' I refer to the HTML attribute)
        elements = driver.find_elements(By.CLASS_NAME,"courseLink")
        # once captured the html code regarding the links,
        # iterate over the elements and write the link on the file
        for e in elements:
            file.write(str(e.get_attribute("href")) + '\n')
# close the webdriver 
driver.quit()