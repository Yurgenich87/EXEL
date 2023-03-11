import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.keys import Keys

def open_web_sait_DOXELL():
    """Открывает сайт DOXELL"""
    exec_path = r"E:\PYTHON\chromedriver.exe"
    URL = "https://obr.doxcell.ru:8182/analyzzp/index.jsp"
    wait_time_out = 15
    driver = webdriver.Firefox(executable_path=exec_path)
    driver.get(URL)
    wait_variable = W(driver, wait_time_out)
    input_field = W(driver, 10).until(E.presence_of_element_located((By.NAME, "j_username")))
    input_field.send_keys("gnovokuz")
    input_field = W(driver, 10).until(E.presence_of_element_located((By.NAME, "j_password")))
    input_field.send_keys("WG7RM3")
    input_field.send_keys(Keys.ENTER)
    wait_variable.until(E.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[5]/div[4]/div[1]/table/tbody/tr[1]/td[1]/img[7]"))).click()



def web_page_link_names():
    """Выводит все имена ссылок на заданной веб странице"""
    exec_path = r"/Altayka-Doxell/geckodriver.exe"
    URL = "https://obr.doxcell.ru:8182/analyzzp/index.jsp"
    wait_time_out = 30
    driver = webdriver.Chrome(executable_path=exec_path)
    driver.get(URL)
    wait_variable = W(driver, wait_time_out)
    input_field = W(driver, 20).until(E.presence_of_element_located((By.NAME, "j_username")))
    input_field.send_keys("gnovokuz")
    input_field = W(driver, 20).until(E.presence_of_element_located((By.NAME, "j_password")))
    input_field.send_keys("WG7RM3")
    input_field.send_keys(Keys.ENTER)
    time.sleep(10)
    links = wait_variable.until(E.visibility_of_any_elements_located((By.TAG_NAME, "a")))
    print("The total number of links", len(links))
    for link in links:
        print(link.text)
    input("Нажмите Enter, чтобы закрыть браузер...")
    driver.quit()

def find_the_field_and_enter_the_value():
    """Находим поле для ввода логина и вводим логин"""
    exec_path = r"/Altayka-Doxell/geckodriver.exe"
    wait_time_out = 15
    driver = webdriver.Firefox(executable_path=exec_path)
    wait_variable = W(driver, wait_time_out)
    wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "j_username"))).click()
    input_field = W(driver, 10).until(E.presence_of_element_located((By.NAME, "j_username")))
    input_field.send_keys("gnovokuz")

def button_press():
    """Находим кнопку Sig in и нажимаем её"""
    exec_path = r"/Altayka-Doxell/geckodriver.exe"
    wait_time_out = 15
    driver = webdriver.Firefox(executable_path=exec_path)
    wait_variable = W(driver, wait_time_out)
    wait_variable.until(E.element_to_be_clickable((By.LINK_TEXT, "j_password"))).click()
    input_field = W(driver, 10).until(E.presence_of_element_located((By.NAME, "j_password")))
    input_field.send_keys("WG7RM3")
    input_field.send_keys(Keys.ENTER)

def open_web_sait_TEST():
    """Открывает сайт DOXELL"""
    exec_path = r"/Altayka-Doxell/geckodriver.exe"
    URL = "https://obr.doxcell.ru:8182/analyzzp/index.jsp"
    wait_time_out = 15
    driver = webdriver.Firefox(executable_path=exec_path)
    driver.get(URL)
    wait_variable = W(driver, wait_time_out)
    input_field = W(driver, 10).until(E.presence_of_element_located((By.NAME, "j_username")))
    input_field.send_keys("gnovokuz")
    input_field = W(driver, 10).until(E.presence_of_element_located((By.NAME, "j_password")))
    input_field.send_keys("WG7RM3")
    input_field.send_keys(Keys.ENTER)
    wait_variable.until(E.element_to_be_clickable((By.XPATH, "//html/body/div[3]/div[5]/div[4]/div[1]/table/tbody/tr[1]/td[1]/img[7]"))).click()

# open_web_sait_DOXELL()
web_page_link_names()