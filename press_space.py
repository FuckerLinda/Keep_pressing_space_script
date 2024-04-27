import time
import random
import pyautogui
import threading
from pynput import keyboard

# 设置屏幕的尺寸，可以根据实际情况调整
screen_width, screen_height = pyautogui.size()

# 模拟鼠标点击函数
def simulate_mouse_click():
    # 生成随机点击的坐标位置
    # x = random.randint(0, screen_width)
    # y = random.randint(0, screen_height)
    
    # 移动鼠标到随机位置并点击
    # pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click()

# 监听键盘输入的线程
def on_press(key):
    try:
        print('字母键： {} 被按下'.format(key.char))
    except AttributeError:
        print('特殊键： {} 被按下'.format(key))

def on_release(key):
    #print('{} 释放了'.format(key))
    if key == keyboard.Key.esc:
        # 释放了esc 键，停止监听并设置Event对象
        stop_clicking.set()
        return False

# 创建一个Event对象用于通信
stop_clicking = threading.Event()
pyautogui.PAUSE=0
click_count = 0
time.sleep(2)
# 开始监听键盘输入的线程
with keyboard.Listener(
        #on_press=on_press,
        on_release=on_release) as listener:

    # 启动模拟点击的线程
    def click_thread():
        global click_count  # 声明全局变量
        while True:
            # 检查是否达到时间限制或者按下了esc键
            if time.time() - start_time > 15 or stop_clicking.is_set():
                break

            # 模拟鼠标点击
            simulate_mouse_click()
            click_count += 1

    click_thread = threading.Thread(target=click_thread)

    # 启动按空格键的线程
    def space_press_thread():
        while True:
            if stop_clicking.is_set():
                break


            pyautogui.press('space')
            

    # 启动按enter键的线程
    def enter_press_thread():
        while True:
            if stop_clicking.is_set():
                break


            pyautogui.press('enter')


    enter_thread = threading.Thread(target=enter_press_thread)
    space_thread = threading.Thread(target=space_press_thread)
    space_thread1 = threading.Thread(target=space_press_thread)
    space_thread2 = threading.Thread(target=space_press_thread)
    space_thread3 = threading.Thread(target=space_press_thread)

    # 启动模拟点击和按空格键的线程
    start_time = time.time()
    #enter_thread.start()
    space_thread.start()
    #space_thread1.start()
    #space_thread2.start()
    #space_thread3.start()
    #click_thread.start()

    # 监听键盘输入
    listener.join()

# 打印模拟点击次数
#print(f"模拟点击了 {click_count} 次")

