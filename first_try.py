from selenium.webdriver.chrome import webdriver
import time

driver = webdriver.WebDriver()

driver.get('https://habr.com')

time.sleep(10)

driver.quit()
