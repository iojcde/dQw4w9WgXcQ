import psutil, webbrowser,time,pyautogui, os
from multiprocessing import Process
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import numpy as np

os.system('killall firefox')

fig = plt.figure()
ax = plt.axes(xlim=(0, 200), ylim=(0, psutil.virtual_memory().total))
line, = ax.plot([],[])
plt.title("Ram usage")
y_list = deque([-1]*400)
x_list = deque(np.linspace(200,0,num=400))

def init():
    line.set_data([],[])
    return line,


def animate(i):
    y_list.pop()
    y_list.appendleft(psutil.virtual_memory().used)
    line.set_data(x_list,y_list)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                           frames=200, interval=100, blit=True)
def show():
    plt.show()



def main():
    THRESHOLD = 100 * 1024 * 1024  # 100MB

    i = 1
    while True:
        print('ram usage: '+ str(psutil.virtual_memory().percent))



        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        os.system('wmctrl -a firefox')
        time.sleep(3+i*0.2)
        pyautogui.typewrite(' ')
        print(i)

        mem = psutil.virtual_memory()F
        if mem.available <= THRESHOLD:
            print('tested ' + str(i) + ' tabs. exiting now......')
            os.system('killall firefox')

            exit()
        i+=1
p = Process(target = show)
m = Process(target = main)
#p.start()
m.start()