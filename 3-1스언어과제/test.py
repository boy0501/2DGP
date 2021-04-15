

###########################
# M, T, S, N = [eval(x) for x in input().split()]

# token = 1
# meCha = S
# lst = []

# for x in range(M*T):
#     num = [eval(x) for x in input().split()]
#     lst.append(num)

# new_lst = [lst[i:i+T] for i in range(0, len(lst), T)]

# for x in range(N-1):
#     next_meCha = new_lst[meCha - 1][token - 1][1]
#     next_token = new_lst[meCha - 1][token - 1][0]

#     meCha, token = next_meCha, next_token

# print(meCha)
# s1 = [eval(i) for i in input().split()]
# total = sum(s1)
# m_list = []
# for i in range(total):
#     m_list.append(int(input()))
# m_dict = dict()
# for i in range(total):
#     if m_list[i] not in m_dict:
#         m_dict[m_list[i]] = 1
#     else:
#         m_dict[m_list[i]] += 1
# res_list = []
# for k,v in m_dict.items():
#     if v > 1:
#         res_list.append(k)
# res_list.sort()
# print(len(res_list))
# for i in res_list:
#     print(i)



# N = 6
# a = [[14,38,11,89,-1],[27,34,-1],[27,12,34,-1],[27,-1],[92,2,3,1,-1],[17,2,-1]]

# n_list = list()
# for i in a:
#     n_list.append(i[0])
# a.sort(key= lambda x:x[0])
# m_list = [[]]
# length = 0
# for i in range(len(a)):
#     if i == len(a)-1:
#         break
#     if a[i][0]!= a[i+1][0]:
#         m_list[length].append(a[i])
#         m_list.append([])
#         length+=1
#     else:
#         m_list[length].append(a[i])
# m_list[length].append(a[len(a)-1])
# print(m_list)
# depth = 0
# #깊이를 정함 
# for i in m_list:
#     depth += 1
#     if len(i)<2:
#         continue
#     else:
#         new_node  = [[]]
#         new_node[0].append(i[depth])
# for i in m_list:
#     i.sort(key=lambda x:x[1])
# print(m_list)

from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
from tkinter.simpledialog import *
from random import *



class MainGUI():
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
MainGUI()