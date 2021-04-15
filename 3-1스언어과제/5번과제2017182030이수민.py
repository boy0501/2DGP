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
class MainGUI2:
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
            
            

MainGUI2()
#3번 공옮기기
class MainGUI3():
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

MainGUI3()
#4번 연이율 계산


class MainGUI4():
    def compute(self):
        mRate = float(self.rate.get())/1200 # 연이율 % -> 월이율 소수점 변환
        f = float(self.money.get()) * (1+mRate)**(float(self.years.get())*12)
        self.futureValue.set(f)
    def __init__(self):
       window = Tk()
       window.title = "투자금 계산기"
       Label(window,text='투자금').grid(row=1,column=1,sticky=W)
       Label(window,text='기간').grid(row=2,column=1,sticky=W)
       Label(window,text='연이율').grid(row=3,column=1,sticky=W)
       Label(window,text='미래가치').grid(row=4,column=1,sticky=W)
       self.money = StringVar()
       Entry(window,textvariable=self.money,justify=RIGHT).grid(row=1,column=2)
       self.years = StringVar()
       Entry(window,textvariable=self.years,justify=RIGHT).grid(row=2,column=2)
       self.rate = StringVar()
       Entry(window,textvariable=self.rate,justify=RIGHT).grid(row=3,column=2)
       self.futureValue = StringVar()
       Label(window,textvariable=self.futureValue).grid(row=4,column=2,sticky=E)

       Button(window,text='계산하기',command=self.compute).grid(row=5,column=2,sticky=E)
       window.mainloop()
MainGUI4()
#5번 라디오 체크버튼
width = 300
height = 50
class MainGUI5():
    def display(self):
        self.canvas.delete('shape')
        if self.filled.get() == 1:
            if self.v.get() == 1:
                self.canvas.create_rectangle(width/2 - width*0.4,height/2-height*0.4,width/2+width*0.4,height/2+height*0.4,tags='shape',fill='red')
            else:
                self.canvas.create_oval(width/2 - width*0.4,height/2-height*0.4,width/2+width*0.4,height/2+height*0.4,tags='shape',fill='red')
        else:
            if self.v.get() == 1:
                self.canvas.create_rectangle(width/2 - width*0.4,height/2-height*0.4,width/2+width*0.4,height/2+height*0.4,tags='shape')
            else:
                self.canvas.create_oval(width/2 - width*0.4,height/2-height*0.4,width/2+width*0.4,height/2+height*0.4,tags='shape')



    def __init__(self):
        window = Tk()
        window.title('라디오버튼과 체크버튼')
        self.canvas = Canvas(window,bg='white',width=width,height=height)
        self.canvas.create_rectangle(width/2 - width*0.4,height/2-height*0.4,width/2+width*0.4,height/2+height*0.4,tags='shape')
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        self.v = IntVar()
        Radiobutton(frame,text='직사각형',variable=self.v,value=1,command=self.display).pack(side=LEFT)
        Radiobutton(frame,text='타원',variable=self.v,value=2,command=self.display).pack(side=LEFT)
        self.filled = IntVar()
        Checkbutton(frame,text='채우기',variable=self.filled,command=self.display).pack(side=LEFT)
        
        window.mainloop()
MainGUI5()
#6번 막대그래프
from random import *

width = 800
height = 600
class MainGUI6():
    def display(self):
        self.canvas.delete('histogram')
        counts=[0]*26
        for i in range(1000):
            ch=randint(0,25)
            counts[ch] += 1
        barWidth = (width-20)/26    #1개 가로길이
        maxCount = int(max(counts))
        for i in range(26):
            self.canvas.create_rectangle(10+i*barWidth,height-(height-10)*counts[i]/maxCount
            ,10+(i+1)*barWidth,height-10,tags='histogram')
            self.canvas.create_text(25+i*barWidth , height-5,text= chr(i+ord('a')),tag='histogram')


    def __init__(self):
        window = Tk()
        window.title('문자의 개수 세기')
        self.canvas = Canvas(window,width=width,height=height,bg='white')
        self.canvas.pack()
        Button(window,text='히스토그램 출력',command=self.display).pack()


        window.mainloop()
MainGUI6()
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


class MainGUI7():
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
        if len(self.Blist) > 0:
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

MainGUI7()
#8번 막대그래프 선형검색 알고리즘 
import tkinter.messagebox
from tkinter.simpledialog import *

width = 800
height = 600
barWidth = (width-20)/20    #1개 가로길이
class MainGUI8():
    def regen(self):
        self.current = 0
        self.canvas.delete('histogram')
        self.counts = [x for x in range(1,21)]
        shuffle(self.counts)
        self.maxCount = int(max(self.counts))
        for i in range(20):
            self.canvas.create_rectangle(10+i*barWidth,height-(height-10)*self.counts[i]/self.maxCount
            ,10+(i+1)*barWidth,height-10,tags='histogram')
            self.canvas.create_text(25+i*barWidth , height-(height-10)*self.counts[i]/self.maxCount + 10,text= self.counts[i],tag='histogram')
    def next(self):
        key = int(self.key.get())
        self.canvas.delete('current_bar')
        self.canvas.create_rectangle(10+self.current *barWidth,height-(height-10)*self.counts[self.current]/self.maxCount
            ,10+(self.current+1)*barWidth,height-10,fill = 'red',tags='current_bar')
        if (key == self.counts[self.current]):
            messagebox.showinfo("이녀석","찾았다 : {0}".format(key))
        else:
            self.current += 1


    def __init__(self):
        window = Tk()
        window.title('선형 검색 애니메이션')
        self.canvas = Canvas(window,width=width,height=height,bg='white')
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Label(frame,text='키를 입력하세요').pack(side=LEFT)
        self.key = IntVar()
        Entry(frame,textvariable=self.key,justify=RIGHT,width=3).pack(side=LEFT)
        Button(window,text='다음단계',command=self.next).pack()
        Button(window,text='재설정',command=self.regen).pack()


        window.mainloop()
