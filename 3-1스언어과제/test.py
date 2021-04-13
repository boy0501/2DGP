# Round = eval(input())
# high = 0 
# win = 0
# for a in range(Round):
#     row1 = [eval(i) for i in input().split()]
#     if abs(row1[0]-row1[1]>high):
#         high = abs(row1[0]-row1[1])
#         if row1[0]>row1[1]:
#             win = 1
#         else:
#             win = 2
# print("{0}{1}".format(win,high))

from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox

class MainGUI():
    def __init__(self):
        window = Tk()
        window.title = "투자금 계산기"
        frame = Frame(window)
        frame.pack()
        Label(frame,text='투자금').pack(side=LEFT)
        Label(frame,text='투자금').pack(side=LEFT)
        Label(frame,text='투자금').pack(side=LEFT)
        self.text1 = Text(frame,width=22,height=1,wrap=WORD)
        self.text1.pack()
        self.text2 = Text(frame,width=22,height=1,wrap=WORD)
        self.text2.pack()
        self.text3 = Text(frame,width=22,height=1,wrap=WORD)
        self.text3.pack()
        window.mainloop()
MainGUI()