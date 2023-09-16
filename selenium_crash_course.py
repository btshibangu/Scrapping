from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# options = webdriver.FirefoxOptions()
# options.add_argument('-headless')
# options.add_argument('-no-sandbox')
# options.add_argument('-disable-dev-shm-usage')

# driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()



driver.get("https://www.amazon.fr")

# cookie = driver.find_element(By.ID, 'sp-cc-rejectall-link')
cookie = driver.find_element(By.XPATH, "//a[@id='sp-cc-rejectall-link']")
cookie.click()
