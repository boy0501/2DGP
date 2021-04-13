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
import random
colors = ['red','green','cyan','white','black','orange','blue']
class Ball():
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
        self.dx = 1
        self.dy = 1
        self.spd = 2
        self.color = colors[random.randint(0,6)]


class MainGUI():
    def __init__(self):
        window = Tk()
        window.title('공 옮기기')
        self.width = 400
        self.height = 200
        self.Blist = []
        self.isstop = False
        self.sleeptime = 100
        self.canvas = Canvas(window,width=self.width,height=self.height,bg='white')
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Button(frame,text='정지',command=self.stop).pack(side=LEFT)
        Button(frame,text='재시작',command=self.resume).pack(side=LEFT)
        Button(frame,text='+',command=self.add).pack(side=LEFT)
        Button(frame,text='-',command=self.subtract).pack(side=LEFT)
        Button(frame,text='빠르게',command=self.faster).pack(side=LEFT)
        Button(frame,text='느리게',command=self.slower).pack(side=LEFT)
        self.render()
        window.mainloop()
    def stop(self):
        self.isstop = True
    def resume(self):
        self.isstop = False
        self.render()
    def add(self):
        self.Blist.append(Ball(10,20,5))
    def subtract(self):
        self.Blist.pop()
    def faster(self):
        if self.sleeptime >5:
            self.sleeptime -= 5
    def slower(self):
        self.sleeptime += 5
    def render(self):
        while not self.isstop:
            
            self.canvas.after(self.sleeptime)
            self.canvas.update()
            self.canvas.delete('ball')

            for ball in self.Blist:
                if ball.x >= self.width:
                    ball.dx *= -1
                if ball.x < 0:
                    ball.dx *= -1
                if ball.y >= self.height:
                    ball.dy *= -1
                if ball.y < 0:
                    ball.dy *= -1
                ball.x += ball.dx * ball.spd
                ball.y += ball.dy * ball.spd
                self.canvas.create_oval(ball.x-ball.r,ball.y-ball.r,ball.x+ball.r,ball.y+ball.r,fill=ball.color,tags='ball')

    def logic(self):
        pass
    def inputs(self):
        pass

MainGUI()