import tkinter as tk
import time
import pyautogui
import os, sys
import winsound
from PIL import Image, ImageTk
ISRUN = False
time.sleep(5)
pyautogui.hotkey("win","d")
time.sleep(0.7)
dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(dir)
im = pyautogui.screenshot('desktop.png')
root = tk.Tk()
root.geometry("{}x{}+0+0". format(root.winfo_screenwidth(),
                root.winfo_screenwidth()))
bg = tk.PhotoImage(file="desktop.png")
bgimage = tk.Label(root, image=bg, width=root.winfo_screenwidth(),
                   height=root.winfo_screenheight(), borderwidth=0)
bgimage.place(x=0, y=0)
def toggle_geom():
    pass
def updateImg(number, sleepNum):
    imgName = dir+"/BSOD"+str(number)+".png"
    img = Image.open(imgName).resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    bg1 = ImageTk.PhotoImage(img)
    bgimage.configure(image=bg1, cursor='none')
    bgimage.image = bg1
    root.update()
    time.sleep(sleepNum)
def initiate(e):
    global ISRUN
    if ISRUN == False:
        ISRUN = True
        updateImg(1, 3)
        updateImg(2, 2)
        winsound.PlaySound(dir+'/noise1.wav', winsound.SND_ASYNC)
        updateImg(3, 4)
        winsound.PlaySound(dir + '/noise2.wav', winsound.SND_ASYNC)
        updateImg(4, 3)
        winsound.PlaySound(dir + '/noise13.wav', winsound.SND_ASYNC)
        updateImg(6, 4)
        winsound.PlaySound(dir + '/final.wav', winsound.SND_ASYNC)
        updateImg(7, 2)
        os.system('shutdown /r /t 1')
bgimage.bind('<Button-1>', initiate)
root.attributes("-fullscreen", True)
root.bind('<Escape>', toggle_geom)
root.attributes('-topmost', True)
root.update()
root.mainloop()
