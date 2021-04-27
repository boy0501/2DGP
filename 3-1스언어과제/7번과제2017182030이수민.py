from tkinter import *
import random
class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('틱택토')
        frame = Frame(window)
        frame.pack()
        self.imageO = PhotoImage(file = "book/pybook/image/o.gif")
        self.imageX = PhotoImage(file = "book/pybook/image/x.gif")
        self.Matrix = []
        for i in range(3):
            self.Matrix.append([])
            for j in range(3):
                if random.randint(0,1):
                    img = self.imageX
                else:
                    img = self.imageO
                self.Matrix[i].append(Label(frame,image=img))
                self.Matrix[i][j].grid(row = i, column = j)
        Button(window,text='다시생성',command=self.refresh).pack()
        window.mainloop()
    def refresh(self):
        for i in range(3):
            for j in range(3):
                if random.randint(0,1):
                    img = self.imageX
                else:
                    img = self.imageO
                self.Matrix[i][j]['image'] = img

#MainGUI()


class MainGUI1:
    def __init__(self):
        window = Tk()
        window.title('틱택토')
        frame = Frame(window)
        frame.pack()
        self.imageO = PhotoImage(file = "book/pybook/image/o.gif")
        self.imageX = PhotoImage(file = "book/pybook/image/x.gif")
        self.imageE = PhotoImage(file = "book/pybook/image/empty.gif")
        self.Matrix = []
        self.turn = True
        self.done = False
        for i in range(3):
            self.Matrix.append([])
            for j in range(3):
                self.Matrix[i].append(Button(frame,image=self.imageE,text = ' ',command = lambda row = i, col = j : self.pressed(row,col)))
                self.Matrix[i][j].grid(row = i, column = j)
        self.explain = StringVar()
        self.explain.set('플레이어 X 차례')
        Label(window,textvariable=self.explain).pack()
        Button(window,text = '다시시작', command=self.refresh).pack()
        
        window.mainloop()
    def pressed(self,row,col):
        if not self.done and self.Matrix[row][col]['text'] == ' ':
            if self.turn :
                self.Matrix[row][col]['image'] = self.imageX
                self.Matrix[row][col]['text'] = 'X'
                if self.check() == '무승부':
                    self.explain.set('무승부')
                elif self.check() != ' ':
                    self.explain.set('{0}승리'.format(self.check()))
                    self.done = True
                else:
                    self.explain.set('플레이어 O 차례')
            else:
                self.Matrix[row][col]['image'] = self.imageO
                self.Matrix[row][col]['text'] = 'O'
                if self.check() == '무승부':
                    self.explain.set('무승부')
                elif self.check() != ' ':
                    self.explain.set('{0}승리'.format(self.check()))
                    self.done = True
                else:
                    self.explain.set('플레이어 X 차례')
            self.turn = not self.turn
    def check(self):    #가로 3 세로 3 대각2줄 검사
        for i in range(3):
            ch = self.Matrix[i][0]['text']
            if ch != ' ' and ch == self.Matrix[i][1]['text'] and ch == self.Matrix[i][2]['text']:
                return ch 
            ch = self.Matrix[0][i]['text']
            if ch != ' ' and ch == self.Matrix[1][i]['text'] and ch == self.Matrix[2][i]['text']:
                return ch
        for i in range(2):
            ch = self.Matrix[1][1]['text']
            if ch != ' ' and ch == self.Matrix[0][0]['text'] and ch == self.Matrix[2][2]['text']:
                return ch
            if ch != ' ' and ch == self.Matrix[0][2]['text'] and ch == self.Matrix[2][0]['text']:
                return ch
        for i in range(3):
            for j in range(3):
                if self.Matrix[i][j]['text'] == ' ':
                    return ' '
        return '무승부'
    def refresh(self):
        self.done = False
        self.turn = True
        self.explain.set('플레이어 X 차례')
        for i in range(3):
            for j in range(3):
                self.Matrix[i][j]['text'] = ' '
                self.Matrix[i][j]['image'] = self.imageE
        

MainGUI1()