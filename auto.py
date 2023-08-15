import time
import pyautogui

# 送信する文字列
characters = "abcdefghijklmnopqrstuvwxyz."
while True:
	# 1秒ごとに文字を送信
	for char in characters:
    		pyautogui.typewrite(char)
    		# time.sleep(0.1)

