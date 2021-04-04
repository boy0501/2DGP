#1번문제 7.1

class Rectangle:
    def __init__(self,w=1,h=2):
        self.width = w
        self.height = h
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return self.width*2 + self.height*2


a = Rectangle(4,10)
b = Rectangle(3.5,35.7)
print("a사각형의 폭:{0} 높이:{1} 넓이:{2} 둘레:{3}".format(a.width,a.height,a.getArea(),a.getPerimeter()))
print("b사각형의 폭:{0} 높이:{1} 넓이:{2} 둘레:{3}".format(b.width,b.height,b.getArea(),b.getPerimeter()))

#2번문제 7.2
class Stock:
    def __init__(self,sym,name,pre,cur):
        self.symbol = sym
        self.name = name
        self.__previousClosingPrice = pre
        self.__currentPrice = cur
    def getname(self):
        return self.name
    def getsymbol(self):
        return self.symbol
    def getprev(self):
        return self.__previousClosingPrice
    def setprev(self,pre):
        self.__previousClosingPrice = pre
    def getcur(self):
        return self.__currentPrice
    def setcur(self,cur):
        self.__currentPrice = cur
    def getchangePercent(self):
        return self.__currentPrice / self.__previousClosingPrice * 100 - 100
a = Stock("INTC","intel Corporation",20500,20350)
print("{0}의 가격변동률은 전일{1},금일{2}로 {3:.2f}%변동입니다.".format(a.name,a.getprev(),a.getcur(),a.getchangePercent()))

#3번문제 7.4
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self,spd = SLOW,rad = 5 ,color ="blue",on = False):
        self.__speed = spd
        self.__radius = rad
        self.__color = color
        self.__on = on 
    def getspd(self):
        return self.__speed
    def setspd(self,spd):
        self.__speed = spd
    def getrad(self):
        return self.__radius
    def setrad(self,rad):
        self.__radius = rad
    def getcolor(self):
        return self.__color
    def setcolor(self,color):
        self.__color=color
    def geton(self):
        return self.__on
    def seton(self,onoff):
        self.__on = onoff
    
a = Fan(Fan.FAST,10,"Yellow",True)
b = Fan(Fan.MEDIUM,5,"blue",False)
print("a의 속도:{0}반지름:{1}색상:{2}전원상태:{3}입니다".format(a.getspd(),a.getrad(),a.getcolor(),a.geton()))
print("b의 속도:{0}반지름:{1}색상:{2}전원상태:{3}입니다".format(b.getspd(),b.getrad(),b.getcolor(),b.geton()))

#4번문제 7.8
class StopWatch:
    