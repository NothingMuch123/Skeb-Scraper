from selenium import webdriver
import json
import time

# Load config
configFile = open("config.json", "r")
config = json.load(configFile)
configFile.close()
sleepTime = config.get("sleepTime")

# Load selenium
driver = webdriver.Chrome()

# Load website
sort = config.get("sort")
seeking = "&acceptonly=1" if config.get("seeking") else ""
driver.get(f"https://skeb.jp/users?sort={sort}{seeking}")
time.sleep(sleepTime)