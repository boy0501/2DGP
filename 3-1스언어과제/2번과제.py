print("#1번")
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
x1,y1,x2,y2,x3,y3 = eval(input("삼각형의 세 꼭짓점을 입력하세요:"))
l1 = distance(x1,y1,x2,y2)
l2 = distance(x1,y1,x3,y3)
l3 = distance(x2,y2,x3,y3)
s = (l1+l2+l3)/2
area = (s*(s-l1)*(s-l2)*(s-l3))**0.5
print("삼각형의 넓이:{0:0.1f}".format(area))

print("#2번")
import math
x1,y1 = eval(input("첫번째 점(위도와 경도)을 60분법 각으로 입력하세요:"))
x2,y2 = eval(input("두번째 점(위도와 경도)을 60분법 각으로 입력하세요:"))
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)
d = 6370.01 * math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print("두점 사이의 거리",d)

print("#3번")
x1 = math.radians(35.1768201)
y1 = math.radians(126.7735892)
x2 = math.radians(35.1645701)
y2 = math.radians(129.0015892)
gangx = math.radians(37.7637326)
gangy = math.radians(128.8824475)
seoulx = math.radians(37.565289)
seouly = math.radians(126.8491259)
d = 6370.01 * math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
#덜함

print("#4번")
code = eval(input("ASCII 코드 입력:"))
print("문자는 {0} 입니다.".format(chr(code)))


print("#5번")
import time

res = int(time.time())%25 + ord('A')
print("랜덤 대문자 :{0}".format(chr(res)))



print("#6번")
name = input("사원이름:")
time = eval(input("주 당 근무시간:"))
pay = eval(input("시간 당 급여:"))
tax = eval(input("원천징수 세율:"))
realtax = eval(input("지방세율:"))
print("이름:",name)
print("주당 근무시간:",time)
print("임금:",pay)
print("총 급여:",time*pay)
print("공제:")
print("원천징수세(20.0%):",time*pay*0.2)
#덜함

print("#7번")
List = [eval(i) for i in input("정수 여러개:").split()]
for i in range(len(List)-1,-1,-1):
    print(List[i])

print("#8번")
List = [eval(i) for i in input("1~100사이 정수:").split()]
Dic = {}
for i in List:
    if not i in Dic:
        Dic[i] = List.count(i)
keyList = list(Dic.keys())
keyList.sort()
for k in keyList:
    print("{0} - {1}번 나타납니다".format(k,Dic[k]))
    
print("#9번")
List = [eval(i) for i in input("정수 여러개 주면 평균내고 그위아래:").split()]
aver = sum(List)/len(List)
high=0
low = 0
for i in List:
    if i >= aver:
        high += 1
    else:
        low += 1
print("평균 이상 {0}개 미만{1}개".format(high,low))


print("#10번")
List = [eval(i) for i in input("정수 여러개주면 중복제거:").split()]
l2 = []
for i in List:
    if not i in l2:
        l2.append(i)
print(l2)

    
