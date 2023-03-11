import time
from selenium import webdriver



option = webdriver.ChromeOptions
option.add_argument('--proxy-server=45.158.11:14593')
driver = webdriver.Chrome(options=option)

try:
    driver.get("https://github.com/Yurgenich87?tab=repositories")
    time.sleep(5)
    login_button = driver.find_element("")
    login_input = driver.find_element_by_xpath("/html/body/div[1]/div[6]/main/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[2]/button")
    login_input.clear()
    login_input.send_keys("Yrgenich")
    time.sleep(5)
except Exception as x:
    print(ex)
finally:
    driver.close()
    driver.quit()