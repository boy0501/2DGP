
class Player:
    UPPER = 6
    LOWER = 7
    def __init__(self,name):
        self.name = name
        self.scores = [0 for i in range(self.UPPER + self.LOWER)]   #13개 카테고리 맨들기
        self.used = [False for i in range(self.UPPER + self.LOWER)]
    
    def setScore(self, score, idx):
        self.scores[idx] = score

    def setAtUsed(self, idx):
        self.used[idx] = True

    def getUpperScore(self):
        sum = 0
        for i in range(self.UPPER):
            sum += self.scores[i]
        return sum
    def getLowerScore(self):
        sum = 0
        for i in range(self.UPPER,self.UPPER + self.LOWER):
            sum += self.scores[i]
        return sum
    def getUsed(self):
        pass
    def getTotalScore(self):
        sum = 0
        for i in range(self.UPPER + self.LOWER):
            sum += self.scores[i]
        return sum
    def toString(self):
        return self.name
    def allLowerUsed(self):             #Lower 카테고리 7개 모두 사용 ?
        for i in range(self.UPPER,self.LOWER+self.UPPER):
            if self.used[i] == False:
                return False
        return True

    def allUpperUsed(self):             #Upper 카테고리 6개 모두 사용? Upper Bonus, score에 사용
        for i in range(self.UPPER):
            if self.used[i] == False:
                return False
        return True