from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from TestFramework.Driver.Drivers import Drivers
import jproperties


#driver = webdriver.Chrome(r"C:/Users/HACI UZDIL/Downloads/chromedriver.exe")

driver = Drivers.getDriver()
url =  Drivers.getconfig()



driver.get(url)
time.sleep(3)
driver.maximize_window()
kitap = driver.find_element("/html/body/div[1]/header/div[4]/div[2]/ul[1]/li[1]/a")
kitap.click()
