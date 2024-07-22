# time sleep

# csv
#  discard first line
#  konse index pe kya

# for len(readlines)

#   pyautogui index 
#   time sleep 0.08
#   tab
#   after look complletion time sleep 2 second

import pyautogui
import time
import csv

time.sleep(5)
csvfile=open("salaries_corrected.csv","r")
i = 1
for lines in csvfile.readlines():
  print(i)
  lines = lines.split(",")
  try:
    pyautogui.typewrite(lines[0])
  except:
    pyautogui.typewrite("-")
  time.sleep(1)
  pyautogui.press('tab')

  try:
    pyautogui.typewrite(lines[1])
  except:
    pyautogui.typewrite("-")
  time.sleep(1)
  pyautogui.press('tab')
  try:
    pyautogui.typewrite(lines[2])
  except:
    pyautogui.typewrite("-")
  time.sleep(1)
  pyautogui.press('tab')

  try:
    pyautogui.typewrite(lines[3])
  except:
    pyautogui.typewrite("-")
  time.sleep(1)
  pyautogui.press('tab')

  try:
    pyautogui.typewrite(lines[4])
  except:
    pyautogui.typewrite("-")
  time.sleep(1)
  pyautogui.press('tab')

  try:
    pyautogui.typewrite(lines[5])
  except:
    pyautogui.typewrite("-")  
  time.sleep(1)
  pyautogui.press('tab')

  try:
    pyautogui.typewrite(lines[6])
  except:
    pyautogui.typewrite("-")
  time.sleep(1)
  pyautogui.press('tab')

  try:
    pyautogui.typewrite(lines[7])
  except:
    pyautogui.typewrite("-")
  time.sleep(1)
  pyautogui.press('tab')

  try:
    pyautogui.typewrite(lines[8])
  except:
    pyautogui.typewrite("-")
  time.sleep(3)
  pyautogui.press('tab')
  pyautogui.press('tab')
  pyautogui.press('tab')
  pyautogui.press('tab')
  pyautogui.press('tab')
  pyautogui.press('tab')
  pyautogui.press('tab')
  pyautogui.press('tab')
  pyautogui.press('tab')
  pyautogui.press('tab')
  pyautogui.press('enter')
  time.sleep(5)
  # pyautogui.press('tab')
  # time.sleep(3)
  # pyautogui.press('tab')
  # time.sleep(3)
  # pyautogui.press('enter')
  # time.sleep(5)
  i+=1


csvfile.close()