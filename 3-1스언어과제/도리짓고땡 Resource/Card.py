class Card:
    def __init__(self,temp):#렌덤 넘버0..39 값을 입력받아서 카드 객체 생성
        self.value = temp//4 + 1 # 1~10 카드숫자 
        self.x = temp % 4 + 1# 1~4 카드 무늬 결정

    def getValue(self): 
        return self.value

    #def getsuit(self): #카드 무늬 결정
    #    if self.x==0:
    #        self.suit = "Clubs"
    #    elif self.x==1:
    #        self.suit = "Spades"
    #    elif self.x == 2:
    #        self.suit = "Hearts"
    #    else:
    #        self.suit = "Diamonds"
    #    return self.suit
    def filename(self): #카드 이미지 파일 이름  카드숫자.카드문양.png
        return str(self.value)+"."+str(self.x)+".gif"