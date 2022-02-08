import pyautogui,time
time.sleep(5)
'''pyautogui.click(470,405)
print("Start Game")'''
score = 0
while True:
    pixel = (pyautogui.pixel(470,405),pyautogui.pixel(542,405),pyautogui.pixel(613,405),pyautogui.pixel(677,405))
    if pixel[0][0] in (0,1):
        pyautogui.click(470,405)
        score += 1
    elif pixel[1][0] in (0,1):
        pyautogui.click(542,405)
        score += 1
    elif pixel[2][0] in (0,1):
        pyautogui.click(613,405)
        score += 1
    elif pixel[3][0] in (0,1):
        pyautogui.click(677,405)
        score += 1
    print(score)