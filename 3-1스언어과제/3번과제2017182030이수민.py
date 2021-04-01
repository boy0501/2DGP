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
def reverse(number):
    num = str(number)
    return num[::-1]


def isPalindrome(number):
    if (str(number) == reverse(number)):
        return True
    else:
        return False
num = eval(input("숫자입력시 대칭수인지 알려드림:"))
if isPalindrome(num):
    print("대칭수네요")
else:
    print("대칭수 아니네요")
#7번문제 6-4
#윗 문제에서 이미 했음
print("345의 역수:{0}",reverse(345))

#8번문제 6-5
def displaySortedNumbers(num1,num2,num3):
    lst = [num1,num2,num3]
    lst.sort()
    return lst
n1,n2,n3 = eval(input("숫자 3개 입력"))
lst = displaySortedNumbers(n1,n2,n3)
print("정렬된 숫자는 {0},{1},{2} 입니다".format(lst[0],lst[1],lst[2]))


#9번문제 6-12
def printChars(ch1,ch2,numberPerLine):
    n = 0
    for i in range(ord(ch1),ord(ch2)+1):
        if n%numberPerLine == 0:
            print()
        print(chr(i),end=' ')
        n+=1
printChars('1','Z',10)

#10번문제 6-13
def m(i):
    res = 0
    for n in range(1,i+1): #n = 1,2,3 ...., i
        res += n/(n+1)
    return res
print("i\tm(i)")
for i in range(1,21):
    print("{0}\t{1:.3f}".format(i,m(i)))
#11번문제 15-3

def gcd(m,n):
    if m%n == 0:
        return n
    else :
        return gcd(n,m%n)
n1,n2 = eval(input("숫자2개 입력시 최대공약수 반환 ,로 구분"))
print(gcd(n1,n2))

#12번문제 15-4
def m1(i):
    if i > 1:
        return 1/i + m(i-1)
    else:
        return 1

print("재귀함수로 만든 m1(10)의 값은 {0}".format(m1(10)))

#13번문제 15-18 
cnt = 0
def moveDisks(n, fromTower, toTower, auxTower):
    global cnt 
    cnt+=1
    if n==1: #정지 조건
        print("디스크 ", n, "을/를 ", fromTower, "에서 ", toTower, "로 옮긴다.")
    else:
        moveDisks(n-1, fromTower, auxTower, toTower)
        print("디스크 ", n, "을/를 ", fromTower, "에서 ", toTower, "로 옮긴다.")
        moveDisks(n-1, auxTower, toTower, fromTower)
       
n = eval(input("디스크의 개수를 입력하세요: "))
#해결 방법을 재귀적으로 찾는다.
print("옮기는 순서는 다음과 같습니다:")
moveDisks(n, 'A', 'B', 'C')
print("옮기고 난 횟수는 {0}".format(cnt))
#14번문제 15-19
n = eval(input("2진수로 변화하고 싶은 10진수 입력: "))
strg = []
def decimalToBinary(value):
    global strg
    strg.append(value%2)
    if value == 1:
        return value
    else:
        value = value//2
        return decimalToBinary(value)

decimalToBinary(n)
strg.reverse()
res =""
for i in strg:
    res += str(i)
print(res)
#15번문제 15-20
n = eval(input("16진수로 변화하고 싶은 10진수 입력: "))
strg =[]
def decimalToHex(value):
    global strg
    res = value % 16
    if res == 10:
        strg.append("A")
    elif res == 11:
        strg.append("B")
    elif res == 12:
        strg.append("C")
    elif res == 13:
        strg.append("D")
    elif res == 14:
        strg.append("E")
    elif res == 15:
        strg.append("F")
    else:
        strg.append(res)
    
    if value < 16:
        return value
    else:
        value = value//16
        return decimalToHex(value)
decimalToHex(n)
strg.reverse()
res = ""
for i in strg:
    res += str(i)
print(res)

input()