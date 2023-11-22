from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import URL, NUM_PAGES

driver = webdriver.Chrome()

with open("link.txt", 'a') as file:
    for i in range(1,NUM_PAGES+1):
        edit_URL = URL + '?PG=' + str(i)
        driver.get(edit_URL)
        elements = driver.find_elements(By.CLASS_NAME,"courseLink")
        for e in elements:
            file.write(str(e.get_attribute("href")) + '\n')
            
driver.quit()