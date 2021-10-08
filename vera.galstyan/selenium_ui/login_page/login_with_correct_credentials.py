#This test case was created by Vera Galstyan

#!/usr/bin/env python 3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_driver = webdriver.Chrome("executable_path https://www.saucedemo.com/inventory.html")
chrome_driver.get("https://www.saucedemo.com/inventory.html")
