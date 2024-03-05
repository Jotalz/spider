from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome(options=chrome_options)
try:
    browser.get('https://www.taobao.com')
    input = browser.find_element(By.CSS_SELECTOR, '.service-bd li')
    # input.send_keys('Python')
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # print(browser.current_url)
    print(input)
    # print(browser.page_source)
finally:
    browser.close()
