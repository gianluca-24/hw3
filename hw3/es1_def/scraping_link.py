from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import URL, NUM_PAGES, DIR_PATH
import os
# TODO
driver = webdriver.Chrome()

with open("link2.txt", 'a') as file:
    for i in range(1,1+1):
        edit_URL = URL + '?PG=' + str(i)
        driver.get(edit_URL)
        # path to the new directory /pages/page_i
        path = os.path.join(DIR_PATH, 'page_' + str(i))
        if not os.path.exists(path):
            os.mkdir(path)
        elements = driver.find_elements(By.CLASS_NAME,"courseLink")

        for e in range(len(elements)):
            url = str(elements[e].get_attribute("href"))
            file.write(url + '\n')
            # download
            driver.get(url)
            source = driver.page_source
            course_path = path + '/course_' + str(e) + '.html'
            with open(course_path, "w", encoding="utf-8") as file_html:
                file_html.write(source)
            file_html.close()

file.close()
driver.quit()