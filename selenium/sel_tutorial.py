from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
url = "https://techwithtim.net"
driver.get(url)
print(driver.title)
search = driver.find_element_by_name('s')
search.send_keys("python", Keys.RETURN)
print(driver.page_source)
