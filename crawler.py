from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import re

driver = webdriver.Chrome(ChromeDriverManager().install())

data = open("data.csv", "a", encoding="utf-8")
data.writelines("tên,giá,thương hiệu,đã bán,sao, số lượng 1 sao,số lượt đánh giá"+"\n")
data.close()

f = open("url.txt", "r")
url = f.readlines()
f.close()

for i in url:
    driver.get(i)
    sleep(0.5)
    for i in range(100):
        actions = ActionChains(driver) 
        actions.send_keys(Keys.DOWN)
        sleep(0.0000000000000000000000000001)
        actions.perform()
    sleep(0.5)
    b = driver.find_elements_by_xpath('//div[contains(@class,"attM6y")]/span')
    c = driver.find_elements_by_xpath('//div[contains(@class,"OitLRu _1mYa1t")]')
    d = driver.find_elements_by_xpath('//div[contains(@class,"aca9MM")]')
    e = driver.find_elements_by_xpath('//div[contains(@class,"Ybrg9j")]')
    thuonghieu = driver.find_elements_by_xpath('//a[contains(@class,"_3Qy6bH")]')
    sao1 = driver.find_elements_by_xpath('//*[contains(text(), "1 Sao")]')
    danhgia = driver.find_elements_by_xpath('//div[contains(@class,"OitLRu")]')
    try:
        ten = b[0].text.replace(",", ".")
    except:
        ten = "none"
    try:
        gia = e[0].text.replace(",", ".")
    except:
        gia = "none"
    try:
        thuonghieu = thuonghieu[0].text.replace(",", ".")
    except:
        thuonghieu = "none"
    try:
        sao = c[0].text.replace(",", ".")
    except:
        sao = "none"
    try:
        daban = d[0].text.replace(",", "").replace("k","00")
    except:
        daban = "0"
    # số lượng 1 sao
    try:
        sao1 = re.search(r"\(([A-Za-z0-9_]+)\)", sao1[0].text).group(1)
    except:
        sao1 = "0"
    #đánh giá
    try:
        danhgia = danhgia[1].text.replace(",", "").replace("k","00")
    except:
        danhgia = "0"

    data = open("data.csv", "a", encoding="utf-8")
    data.writelines(ten +","+ gia + "," + thuonghieu +","+ daban +","+ sao + "," + sao1 +"," + danhgia +"\n")
    data.close()
    
