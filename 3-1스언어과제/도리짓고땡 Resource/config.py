from dice import *

class Configuration:
    configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes",
    "Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)",
    "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"]
    def getConfigs(): # 정적 메소드: 객체생성 없이 사용 가능
        return Configuration.configs

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