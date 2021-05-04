from tkinter import *
from tkinter.simpledialog import *
class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('사목게임')
        self.matrix = [] # 6x7 2차원 버튼을 담는 2차원 리스트
        self.imageX = PhotoImage(file = "book/pybook/image/x.gif")
        self.imageO = PhotoImage(file = "book/pybook/image/o.gif")
        self.imageE = PhotoImage(file = "book/pybook/image/empty.gif")
        frame = Frame(window)
        frame.pack()
        self.turn  = True #번갈아 가면서 실행할 예정
        for i in range(6):  #6행
            self.matrix.append([])      #[[B,B,B,B,B,B,B],[],[],[],[],[]]
            for j in range(7):  #7열
                self.matrix[i].append(Button(frame,text=' ',image=self.imageE,
                command = lambda col = j:self.pressed(col)))
                self.matrix[i][j].grid(row = i, column = j)
        Button(window,text = '새로시작',command = self.restart).pack()
        
        window.mainloop()
    def restart(self):
        self.turn = True
        for i in range(6):
            for j in range(7):
                self.matrix[i][j]['text'] = ' '
                self.matrix[i][j]['image'] = self.imageE
    def check(self):
        #가로 4개 체크
        for i in range(6):  # i = 0 1 2 3 4 5
            for j in range(4): # j = 0 1 2 3
                if self.matrix[i][j]['text'] != ' ' and\
                self.matrix[i][j]['text'] == self.matrix[i][j+1]['text'] and\
                self.matrix[i][j]['text'] == self.matrix[i][j+2]['text'] and\
                self.matrix[i][j]['text'] == self.matrix[i][j+3]['text']:
                    return True
        #세로 4개 체크
        for i in range(3):  #시작 행 3개 검사
            for j  in range(7): # 모두 검사
                if self.matrix[i][j]['text'] != ' ' and\
                self.matrix[i][j]['text'] == self.matrix[i+1][j]['text'] and\
                self.matrix[i][j]['text'] == self.matrix[i+2][j]['text'] and\
                self.matrix[i][j]['text'] == self.matrix[i+3][j]['text']:
                    return True      
        #대각선 4개 체크 (좌하향)
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j]['text'] != ' ' and\
                self.matrix[i][j]['text'] == self.matrix[i+1][j+1]['text'] and\
                self.matrix[i][j]['text'] == self.matrix[i+2][j+2]['text'] and\
                self.matrix[i][j]['text'] == self.matrix[i+3][j+3]['text']:
                    return True       
        #대각선 4개 체크 (우상향) 
        for i in range(5,-1,-1):
            for j in range(4):
                if self.matrix[i][j]['text'] != ' ' and\
                self.matrix[i][j]['text'] == self.matrix[i-1][j+1]['text'] and\
                self.matrix[i][j]['text'] == self.matrix[i-2][j+2]['text'] and\
                self.matrix[i][j]['text'] == self.matrix[i-3][j+3]['text']:
                    return True               
                 
            

    def pressed(self,col):
        for row in range(5,-1,-1):  #row = 5 4 3 2 1  0
            if self.matrix[row][col]['text'] == ' ':
                if self.turn:
                    self.matrix[row][col]['text'] = 'X'
                    self.matrix[row][col]['image'] = self.imageX
                else:
                    self.matrix[row][col]['text'] = 'O'
                    self.matrix[row][col]['image'] = self.imageO
                if self.check():    #True면 승자가 있음
                    if self.turn:
                        messagebox.showinfo("종료","X 승")
                    else:
                        messagebox.showinfo("종료","O 승")
                    self.restart()
                    break

                self.turn = not self.turn
                break

MainGUI()


        