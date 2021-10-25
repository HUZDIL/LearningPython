from selenium import webdriver
import time



driver  =webdriver.Firefox(executable_path ="c:\\SeleniumChrome\\geckodriver.exe")
driver.get("http:\\www.instagram.com")
time.sleep(2)

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
enter = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
username.click()
time.sleep(2)
username.send_keys("haciuzdil")
time.sleep(2)
password.click()
time.sleep(2)
password.send_keys("123Bll123")
time.sleep(2)
enter.click()
