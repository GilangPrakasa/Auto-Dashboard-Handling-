from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd
import os
import datetime

# options = webdriver.ChromeOptions()
# options.add_argument('--profile-directory=Profile 1')
# options.add_argument('--user-data-dir=C:\\Users\\eFishery\\AppData\\Local\\Google\\Chrome\\User Data\\')
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dashboard.efishery.com/#/feeders/workshop")
time.sleep(2)

csvdata = pd.read_csv("Dashboard Manufacture eFishery - ID_COBOX.csv", dtype={'ID':str})
df = pd.DataFrame(csvdata)
row = len(df.index)
now = datetime.datetime.now()
waktu = now.strftime("%y/%m/%d %H:%M:%S")

try:
    driver.implicitly_wait(15)
    driver.find_element(By.CSS_SELECTOR, '#lang-loginFormTitle').is_displayed()
    print("Login dulu ya ges")
    email = driver.find_element(By.CSS_SELECTOR, '#loginEmail')
    email.click()
    email.send_keys("manufacture@efishery.com")

    paswd = driver.find_element(By.CSS_SELECTOR, '#loginPassword')
    paswd.click()
    paswd.send_keys("passwordhere")

    time.sleep(1)
    login = driver.find_element(By.CSS_SELECTOR, '#loginSubmit')
    login.click()
    print("Gaskeun Karapyak")
    time.sleep(3)
except:
    print("udah login ini mah aman")

for i in range(0, row):
    idcobox = df.at[df.index[i],'ID']
    print("Process "+idcobox)
    x = i + 1
    i += 1
    log = open("Log.txt", "a")

    try:
        driver.implicitly_wait(15)
        search = driver.find_element(By.CSS_SELECTOR, '#table_workshops_filter > label > input')
        search.click()
        search.send_keys(Keys.CONTROL, 'A')
        search.send_keys(Keys.DELETE)
        search.send_keys("efishery_"+idcobox)
        driver.implicitly_wait(15)
        select = driver.find_element(By.CSS_SELECTOR, '#table_workshops > tbody > tr > td:nth-child(1) > input')
        driver.execute_script("arguments[0].scrollIntoView();",select)
        select.click()
        log.write(str(x)+" COBOX = "+idcobox+"\n")
        print("Success "+idcobox)
        print(" ")
    except:
        log.write(str(x)+" COBOX = "+idcobox+" Not Found\n")
        print(idcobox+" Not Found")
        print(" ")

driver.implicitly_wait(15)
downloadcsv = driver.find_element(By.CSS_SELECTOR, '#table_workshops-download-spec')
downloadcsv.click()

time.sleep(5)

log.write("========Downloaded "+waktu+"========\n")
log.close()
print("DOWNLOAD SUCCESS")

driver.quit()
os._exit(1)

# ==============SYNTAX INPUT ID================
# options = webdriver.ChromeOptions()
# options.add_argument('--profile-directory=Profile 1')
# options.add_argument('--user-data-dir=C:\\Users\\eFishery\\AppData\\Local\\Google\\Chrome\\User Data\\')

# driver = webdriver.Chrome(options=options, use_subprocess=True)
# driver.maximize_window()
# driver.get("https://dashboard.efishery.com/#/feeders/workshop")
# driver.implicitly_wait(20)

# search = driver.find_element(By.CSS_SELECTOR, '#table_workshops_filter > label > input')
# search.send_keys('06A3F')
# driver.implicitly_wait(10)

# detail = driver.find_element(By.CSS_SELECTOR, '#table_workshops > tbody > tr > td:nth-child(10) > button')
# detail.click()
# driver.implicitly_wait(10)

# select = driver.find_element(By.XPATH, '//*[@id="device-feeder-change-status"]')
# select.click()
# driver.implicitly_wait(10)

# status = driver.find_element(By.XPATH,'//*[@id="device-feeder-change-status"]/option[5]')
# status.click()
# driver.implicitly_wait(10)

# yes = driver.find_element(By.CSS_SELECTOR, 'body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button')
# yes.click()
# driver.implicitly_wait(10)
# time.sleep(1)

# oke = driver.find_element(By.CSS_SELECTOR, 'body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button')
# oke.click()
# driver.implicitly_wait(10)
# time.sleep(1)

# top = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/i')
# top.click()
# driver.implicitly_wait(10)
# time.sleep(1)

# search1 = driver.find_element(By.CSS_SELECTOR, '#table_workshops_filter > label > input')
# search1.clear()
# search1.send_keys('well')
# driver.implicitly_wait(20)
# time.sleep(1)

# ==================TEST==================
# csvdata = pd.read_csv("Database.csv", dtype={'ID':str})
# df = pd.DataFrame(csvdata)
# row = len(df.index)

# for i in range(0, row):
#     idcobox = df.at[df.index[i],'ID']
#     print("Process "+idcobox)
#     # =================SYNTAX WEB DRIVER=================
#     time.sleep(1)
#     search = driver.find_element(By.CSS_SELECTOR, '#table_workshops_filter > label > input')
#     search.send_keys(idcobox)
#     driver.implicitly_wait(10)
#     time.sleep(1)
#     search.clear()
#     # =================SYNTAX WEB DRIVER=================
#     x = i + 1
#     i += 1
#     # for x in range(1, row):
#     log = open("Log.txt", "a")
#     log.write(str(x)+" COBOX = "+idcobox+"\n")
#     time.sleep(1)
#     print("Success "+idcobox)
#     print(" ")

# log.write("================\n")
# log.close()