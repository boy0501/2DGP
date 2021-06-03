from Card import *

class Configuration:
    configs = ["광땡","땡","끗","망통"]
    madeconfig = ["콩콩팔(1 1 8)","삐리칠(1 2 7)","물삼육(1 3 6)","빽새오(1 4 5)","삥구장(1 9 10)",
    "니니육(2 2 6)","이삼오(2 3 5)","이판장(2 8 10)",
    "심심새(3 3 4)","삼칠장(3 7 10)","삼빡구(3 8 9)",
    "살살이(4 4 2)","사륙장(4 6 10)","사칠구(4 7 9)",
    "꼬꼬장(5 5 10)", "오륙구(5 6 9)","오리발(5 7 8)",
    "쭉쭉팔(6 6 8)",
    "철철육(7 7 6)",
    "팍팍싸(8 8 4)",
    "구구리(9 9 2)",
    "장장장(10 10 10)"
    ]

    def getmadeconfig(cardlist):
        lst = []
        lst.append(cardlist[0].value)
        lst.append(cardlist[1].value)
        lst.append(cardlist[2].value)
        lst.sort()
        if lst[0] == 1 and lst[1] == 1 and lst[2] == 8:
            return Configuration.madeconfig[0]
        if lst[0] == 1 and lst[1] == 2 and lst[2] == 7:
            return Configuration.madeconfig[1]
        if lst[0] == 1 and lst[1] == 3 and lst[2] == 6:
            return Configuration.madeconfig[2]
        if lst[0] == 1 and lst[1] == 4 and lst[2] == 5:
            return Configuration.madeconfig[3]
        if lst[0] == 1 and lst[1] == 9 and lst[2] == 10:
            return Configuration.madeconfig[4]
        if lst[0] == 2 and lst[1] == 2 and lst[2] == 6:
            return Configuration.madeconfig[5]
        if lst[0] == 2 and lst[1] == 3 and lst[2] == 5:
            return Configuration.madeconfig[6]
        if lst[0] == 2 and lst[1] == 8 and lst[2] == 10:
            return Configuration.madeconfig[7]
        if lst[0] == 3 and lst[1] == 3 and lst[2] == 4:
            return Configuration.madeconfig[8]
        if lst[0] == 3 and lst[1] == 7 and lst[2] == 10:
            return Configuration.madeconfig[9]
        if lst[0] == 3 and lst[1] == 8 and lst[2] == 9:
            return Configuration.madeconfig[10]
        if lst[0] == 2 and lst[1] == 4 and lst[2] == 4:
            return Configuration.madeconfig[11]
        if lst[0] == 4 and lst[1] == 6 and lst[2] == 10:
            return Configuration.madeconfig[12]
        if lst[0] == 4 and lst[1] == 7 and lst[2] == 9:
            return Configuration.madeconfig[13]
        if lst[0] == 5 and lst[1] == 5 and lst[2] == 10:
            return Configuration.madeconfig[14]
        if lst[0] == 5 and lst[1] == 6 and lst[2] == 9:
            return Configuration.madeconfig[15]
        if lst[0] == 5 and lst[1] == 7 and lst[2] == 8:
            return Configuration.madeconfig[16]
        if lst[0] == 6 and lst[1] == 6 and lst[2] == 8:
            return Configuration.madeconfig[17]
        if lst[0] == 6 and lst[1] == 7 and lst[2] == 7:
            return Configuration.madeconfig[18]
        if lst[0] == 4 and lst[1] == 8 and lst[2] == 8:
            return Configuration.madeconfig[19]
        if lst[0] == 2 and lst[1] == 9 and lst[2] == 9:
            return Configuration.madeconfig[20]
        if lst[0] == 10 and lst[1] == 10 and lst[2] == 10:
            return Configuration.madeconfig[21]
        return "노메이드"


    def getConfigs(): # 정적 메소드: 객체생성 없이 사용 가능
        return Configuration.configs

    def lightDDang(c):
        a = str(c[0].value) +"." + str(c[0].x)
        b = str(c[1].value) + "." + str(c[1].x)
        if a == "3.1" or a == "8.1" or a == "1.1":
            print("여긴 들어오네")
            if b == "3.1" or b == "8.1" or b == "1.1":
                return 1
        return 0  
    
    def DDang(c):
        if c[0].value == c[1].value:
            return 1
        return 0
    def GGeut(c):
        res = (c[0].value + c[1].value) % 10 
        if res == 0:
            return 0
        else:
            return 1

    def judgement(c):
        if Configuration.lightDDang(c):
            return (3,str(c[0].value) + " " + str(c[1].value) + "광땡")
        if Configuration.DDang(c):
            return  (2,str(c[0].value) + "땡")
        if Configuration.GGeut(c):
            return (1,str((c[0].value + c[1].value) % 10 )+"끗")
        return (0,"망통")

    def score(row, d): # 정적 메소드: 객체생성 없이 사용 가능
