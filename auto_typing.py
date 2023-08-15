import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import pyautogui


benesse_url = "https://manabi-gakushu.benesse.ne.jp/gakushu/typing/nihongonyuryoku.html"
driver = webdriver.Chrome()
# driver = webdriver.Chrome('chromedriver')
driver.get(benesse_url)

while True:
    # span 要素の取得
    span_element = driver.find_element(By.ID, "remaining")  # By.ID を使用して要素を取得
    # span 要素内のテキストを取得
    text = span_element.text
    pyautogui.typewrite(text)
