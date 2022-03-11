from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import configparser




class Drivers:
    def __init__(self,driver):
       self.driver = driver


    def getDriver():
        return webdriver.Chrome(r"C:/Users/HACI UZDIL/Downloads/chromedriver.exe")


    def getconfig():
        config = configparser.ConfigParser()
        config.read('config.properties')
        return config.get('URLSection', 'url');