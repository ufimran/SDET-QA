# Test Case
# -----------------------
# 1. Open web browser
# 2. Open URL - https://opensource-demo.orangehrmlive.com/
# 3. Provide Email - Admin
# 4. Provide Password - admin123
# 5. Click on login
# 6. Capture title of the dashboard page
# 7. Verify title of the page
# 8. Close browser
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\SeleniumWebDrivers\Google Chrome(32bit)\chromedriver.exe")
# driver=webdriver.Chrome() #don't have to give the executeable path if we use this, but we have to copy the drivers in python location "Script" Folder
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
time.sleep(10)

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()