#row에 따라 주사위 점수를 계산 반환. 예를 들어, row가 0이면 "Ones"가 채점되어야 함을
# 의미합니다. row가 2이면, "Threes"가 득점되어야 함을 의미합니다. row가 득점 (scored)하지
# 않아야 하는 버튼 (즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우
# -1을 반환합니다.
        if (row>=0 and row<=6):
            return Configuration.scoreUpper(d,row+1)
        elif (row==6 or row == 7):
            return -1
        elif row == 8:
            return Configuration.scoreThreeOfAKind(d)
        elif row == 9:
            return Configuration.scoreFourOfAKind(d)
        elif row == 10:
            return Configuration.scoreFullHouse(d)
        elif row == 11:
            return Configuration.scoreSmallStraight(d)
        elif row == 12:
            return Configuration.scoreLargeStraight(d)
        elif row == 13:
            return Configuration.scoreYahtzee(d)
        elif row == 14:
            return Configuration.sumDie(d)
    def scoreUpper(d, num): # 정적 메소드: 객체생성 없이 사용 가능
        sum = 0
        for i in range(5):
            if d[i].getRoll() == num:
                sum+=num
        return sum

#Upper Section 구성 (Ones, Twos, Threes, ...)에 대해 주사위 점수를 매 깁니다. 예를 들어,
# num이 1이면 "Ones"구성의 주사위 점수를 반환합니다.

    def scoreThreeOfAKind(d):
        dicelist = [0 for i in range(6)]
        cnt = 1
        sum = 0
        for i in range(5):
            dicelist[d[i].getRoll()-1] += 1
            sum += d[i].getRoll()
        for i in dicelist:
            if i >= 3:
                return sum
            cnt += 1
        return 0

    def scoreFourOfAKind(d):
        dicelist = [0 for i in range(6)]
        cnt = 1
        sum = 0
        for i in range(5):
            dicelist[d[i].getRoll()-1] += 1
            sum += d[i].getRoll()
        for i in dicelist:
            if i >= 4:
                return sum
            cnt += 1
        return 0
    def scoreFullHouse(d):
        dicelist = [0 for i in range(6)]
        check2 = False
        check3 = False
        for i in range(5):
            dicelist[d[i].getRoll()-1] += 1
        for i in dicelist:
            if i == 2:
                check2 = True
            if i == 3:
                check3 = True
        if check2 == True and check3 == True:
            return 25
        return 0

        
    def scoreSmallStraight(d):
        dicelist = [0 for i in range(6)]
        check1234 = True
        check2345 = True
        check3456 = True
        for i in range(5):
            dicelist[d[i].getRoll()-1] += 1
        for i in range(4):        
            if dicelist[i] == 0 :
                check1234 = False
            if dicelist[i+1] == 0:
                check2345 = False
            if dicelist[i+2] == 0:
                check3456 = False
        if check1234 == True or check2345 == True or check3456 == True:
            return 30
        return 0
#1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
#1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5

    def scoreLargeStraight(d):
        dicelist = [0 for i in range(6)]
        check12345 = True
        check23456 = True
        for i in range(5):
            dicelist[d[i].getRoll()-1] += 1
        for i in range(5):        
            if dicelist[i] == 0 :
                check12345 = False
            if dicelist[i+1] == 0:
                check23456 = False
        if check12345 == True or check23456 == True:
            return 40
        return 0
    # 1 2 3 4 5 혹은 2 3 4 5 6 검사

    def scoreYahtzee(d):
        dicelist = [0 for i in range(6)]
        cnt = 1
        for i in range(5):
            dicelist[d[i].getRoll()-1] += 1
        for i in dicelist:
            if i == 5:
                return 50
            cnt += 1
        return 0
    def sumDie(d):
        sum = 0
        for i in range(5):
           sum += d[i].getRoll()
        return sum