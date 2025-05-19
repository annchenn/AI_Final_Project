from selenium import webdriver
import time 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import json
from tqdm import tqdm
import re
import numpy as np

driver = webdriver.Chrome(service=Service())
driver.get('https://timetable.nycu.edu.tw/')           # 打開瀏覽器，開啟網頁
time.sleep(1)
select = Select(driver.find_element("name", "fType"))
button = driver.find_element("id" , "crstime_search")
for op in select.options:
      print(op.text)
      select.select_by_visible_text(op.text)
      # crstime_search
      button.click()
      time.sleep(10)
time.sleep(50)
driver.close()