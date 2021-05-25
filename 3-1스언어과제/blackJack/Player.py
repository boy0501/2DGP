class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0
    def inHand(self):
        return self.N
    def addCard(self,c):
        self.cards.append(c)
        self.N += 1
    def reset(self):
        self.N = 0
        self.cards.clear()
    def value(self):
        sum = 0
        for i in self.cards:
            if i.getValue() == 1:
                if sum + 11 > 21:
                    sum += i.getValue()
                else:
                    sum += 11
            else:
                sum += i.getValue()
        return sum