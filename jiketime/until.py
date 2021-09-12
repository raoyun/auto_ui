from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def get_element(driver,*loc):
    e = driver.find_element(*loc)
    return e

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    sleep(1)

    loc1 = (By.ID,'kw')
    loc2 = (By.ID,'su')

    get_element(driver,*loc1).send_keys('selenium')
    get_element(driver,*loc2).click()

