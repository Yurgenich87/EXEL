import openpyxl
import pprint as pp
import time
from appium import webdriver
from selenium import webdriver
from typing import Optional
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.options import Options as Op
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


exec_path = r"/Altayka-Doxell/geckodriver.exe"
URL = "https://russianblogs.com/article/44011615734/"
wait_time_out = 15
driver_manager = GeckoDriverManager()
driver_manager.install()
driver = webdriver.Firefox(service=driver_manager.service)
driver.get(URL)

element = W(driver, wait_time_out).until(E.element_to_be_clickable((By.XPATH, "//*[@href='https://russianblogs.com']")))
element.click()

[src="./img/new_design/icons/monitoring_composite_reports.png"]