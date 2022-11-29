import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\SeleniumWebDrivers\Google Chrome(32bit)\chromedriver.exe")
# driver=webdriver.Chrome() #don't have to give the executeable path if we use this, but we have to copy the drivers in python location "Script" Folder
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

# driver.implicitly_wait(5) #implicitly wait is applicable for all the elements in the page


driver.maximize_window()
time.sleep(1.0)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
time.sleep(1.0)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
time.sleep(1.0)
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
time.sleep(5)

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()