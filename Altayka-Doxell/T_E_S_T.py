import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('http://example.com/page.jsp')
element = driver.find_element_by_id('my_element_id')
element.click()
element.send_keys('Hello, world!')
link = driver.find_element_by_link_text('Ссылка на другую страницу')
link.click()
driver.get(link.get_attribute('href'))
frame = driver.find_element_by_name('my_frame_name')
driver.switch_to.frame(frame)
main_window = driver.current_window_handle
new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)
# выполнение действий в новой вкладке
driver.close()
driver.switch_to.window(main_window)