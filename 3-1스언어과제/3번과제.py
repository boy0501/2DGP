#1번문제
a,b,c = eval(input("a,b,c 입력:"))
D = b**2 - 4*a*c

if D<0:
    print('실근이 없음')
elif D == 0:
    r = -b / (2*a)
    print('중근을 가짐, 값은 {0:.2f}'.format(r))
else:
    r1 = (-b + (D **0.5))/(2*a)
    r2 = (-b - (D **0.5))/(2*a)
    print('두개의 실근을 가짐 값은 {0:.2f},{1:.2f}'.format(r1,r2))

#2번문제
import random

listShape = ['스페이드','다이아몬드','하트','크로바']
listNum = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
shape = listShape[random.randint(0,3)]
num = listNum[random.randint(0,12)]
print('당신이 뽑은 카드는 {0} {1}입니다.'.format(shape,num))

#3번문제
x,y = eval(input("x,y 입력:"))
def is_inTriangle(x,y):
    if x < 0:
        return False
    if y < 0:
        return False
    if (-1/2)*x - y + 100 < 0:
        return False
    return True
if is_inTriangle(x,y):
    print("점은 내부에 있습니다.")
else:
    print("점은 내부에 없습니다.")

#4번문제
commission = (5000000*0.08) +(5000000*0.10)
sales = 0
while True :
    if commission + sales * 0.12  > 25000000:
        break
    sales+=100
print("커미션 포함 3천 벌어야 하는 돈은 {0}원 입니다.".format(10000000+sales))

#5번문제
n = 0
for _ in range(1000000):
    x1 = random.random() * 2 - 1
    y1 = random.random() * 2 - 1
    if x1 < 0:
        n += 1
    elif 0<=x1<=1 and 0<=y1<=1:
        if(-x1 + 1 - y1 > 0 ):
            n += 1
print("무작위 점의 홀수번호 안에 생성되는 개수는 : {0}입니다".format(n))


#6번문제



