import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.google.com/")
time.sleep(1)                               # 1초 기다리기

search_box = driver.find_element_by_css_selector('.gLFyf.gsfi')
search_box.send_keys("Chromedriver")
search_box.send_keys(Keys.ENTER)            # Keys.RETURN
time.sleep(1)

divs = driver.find_elements_by_css_selector('div#rso>div.g')

for div in divs:
    try:
        title = div.find_element_by_css_selector('.LC20lb.DKV0Md').text 
        contents = div.find_element_by_css_selector('.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc').text

        print(title)
        print(contents)
        print("==================================================")
    except:
        pass
    
driver.close()