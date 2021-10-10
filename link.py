from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
item = []
for i in range(100):
    driver.get("https://shopee.vn/search?keyword=m%E1%BB%B9%20ph%E1%BA%A9m&page="+str(i))
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(0.5)
    for i in range(150):
        actions = ActionChains(driver) 
        actions.send_keys(Keys.DOWN)
        sleep(0.0000000000000000000000000001)
        actions.perform()
    
    for a in driver.find_elements_by_xpath('.//div[contains(@class,"col-xs-2-4 shopee-search-item-result__item")]/a'):
        it = a.get_attribute('href')
        print(it)
        item.append(it)

f = open("url.txt", "a")
for i in item:
    f.writelines(i+"\n")
f.close()
print(len(item))
