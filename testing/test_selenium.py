import selenium
from selenium import webdriver

def test_selenium():
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com/")