from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# case 값은 이전/다음의 갯수에 따라 0, 1, 2 중 입력
def grade(score, case):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


    for i in range(score):
        keyboard.press(Key.down)
        keyboard.release(Key.down) 
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(1)
    for i in range(case + 1):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

if __name__ == '__main__':
    grade(score=1, case=0)