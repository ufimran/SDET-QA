import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\SeleniumWebDrivers\Google Chrome(32bit)\chromedriver.exe")
# driver=webdriver.Chrome() #don't have to give the executeable path if we use this, but we have to copy the drivers in python location "Script" Folder
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")

# driver.implicitly_wait(5) #implicitly wait is applicable for all the elements in the page


driver.maximize_window()
time.sleep(1.0)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a").click() #clicks on the SignUp
time.sleep(1.0)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input").send_keys("Testing Purpose") # Gives First Name
time.sleep(1.0)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input").send_keys("Created") #Gives Sur Name
time.sleep(1.0)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input").send_keys("sdadas@lmail.com") #Gives Email
time.sleep(1.0)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input").send_keys("sdadas@lmail.com") #gives the confirm Email
time.sleep(1.0)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input").send_keys("sdadas@lmail.com") #gives the Password

time.sleep(1.0)
day = Select(driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]"))
day.select_by_visible_text("12")
time.sleep(1.0)
month = Select(driver.find_element(By.NAME, "birthday_month"))
month.select_by_visible_text("Jan")
time.sleep(1.0)
year = Select(driver.find_element(By.NAME, "birthday_year"))
year.select_by_visible_text("1999")

time.sleep(1.0)
driver.find_element(By.XPATH, "//label[text()='Male']").click()

time.sleep(1.0)
driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()

time.sleep(10.0)

act_title = driver.title
exp_title = "Facebook-log in or sign up"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()










