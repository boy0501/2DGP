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
import time
class StopWatch:
    def __init__(self):
        self.__startTime = time.time()
        self.__endTime = time.time()
    
    def start(self):
        self.__startTime = time.time()
    def end(self):
        self.__endTime = time.time()
    def getElapsedTime(self):
        return int((self.__endTime - self.__startTime) * 1000 )

d = StopWatch()
a = 0
for i in range(1000000):
    a = a + i
d.end()
print("밀리초 : {0}".format(d.getElapsedTime()))

#5번문제 12.1
class Triangle:
    def __init__(self,s1 = 1.0,s2 = 1.0 ,s3 = 1.0,color ="black",fll = False):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.color = color
        self.fill = fll
    def gets1(self):
        return self.side1
    def sets1(self,s1):
        self.side1 = s1
    def gets2(self):
        return self.side2
    def sets2(self,s2):
        self.side2 = s2
    def gets3(self):
        return self.side3
    def sets3(self,s3):
        self.side3 = s3
    def getArea(self):
        s = (self.side1+self.side2+self.side3)/2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
    def getPerimeter(self):
        return self.side1 + self.side2+self.side3
    def __str__(self):
        return "Triangle: side1 =" + str(self.side1) + "side2 = " + str(self.side2) + "side3 = "+ str(self.side3)

a,b,c = eval(input("변3개 입력 ,로 구분:"))
color = input("색상 입력:")
fll = eval(input("채웠는지 아닌지 구분(0,1)"))
tri = Triangle(a,b,c,color,fll)
print("삼각형의 넓이:{0} 둘레:{1} 색상:{2} 채워져있나?:{3}".format(tri.getArea(),tri.getPerimeter(),tri.color,tri.fill))

#6번문제 13.1
filename = input("파일이름 입력:")
delstr = input("제거할 문자열 입력:")
f = open(filename)
line = f.read()
line = line.replace(delstr,'')
f.close()
f = open(filename,'w')
f.write(line)
f.close()

#7번문제 13.2
filename = input("파일이름 입력:")
f = open(filename)
line = f.read()
f.close()
flist = line.split()
fhang = line.split('\n')
print("문자:",len(line))
print("단어",len(flist))
print("행:",len(fhang))

input()