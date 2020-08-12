from pyautogui import *
import time

# case 값은 이전/다음의 갯수에 따라 0, 1, 2 중 입력
case = 0
score = 1
def grade(n, case):
    click(x=513, y=375)
    press(['tab', 'enter']) 
    for i in range(1):
        press('down') 
    press(['enter', 'tab', 'tab', 'tab', 'enter'])
    time.sleep(1)
    for i in range(case + 1):
        press('tab')
    press('enter')
grade(score, case)