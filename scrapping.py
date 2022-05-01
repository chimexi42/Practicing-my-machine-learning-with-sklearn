import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://techwithtim.net')
print(driver.title)

search = driver.find_element(By.NAME,'s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

# print(driver.page_source)

main = driver.find_element(by.ID, 'main')
print(main.text)
# driver.quit()