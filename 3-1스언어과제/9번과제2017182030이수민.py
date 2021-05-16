import random
from tkinter import *
class MainGUI:
    def __init__(self):
        fp = open('행맨.txt')
        self.words = fp.read().split()
        window = Tk()
        window.title('행맨 게임')
        self.canvas = Canvas(window,bg='white',width=400,height=300)
        self.canvas.pack()
        self.setWord()
        self.DrawHangMen()
        self.canvas.bind('<Key>',self.keyEvent)
        self.canvas.focus_set()
        window.mainloop()
    def setWord(self):
        Idx = random.randint(0,len(self.words)-1)
        self.hiddenWord = self.words[Idx]
        self.guessWord = ['*']*len(self.hiddenWord)
        self.NofCorrect = 0
        self.NofMiss = 0
        self.MissChar = []
        self.donewithWrong = False
        self.donewithCorrect = False
    def DrawHangMen(self):
        self.canvas.delete('hangman')
        self.canvas.create_arc(20,200,20+80,200+40,start = 0 ,extent = 180)
        self.canvas.create_line(20+40,200,20+40,20)
        self.canvas.create_line(20+40,20, 20+40 + 100 ,20)
        if self.donewithWrong:
            self.canvas.create_text(200,250,text = '정답:'+self.hiddenWord,tags = 'hangman')
            self.canvas.create_text(200,265,text='계속하려면 enter',tags = 'hangman')
        elif self.donewithCorrect:
            self.canvas.create_text(200,250,text = '맞았습니다:'+self.hiddenWord,tags = 'hangman')
            self.canvas.create_text(200,265,text='계속하려면 enter',tags = 'hangman')
        else:
            self.canvas.create_text(200,250,text = '단어 추측 :'+ self.toString(self.guessWord),tags = 'hangman')
            if self.NofMiss > 0:
                self.canvas.create_text(200,260,text = '틀린글자'+self.toString(self.MissChar),tags='hangman')
        if self.NofMiss < 1:
            return
        x1 = 20+40+100
        y1 = 20
        x2 = x1
        y2 = y1 + 20
        self.canvas.create_line(x1,y1,x2,y2,tags='hangman')
        if self.NofMiss < 2:
            return
        x3 = x2
        y3 = y2 + 20
        self.canvas.create_oval(x3-20,y3-20,x3+20,y3+20,tags='hangman')
        if self.NofMiss < 3:
            return
        self.canvas.create_line(x3-15,y3+15,x3-50,y3+70,tags='hangman')
        if self.NofMiss < 4:
            return
        self.canvas.create_line(x3+15,y3+15,x3+50,y3+70,tags='hangman')
        if self.NofMiss < 5:
            return
        x4 = x3
        y4 = y3 + 100
        self.canvas.create_line(x3,y3+20,x4,y4,tags='hangman')
        if self.NofMiss < 6:
            return
        self.canvas.create_line(x4,y4,x4-50,y4+100,tags='hangman')
        if self.NofMiss < 7:
            return
        self.canvas.create_line(x4,y4,x4+50,y4+100,tags='hangman')

    def toString(self,wordList):
        result =''
        for ch in wordList:
            result += ch
        return result
    def keyEvent(self,Key):

        if 'a'<= Key.char <= 'z':
            if self.donewithCorrect or self.donewithWrong:
                return
            if Key.char in self.guessWord:
                self.DrawHangMen()
                self.canvas.create_text(200,280,text=Key.char + '는 이미 포함되어 있음',tags = 'hangman')
            elif Key.char not in self.hiddenWord:
                self.NofMiss += 1
                if not Key.char in self.MissChar:
                    self.MissChar.append(Key.char)
                if self.NofMiss == 7:
                    self.donewithWrong = True
                self.DrawHangMen()
                self.canvas.create_text(200,280,text = Key.char +'는 포함되지않음',tags='hangman')
            else:
                for i in range(len(self.hiddenWord)):
                    if self.hiddenWord[i] == Key.char:
                        self.guessWord[i] = Key.char
                        self.NofCorrect += 1
                    if self.NofCorrect == len(self.hiddenWord):
                        self.donewithCorrect = True
                self.DrawHangMen()
                self.canvas.create_text(200,280,text = Key.char +'는 맞았음',tags='hangman')
        elif Key.keycode == 13:
            if self.donewithCorrect or self.donewithWrong:
                self.donewithWrong = False
                self.donewithCorrect = False
                self.NofCorrect = 0
                self.NofMiss = 0
                self.setWord()
                self.DrawHangMen()



MainGUI()