#1번문제 14.5
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox

def openfile():
    fn = askopenfilename()
    filename.set(fn)
def showresult():
    fn = filename.get()
    fp = open(fn)
    counts=[0]*26
    raw = fp.read()
    raw.lower()
    for ch in raw:
        if ch.isalpha():
            counts[ord(ch.lower())-ord('a')] += 1
    for i in range(26):
        if counts[i]:
            text.insert(END,chr(ord('a')+i)+' - '+str(counts[i])+'번 나타납니다.\n')

window = Tk()
window.title('문자의 출현 빈도수')
frame1 = Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=Y)

text = Text(frame1,width=22,height=20,wrap=WORD,yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)


frame2 = Frame(window)
frame2.pack()
Label(frame2,text="파일명을 입력하세요:").pack(side=LEFT)
filename = StringVar()
Entry(frame2,width=20,textvariable=filename).pack(side=LEFT)
Button(frame2,text="열기",command=openfile).pack(side= LEFT)
Button(frame2,text="결과보기",command=showresult).pack(side = LEFT)





window.mainloop()

#2번무네 14.7
class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('문자 빈도수 히스토그램')
        frame1 = Frame(window)
        frame1.pack()

        self.canvas = Canvas(frame1,width=500,height=200,bg='white')
        self.canvas.pack()
        frame2 = Frame(window)
        frame2.pack()
        Label(frame2,text="파일명을 입력하세요:").pack(side=LEFT)
        self.filename = StringVar()
        Entry(frame2,width=20,textvariable=self.filename).pack(side=LEFT)
        Button(frame2,text="열기",command=self.openfile).pack(side= LEFT)
        Button(frame2,text="결과보기",command=self.showresult).pack(side = LEFT)

        window.mainloop()
    def openfile(self):
        fn = askopenfilename()
        self.filename.set(fn)
    def showresult(self):
        fn = self.filename.get()
        fp = open(fn)
        counts=[0]*26
        raw = fp.read()
        raw.lower()
        for ch in raw:
            if ch.isalpha():
                counts[ord(ch.lower())-ord('a')] += 1
        width = int(self.canvas['width'])
        height = int(self.canvas['height'])
        barWidth = (width - 20) / 26
        maxCount = max(counts)
        for i in range(26):
            self.canvas.create_rectangle(
            i*barWidth+10,
            height-10-counts[i]/maxCount*(height-30),
            (i+1)*barWidth+10,
            height-10
            )
            self.canvas.create_text(
                i*barWidth+10+8,
                height-5,
                text=chr(ord('a')+i)
                )
            self.canvas.create_text(
                i*barWidth+10+8,
                height-20-counts[i]/maxCount*(height-30),
                text=str(counts[i])
                )
            
            

MainGUI()
#3번 공옮기기
class MainGUI():
    def __init__(self):
        window = Tk()
        window.title('공 옮기기')
        self.width = 400
        self.height = 200
        self.x=10
        self.y=20
        self.r=5
        self.canvas = Canvas(window,width=self.width,height=self.height,bg='white')
        self.canvas.pack()
        self.canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill='red',tags='ball')
        frame = Frame(window)
        frame.pack()
        Button(frame,text='상',command=self.up).pack(side=LEFT)
        Button(frame,text='하',command=self.down).pack(side=LEFT)
        Button(frame,text='좌',command=self.left).pack(side=LEFT)
        Button(frame,text='우',command=self.right).pack(side=LEFT)

        window.mainloop()
    def up(self):
        if self.y>5:
            self.y-=5
            self.canvas.delete('ball')
            self.canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill='red',tags='ball')
    def down(self):
        if self.y<395:
            self.y+=5
            self.canvas.delete('ball')
            self.canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill='red',tags='ball')

    def left(self):
        if self.x>5:
            self.x-=5
            self.canvas.delete('ball')
            self.canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill='red',tags='ball')

    def right(self):
        if self.x<self.width-5:
            self.x+=5
            self.canvas.delete('ball')
            self.canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill='red',tags='ball')

MainGUI()
#4번
#5번
#6번
#7번 공튀기기 애니메이션
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