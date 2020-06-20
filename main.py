'''copyright 2020 by JcdeA
    ok please don't judge me by how this is written
    I wasnt really trying my best.
'''
import psutil, webbrowser,time,pyautogui, os
from multiprocessing import Process


os.system('killall firefox')#UNLIMITED POWER!!!!!!!





def main():
    THRESHOLD = 100 * 1024 * 1024  # 100MB

    i = 1
    while True:
        print('ram usage: '+ str(psutil.virtual_memory().percent))



        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')#oh yah
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

m = Process(target = main)


#p.start()
m.start()
