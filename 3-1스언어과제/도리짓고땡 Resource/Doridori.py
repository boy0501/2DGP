from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random
from itertools import combinations
from config import *

firstbetting = 0
class DoriDori:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dori and Ring")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()  #버튼7
        self.setupLabel()   #라벨5
        self.player = Player("player")
        self.player2 = Player("player")
        self.player3 = Player("player")
        self.dealer = Player("dealer")
        self.betMoney = 0
        self.betMoney2 = 0
        self.betMoney3 = 0
        self.playerMoney = 1000
        self.nCardsDealer = 0       #카드가 놓일 인덱스의 위치
        self.nCardsPlayer = 0
        self.nCardsPlayer2 = 0
        self.nCardsPlayer3 = 0
        self.LcardsPlayer = []      #L = Label 라벨의 리스트임 
        self.LcardsPlayer2 = []      #L = Label 라벨의 리스트임 
        self.LcardsPlayer3 = []      #L = Label 라벨의 리스트임 
        self.LcardsDealer = []
        self.deckN = 0          #카드덱에서 0번째부터 뽑기 (카드덱은 섞여있음)
        self.window.mainloop()
    def setupButton(self):
        self.p1B50 = Button(self.window,text="50", width=3,height=1, font=self.fontstyle2,command=self.pressedB50)
        self.p1B50.place(x=50,y=550)
        self.p1B10 = Button(self.window,text="10", width=3,height=1, font=self.fontstyle2,command=self.pressedB10)
        self.p1B10.place(x=100,y=550)
        self.p1B1 = Button(self.window,text="1", width=3,height=1, font=self.fontstyle2,command=self.pressedB1)
        self.p1B1.place(x=150,y=550)
        self.p2B50 = Button(self.window,text="50", width=3,height=1, font=self.fontstyle2,command=self.pressedB50P2)
        self.p2B50.place(x=250,y=550)
        self.p2B10 = Button(self.window,text="10", width=3,height=1, font=self.fontstyle2,command=self.pressedB10P2)
        self.p2B10.place(x=300,y=550)
        self.p2B1 = Button(self.window,text="1", width=3,height=1, font=self.fontstyle2,command=self.pressedB1P2)
        self.p2B1.place(x=350,y=550)
        self.p3B50 = Button(self.window,text="50", width=3,height=1, font=self.fontstyle2,command=self.pressedB50P3)
        self.p3B50.place(x=450,y=550)
        self.p3B10 = Button(self.window,text="10", width=3,height=1, font=self.fontstyle2,command=self.pressedB10P3)
        self.p3B10.place(x=500,y=550)
        self.p3B1 = Button(self.window,text="1", width=3,height=1, font=self.fontstyle2,command=self.pressedB1P3)
        self.p3B1.place(x=550,y=550)

        self.Deal = Button(self.window,text="Deal", width=6,height=1, font=self.fontstyle2,command=self.pressedDeal)
        self.Deal.place(x=600,y=550)
        self.Again = Button(self.window,text="Again", width=6,height=1, font=self.fontstyle2,command=self.pressedAgain)
        self.Again.place(x=700,y=550)
        self.MoneyButtonDisable()
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'
    def MoneyButtonEnable(self):
        self.p1B50['state'] = 'normal'
        self.p1B50['bg'] = 'white'
        self.p1B10['state'] = 'normal'
        self.p1B10['bg'] = 'white'
        self.p1B1['state'] = 'normal'
        self.p1B1['bg'] = 'white'
        self.p2B50['state'] = 'normal'
        self.p2B50['bg'] = 'white'
        self.p2B10['state'] = 'normal'
        self.p2B10['bg'] = 'white'
        self.p2B1['state'] = 'normal'
        self.p2B1['bg'] = 'white'
        self.p3B50['state'] = 'normal'
        self.p3B50['bg'] = 'white'
        self.p3B10['state'] = 'normal'
        self.p3B10['bg'] = 'white'
        self.p3B1['state'] = 'normal'
        self.p3B1['bg'] = 'white'
    def MoneyButtonDisable(self):
        self.p1B50['state'] = 'disabled'
        self.p1B50['bg'] = 'gray'
        self.p1B10['state'] = 'disabled'
        self.p1B10['bg'] = 'gray'
        self.p1B1['state'] = 'disabled'
        self.p1B1['bg'] = 'gray'
        self.p2B50['state'] = 'disabled'
        self.p2B50['bg'] = 'gray'
        self.p2B10['state'] = 'disabled'
        self.p2B10['bg'] = 'gray'
        self.p2B1['state'] = 'disabled'
        self.p2B1['bg'] = 'gray'
        self.p3B50['state'] = 'disabled'
        self.p3B50['bg'] = 'gray'
        self.p3B10['state'] = 'disabled'
        self.p3B10['bg'] = 'gray'
        self.p3B1['state'] = 'disabled'
        self.p3B1['bg'] = 'gray'




    def setupLabel(self):
        self.LbetMoney = Label(text="$0",width=4,height=1,font=self.fontstyle,bg="green",fg="cyan")
        self.LbetMoney.place(x=40,y=500)
        self.LbetMoney2 = Label(text="$0",width=4,height=1,font=self.fontstyle,bg="green",fg="cyan")
        self.LbetMoney2.place(x=240,y=500)
        self.LbetMoney3 = Label(text="$0",width=4,height=1,font=self.fontstyle,bg="green",fg="cyan")
        self.LbetMoney3.place(x=440,y=500)
        self.LplayerMoney = Label(text="You have $1000",width=15,height=1,font=self.fontstyle,bg="green",fg="cyan")
        self.LplayerMoney.place(x=540,y=500)
        self.LplayerPts = Label(text="",width=2,height=1,font=self.fontstyle2,bg="green",fg="white")
        self.LplayerPts.place(x=50,y=300)
        self.LdealerPts = Label(text="",width=2,height=1,font=self.fontstyle2,bg="green",fg="white")
        self.LdealerPts.place(x=300,y=100)
        self.Lstatus = Label(text="",width=15,height=1,font=self.fontstyle,bg="green",fg="white")
        self.Lstatus.place(x=500,y=300)
        
        self.playermade = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.playermade.place(x=50,y=255)
        self.playervalue = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.playervalue.place(x=50,y=285)
        self.playercardnum = []
        for i in range(5):
            self.playercardnum.append(Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white"))
            self.playercardnum[i].place(x=50+i*30,y=310)
        self.playerwin = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.playerwin.place(x=50,y=225)
        
        self.playermade2 = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.playermade2.place(x=250,y=255)
        self.playervalue2 = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.playervalue2.place(x=250,y=285)
        self.playercardnum2 = []
        for i in range(5):
            self.playercardnum2.append(Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white"))
            self.playercardnum2[i].place(x=250+i*30,y=310)
        self.playerwin2 = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.playerwin2.place(x=250,y=225)

        self.playermade3 = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.playermade3.place(x=450,y=255)
        self.playervalue3 = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.playervalue3.place(x=450,y=285)
        self.playercardnum3 = []
        for i in range(5):
            self.playercardnum3.append(Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white"))
            self.playercardnum3[i].place(x=450+i*30,y=310)
        self.playerwin3 = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.playerwin3.place(x=450,y=225)
        
        self.dealermade = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.dealermade.place(x=450,y=50)
        self.dealervalue = Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white")
        self.dealervalue.place(x=450,y=80)
        self.dealercardnum = []
        for i in range(5):
            self.dealercardnum.append(Label(self.window,text="",font=self.fontstyle2,bg="green",fg="white"))
            self.dealercardnum[i].place(x=250+i*30,y=10)
        
        
    def pressedB50(self):
        self.betMoney += 50
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney -=50
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            #Playsound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 50

    def pressedB10(self):
        self.betMoney += 10
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney -=10
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            #Playsound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 10
    def pressedB1(self):
        self.betMoney += 1
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney -=1
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            #Playsound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 1
    def pressedB50P2(self):
        self.betMoney2 += 50
        if self.betMoney2 <= self.playerMoney:
            self.LbetMoney2.configure(text="$"+str(self.betMoney2))
            self.playerMoney -=50
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            #Playsound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney2 -= 50

    def pressedB10P2(self):
        self.betMoney2 += 10
        if self.betMoney2 <= self.playerMoney:
            self.LbetMoney2.configure(text="$"+str(self.betMoney2))
            self.playerMoney -=10
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            #Playsound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney2 -= 10
    def pressedB1P2(self):
        self.betMoney2 += 1
        if self.betMoney2 <= self.playerMoney:
            self.LbetMoney2.configure(text="$"+str(self.betMoney2))
            self.playerMoney -=1
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            #Playsound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney2 -= 1
    def pressedB50P3(self):
        self.betMoney3 += 50
        if self.betMoney3 <= self.playerMoney:
            self.LbetMoney3.configure(text="$"+str(self.betMoney3))
            self.playerMoney -=50
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            #Playsound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney3 -= 50

    def pressedB10P3(self):
        self.betMoney3 += 10
        if self.betMoney3 <= self.playerMoney:
            self.LbetMoney3.configure(text="$"+str(self.betMoney3))
            self.playerMoney -=10
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            #Playsound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney3 -= 10
    def pressedB1P3(self):
        self.betMoney3 += 1
        if self.betMoney3 <= self.playerMoney:
            self.LbetMoney3.configure(text="$"+str(self.betMoney3))
            self.playerMoney -=1
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            #Playsound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney3 -= 1




    def pressedStay(self):
        self.checkWinner()
        
    def pressedDeal(self):
        self.MoneyButtonEnable()
        self.Deal['state']='disable'
        self.Deal['bg'] = 'gray'
        self.deal()
        #카드 두장 뿌려주고
        #플레이어 점수 보여준다음
        #stay again normal / deal은 disable 시킴 버튼을 

    def pressedAgain(self):
        global firstbetting
        for i in self.LcardsPlayer:
            i.place_forget()
        for i in self.LcardsPlayer2:
            i.place_forget()
        for i in self.LcardsPlayer3:
            i.place_forget()
        for i in self.LcardsDealer:
            i.place_forget()
        self.LplayerPts.configure(text="")
        self.LdealerPts.configure(text="")
        self.Lstatus.configure(text="")
        self.playermade.configure(text="")
        self.playervalue.configure(text="")
        self.playermade2.configure(text="")
        self.playervalue2.configure(text="")
        self.playermade3.configure(text="")
        self.playervalue3.configure(text="")
        self.dealermade.configure(text="")
        self.dealervalue.configure(text="")
        self.playerwin.configure(text="")
        self.playerwin2.configure(text="")
        self.playerwin3.configure(text="")
        for i in range(5):
            self.playercardnum[i].configure(text="",fg="white")
            self.playercardnum2[i].configure(text="",fg="white")
            self.playercardnum3[i].configure(text="",fg="white")
            self.dealercardnum[i].configure(text="",fg="white")
        self.LcardsDealer.clear()
        self.LcardsPlayer.clear()
        self.LcardsPlayer2.clear()
        self.LcardsPlayer3.clear()
        self.betMoney = 0
        self.betMoney2 = 0
        self.betMoney3 = 0
        self.deckN = 0
        self.nCardsPlayer = 0
        self.nCardsPlayer2 = 0
        self.nCardsPlayer3 = 0
        self.nCardsDealer = 0
        self.MoneyButtonDisable()
        self.Deal['state'] = 'normal'
        self.Deal['bg'] = 'white'
        self.Again['state'] = "disabled"
        self.Again['bg'] = 'gray'
        firstbetting = 0

    def deal(self):
        global firstbetting
        if firstbetting == 0:
            self.player.reset()
            self.player2.reset()
            self.player3.reset()
            self.dealer.reset() #카드 덱 40장 셔플링 0,1,,.39
            self.cardDeck = [i for i in range(40)]
            random.shuffle(self.cardDeck)
            self.deckN =0
            self.hitPlayer(0)
            self.hitDealerDown(0)
            self.nCardsPlayer = 1
            self.nCardsDealer = 0
            firstbetting += 1
            #Playsound('sounds/cardFlip1.wav', SND_FILENAME)
        elif firstbetting == 1:
            self.hitPlayer(1)
            self.hitPlayer(2)
            self.hitPlayer(3)
            self.hitDealerDown(1)
            self.hitDealerDown(2)
            self.hitDealerDown(3)
            firstbetting += 1
            #Playsound('sounds/cardFlip1.wav', SND_FILENAME)
        else:
            self.hitPlayer(4)
            self.hitDealerDown(4)

            self.checkWinner()
            


    def hitPlayer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file="GodoriCards/"+newCard.filename())
        self.LcardsPlayer.append(Label(self.window,image=p))
        #파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=50+n*30,y=350)
        self.playercardnum[n].configure(text=str(newCard.getValue()))

        
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player2.addCard(newCard)
        p = PhotoImage(file="GodoriCards/"+newCard.filename())
        self.LcardsPlayer2.append(Label(self.window,image=p))
        ##파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer2[self.player2.inHand() - 1].image = p
        self.LcardsPlayer2[self.player2.inHand() - 1].place(x=250+n*30,y=350)
        self.playercardnum2[n].configure(text=str(newCard.getValue()))

        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player3.addCard(newCard)
        p = PhotoImage(file="GodoriCards/"+newCard.filename())
        self.LcardsPlayer3.append(Label(self.window,image=p))
        ##파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer3[self.player3.inHand() - 1].image = p
        self.LcardsPlayer3[self.player3.inHand() - 1].place(x=450+n*30,y=350)
        self.playercardnum3[n].configure(text=str(newCard.getValue()))


    def hitDealerDown(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="GodoriCards/cardback.gif")
        self.LcardsDealer.append(Label(self.window,image=p))
        #파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=250+n*30,y=50)
        #self.LdealerPts.configure(text=str(self.dealer.value()))

    def hitDealer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="GodoriCards/"+newCard.filename())
        self.LcardsDealer.append(Label(self.window,image=p))
        #파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=280+n*30,y=150)
        #Playsound('sounds/cardFlip1.wav', SND_FILENAME)
    
    def pressedHit(self):
        self.nCardsPlayer += 1
        self.hitPlayer(self.nCardsPlayer)
        if self.player.value() > 21:
            self.checkWinner()

    def checkWinner(self):
        self.Again['state']='normal'
        self.Again['bg']='white'
        #뒤집힌 카드 그리기 
        p = PhotoImage(file="GodoriCards/"+self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image = p) #이미지 레퍼런스 변경
        self.LcardsDealer[0].image=p#파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        p = PhotoImage(file="GodoriCards/"+self.dealer.cards[1].filename())
        self.LcardsDealer[1].configure(image = p) #이미지 레퍼런스 변경
        self.LcardsDealer[1].image=p#파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        p = PhotoImage(file="GodoriCards/"+self.dealer.cards[2].filename())
        self.LcardsDealer[2].configure(image = p) #이미지 레퍼런스 변경
        self.LcardsDealer[2].image=p#파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        p = PhotoImage(file="GodoriCards/"+self.dealer.cards[3].filename())
        self.LcardsDealer[3].configure(image = p) #이미지 레퍼런스 변경
        self.LcardsDealer[3].image=p#파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        p = PhotoImage(file="GodoriCards/"+self.dealer.cards[4].filename())
        self.LcardsDealer[4].configure(image = p) #이미지 레퍼런스 변경
        self.LcardsDealer[4].image=p#파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        for i in range(5):
            self.dealercardnum[i].configure(text=str(self.dealer.cards[i].getValue()))
        #카드 그리기 끝 
        self.compareWin()

        self.betMoney = 0
        self.betMoney2 = 0
        self.betMoney3 = 0
        self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
        self.LbetMoney.configure(text="$"+str(self.betMoney))
        self.LbetMoney2.configure(text="$"+str(self.betMoney2))
        self.LbetMoney3.configure(text="$"+str(self.betMoney3))
        self.MoneyButtonDisable()
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

    def compareWin(self):
        playerhigh = []
        playerhighmade = []
        playerhigh2 = []
        playerhighmade2 = []
        playerhigh3 = []
        playerhighmade3 = []
        dealerhigh = []
        dealerhighmade = []

        for i in combinations(self.player.cards, 3):
            if (i[0].value+i[1].value+i[2].value) % 10 == 0:
                namozi = []
                for j in self.player.cards:
                    if j not in i:
                        namozi.append(j)
                
                playerhighmade.append(i)
                playerhigh.append(Configuration.judgement(namozi))

        for i in combinations(self.player2.cards, 3):
            if (i[0].value+i[1].value+i[2].value) % 10 == 0:
                namozi = []
                for j in self.player2.cards:
                    if j not in i:
                        namozi.append(j)
                playerhighmade2.append(i)
                playerhigh2.append(Configuration.judgement(namozi))

        for i in combinations(self.player3.cards, 3):
            if (i[0].value+i[1].value+i[2].value) % 10 == 0:
                namozi = []
                for j in self.player3.cards:
                    if j not in i:
                        namozi.append(j)

                playerhighmade3.append(i)
                playerhigh3.append(Configuration.judgement(namozi))


        for i in combinations(self.dealer.cards, 3):
            idx = 0
            if (i[0].value+i[1].value+i[2].value) % 10 == 0:
                namozi = []
                for j in self.dealer.cards:
                    if j not in i:
                        namozi.append(j)
                dealerhigh.append(Configuration.judgement(namozi))
                dealerhighmade.append(i)



        p1 = None
        p1v = None
        p2 = None
        p2v = None
        p3 = None
        p3v = None
        d = None
        dv = None


        if playerhigh:
            p1 = Configuration.getmadeconfig(playerhighmade[playerhigh.index(max(playerhigh))])
            p1v = max(playerhigh)
            self.playermade.configure(text=p1)
            self.playervalue.configure(text=p1v[1])
            for i in range(3):
                indx = self.player.cards.index(playerhighmade[playerhigh.index(max(playerhigh))][i])
                self.LcardsPlayer[indx].place(x=50+indx*30,y=370)
                self.playercardnum[indx].configure(fg="yellow")
            #Label(self.window,text=p1,font=self.fontstyle2,bg="green",fg="white").place(x=50,y=255)
            #Label(self.window,text=p1v,font=self.fontstyle2,bg="green",fg="white").place(x=50,y=285)
            print("플레이어 1의 메이드:",p1)
            print("플레이어 1의 값",p1v[1])
        else:
            self.playervalue.configure(text="노메이드")

        if playerhigh2:
            p2 = Configuration.getmadeconfig(playerhighmade2[playerhigh2.index(max(playerhigh2))])
            p2v = max(playerhigh2)
            self.playermade2.configure(text=p2)
            self.playervalue2.configure(text=p2v[1])
            for i in range(3):
                indx = self.player2.cards.index(playerhighmade2[playerhigh2.index(max(playerhigh2))][i])
                self.LcardsPlayer2[indx].place(x=250+indx*30,y=370)
                self.playercardnum2[indx].configure(fg="yellow")
            #Label(self.window,text=p2,font=self.fontstyle2,bg="green",fg="white").place(x=250,y=255)
            #Label(self.window,text=p2v,font=self.fontstyle2,bg="green",fg="white").place(x=250,y=285)
            print("플레이어 2의 메이드:",p2)
            print("플레이어 2의 값",p2v[1])
        else:
            self.playervalue2.configure(text="노메이드")

        if playerhigh3:
            p3 = Configuration.getmadeconfig(playerhighmade3[playerhigh3.index(max(playerhigh3))])
            p3v = max(playerhigh3)
            self.playermade3.configure(text=p3)
            self.playervalue3.configure(text=p3v[1])
            for i in range(3):
                indx = self.player3.cards.index(playerhighmade3[playerhigh3.index(max(playerhigh3))][i])
                self.LcardsPlayer3[indx].place(x=450+indx*30,y=370)
                self.playercardnum3[indx].configure(fg="yellow")
            #Label(self.window,text=p3,font=self.fontstyle2,bg="green",fg="white").place(x=450,y=255)
            #Label(self.window,text=p3v,font=self.fontstyle2,bg="green",fg="white").place(x=450,y=285)
            print("플레이어 3의 메이드:",p3)
            print("플레이어 3의 값",p3v[1])
        else:
            self.playervalue3.configure(text="노메이드")

        if dealerhigh:
            d = Configuration.getmadeconfig(dealerhighmade[dealerhigh.index(max(dealerhigh))])
            dv = max(dealerhigh)
            self.dealermade.configure(text=d)
            self.dealervalue.configure(text=dv[1])
            for i in range(3):
                indx = self.dealer.cards.index(dealerhighmade[dealerhigh.index(max(dealerhigh))][i])
                self.LcardsDealer[indx].place(x=250+indx*30,y=70)
                self.dealercardnum[indx].configure(fg="yellow")
            #Label(self.window,text=d,font=self.fontstyle2,bg="green",fg="white").place(x=450,y=50)
            #Label(self.window,text=dv,font=self.fontstyle2,bg="green",fg="white").place(x=450,y=80)
            print("딜러의 메이드:",d)
            print("딜러의 값",dv[1])
        else:
            self.dealervalue.configure(text="노메이드")
            #Label(self.window,text="노메이드",font=self.fontstyle2,bg="green",fg="white").place(x=450,y=80)

        winplayeris = False
        if self.isWin(p1v,dv):
            self.playerwin.configure(text="승")
            self.playerMoney += self.betMoney*2
            winplayeris = True
        else:
            self.playerwin.configure(text="패")

        if self.isWin(p2v,dv):
            self.playerwin2.configure(text="승")
            self.playerMoney += self.betMoney2*2
            winplayeris = True
        else:
            self.playerwin2.configure(text="패")


        if self.isWin(p3v,dv):
            self.playerwin3.configure(text="승")
            self.playerMoney += self.betMoney3*2
            winplayeris = True
        else:
            self.playerwin3.configure(text="패")

        if winplayeris == True:
            pass#Playsound('sounds/win.wav', SND_FILENAME)
        else:
            pass#Playsound('sounds/wrong.wav', SND_FILENAME)
            


        print("한 판 끝")
        
    def isWin(self,player,dealer):
        if player == None:              #플레이어 노메이드
            return 0

        if dealer == None:              #딜러 노메이드 (위에서 플레이어가 노메이드인 경우는 처리)
            return 1

        if dealer[0] > player[0]:       #족보가 낮으면
            return 0

        if dealer[0] < player[0]:       #족보가 높으면
            return 1
        
        if dealer[1] < player[1]:       #족보가 같을때 끝,땡 이 높다면
            return 1
        
        return 0                        #나머지


        








DoriDori()