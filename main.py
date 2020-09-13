
import psutil, webbrowser,time,pyautogui, os
from multiprocessing import Process


os.system('killall firefox')





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

        mem = psutil.virtual_memory()
        if mem.available <= THRESHOLD:
            print('tested ' + str(i) + ' tabs. exiting now......')
            os.system('killall firefox')

            exit()
        i+=1

m = Process(target = main)


#p.start()
m.start()
