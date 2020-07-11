from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'C:/Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(PATH)
url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)

driver.implicitly_wait(20)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
total_items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]
actions = ActionChains(driver)
actions.click(cookie)
for _ in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in total_items:
        if int(item.text) <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()