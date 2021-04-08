
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
