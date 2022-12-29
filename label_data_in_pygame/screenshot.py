import pyautogui
import time
import random
import os



for i in range(10000):
    time.sleep(3)
    im=pyautogui.screenshot()
    name="{}.png".format(random.randint(0,1000000000))
    folder="screenshot"
    path=os.path.join(folder,name)
    print(name)
    im.save(path)
    
    print("saved ",i)