MainGUI8()
#9번 막대그래프 선택정렬 알고리즘
width = 800
height = 600
barWidth = (width-20)/20    #1개 가로길이
class MainGUI9():
    def regen(self):
        self.current = 0
        self.canvas.delete('histogram')
        self.counts = [x for x in range(1,21)]
        shuffle(self.counts)
        self.maxCount = int(max(self.counts))
        for i in range(20):
            self.canvas.create_rectangle(10+i*barWidth,height-(height-10)*self.counts[i]/self.maxCount
            ,10+(i+1)*barWidth,height-10,tags='histogram')
            self.canvas.create_text(25+i*barWidth , height-(height-10)*self.counts[i]/self.maxCount + 10,text= self.counts[i],tag='histogram')
    def next(self):
        if self.current < 20:
            indexMin = self.current
            for i in range(self.current+1,20):
                if self.counts[indexMin] > self.counts[i]:
                    indexMin = i
            self.counts[self.current],self.counts[indexMin] = self.counts[indexMin],self.counts[self.current]
        

        self.canvas.delete('current_bar')
        self.canvas.delete('histogram')
        for i in range(20):
            self.canvas.create_rectangle(10+i*barWidth,height-(height-10)*self.counts[i]/self.maxCount
            ,10+(i+1)*barWidth,height-10,tags='histogram')
            self.canvas.create_text(25+i*barWidth , height-(height-10)*self.counts[i]/self.maxCount + 10,text= self.counts[i],tag='histogram')

        self.canvas.create_rectangle(10+self.current *barWidth,height-(height-10)*self.counts[self.current]/self.maxCount
            ,10+(self.current+1)*barWidth,height-10,fill = 'red',tags='current_bar')
        self.current += 1
        print(self.current)
        if self.current == 20:
            messagebox.showinfo("이녀석","정렬 끝났습니당")


    def __init__(self):
        window = Tk()
        window.title('선택 정렬 알고리즘 애니메이션')
        self.canvas = Canvas(window,width=width,height=height,bg='white')
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Button(window,text='다음단계',command=self.next).pack(side=LEFT)
        Button(window,text='재설정',command=self.regen).pack(side=LEFT)


        window.mainloop()
MainGUI9()
#10번 카드게임
class MainGUI10():
    def check(self):
        fourCards = []
        for i in range(4):
            fourCards.append(self.idx[i]%13)
        fourCards.sort()
        fourCards = [x for x in fourCards]
        ex = self.answer.get()
        ex = ex.replace('+',' ')
        ex = ex.replace('-',' ')
        ex = ex.replace('*',' ')
        ex = ex.replace('/',' ')
        ex = ex.replace('(',' ')
        ex = ex.replace(')',' ')
        numbers = ex.split()
        numbers = [eval(x) for x in numbers]
        numbers.sort()
        if fourCards == numbers:
            if eval(self.answer.get()) == 24:
                tkinter.messagebox.showerror("맞음","ㅇㅇ")
            else:
                tkinter.messagebox.showerror("틀림",self.answer.get() + "아님 값틀림")
        else:
            tkinter.messagebox.showerror("틀림","보여지는 카드 사용")


    def regen(self):
        cnt = 0
        while(True):
            rancard = randint(1,51)
            if rancard not in self.idx:
                self.card_list[cnt] = PhotoImage(file = "book/pybook/image/card/"+str(rancard)+".gif")
                self.idx[cnt] = rancard
                cnt += 1
            if cnt == 4:
                break        
        for i in range(4):
            self.LabelList[i]['image'] = self.card_list[i]
    def __init__(self):
        window = Tk()
        window.title('24점 게임')
        self.card_list = []
        self.idx =[]
        cnt = 0
        self.frame1 = Frame(window)
        self.frame1.pack()
        Button(self.frame1,command=self.regen,text="새로고침").pack()
        self.frame2 = Frame(window)
        self.frame2.pack()
        while(True):
            rancard = randint(1,51)
            if rancard not in self.idx:
                self.card_list.append(PhotoImage(file = "book/pybook/image/card/"+str(rancard)+".gif"))
                self.idx.append(rancard)
                cnt += 1
            if cnt == 4:
                break
        self.LabelList = []
        for i in range(4):
            self.LabelList.append(Label(self.frame2,image=self.card_list[i]))
            self.LabelList[i].pack(side=LEFT)
        self.frame3 = Frame(window)
        self.frame3.pack()
        Label(self.frame3,text="수식을 입력하세요:").pack(side=LEFT)
        self.answer = StringVar()
        Entry(self.frame3,textvariable=self.answer).pack(side=LEFT)
        Button(self.frame3,text='확인',command=self.check).pack(side=LEFT)

        window.mainloop()
MainGUI10()