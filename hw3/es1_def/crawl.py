# create 400 folders, one for each page. In each folder there are the 15 html files downloaded.
import os
from selenium import webdriver
from constants import NUM_PAGES, DIR_PATH
import time

file = open("link.txt", "r")
driver = webdriver.Chrome()
#we close and reopen the browser to avoid error of going too fast, because if we go too fast the network will stop us 
#with a security check and with it we would obtain wrong data
# for i in range(1,NUM_PAGES+1):
for i in range(1,NUM_PAGES+1):
    if i%3==0:
        driver.quit()
        driver = webdriver.Chrome()
    path = os.path.join(DIR_PATH, 'page_' + str(i))
    if not os.path.exists(path):
        os.mkdir(path)
    for x in range(15):

        url = file.readline()
        driver.get(url)
        source = driver.page_source
        course_path = path + '/course_' + str(x) + '.html'
        with open(course_path, "w", encoding="utf-8") as file_html:
            file_html.write(source)
    time.sleep(1)

file.close() 
driver.quit()