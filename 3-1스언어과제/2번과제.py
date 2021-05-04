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
x1 = math.radians(35.1768201)       #광주
y1 = math.radians(126.7735892)
x2 = math.radians(35.1645701)       #부산
y2 = math.radians(129.0015892)
gangx = math.radians(37.7637326)    #강원도
gangy = math.radians(128.8824475)
seoulx = math.radians(37.565289)    #서울
seouly = math.radians(126.8491259)
d1 = 6370.01 * math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))#광주 부산
d2 = 6370.01 * math.acos(math.sin(x2)*math.sin(gangx)+math.cos(x2)*math.cos(gangx)*math.cos(y2-gangy))#부산 강원
d3 = 6370.01 * math.acos(math.sin(gangx)*math.sin(seoulx)+math.cos(gangx)*math.cos(seoulx)*math.cos(gangy-seouly))#강원 서울
d4 = 6370.01 * math.acos(math.sin(x1)*math.sin(seoulx)+math.cos(x1)*math.cos(seoulx)*math.cos(y1-seouly))#서울 광주
#123 삼각하나 , 143삼각하나
s1 = (d1+d2+d3)/2
s2 = (d1+d3+d4)/2
area1 = (s1*(s1-d1)*(s1-d2)*(s1-d3))**0.5
area2 = (s2*(s2-d1)*(s2-d4)*(s2-d3))**0.5
res = area1+area2
print("추정넓이 :{0}".format(res))

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
print("원천징수세(20.0%):",time*pay*tax)
print("주민세(9.0%):",time*pay*realtax)
print("총공제:",time*pay*tax+time*pay*realtax)
print("공제 후 급여 :",time*pay -(time*pay*tax+time*pay*realtax))

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

print("#11번")
lst  =  [30, 1, 12, 14,10,0]
print("lst 원소개수 :{0},첫번째 원소의 인덱스 {1},마지막 원소의 인덱스{2},lst[2]의 값:{3},lst[-2]의 값:{4}",len(lst),0,-1,lst[2],lst[-2])

print("#12번")
import random
lst  =  [30, 1, 2, 1,0]
lst.append(40)
lst.insert(1, 43)
lst.extend([1, 43])
lst.pop(1)
lst.pop()
lst.sort()
lst.reverse()
random.shuffle(lst)
print(lst)

print("#13번")
lst  =  [30, 1, 2, 1,0]
print(lst.index(1))
print(lst.count(1))
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))

print("#14번")
list1 = [30, 1, 2, 1, 0]
list2 = [1, 21, 13]
print(list1 + list2)
print(2 * list1)
print(list2 * 2)
print(list1[1 : 3])
print(list1[3])

print("#15번")
lst = [eval(i) for i in input("정수를 입력하세요 제일 작은걸 보여드립니다.").split()]
def indexOfSmallestElement(lst):
    index = 0 
    value = lst[0]
    for i in range(1,len(lst)):
        if value>lst[i]:
            index = i
            value = lst[i]
    return index
index = indexOfSmallestElement(lst)
print("가장작은거:",index)

print("#16번")
def isSorted(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True

lst = [eval(i) for i in input("정수를 입력하세요 정렬됐는지 아닌지를 알려드립니다..").split()]

if isSorted(lst):
    print("정렬되어있음")
else:
    print("정렬안됨")

lst = [eval(i) for i in input("정수를 입력하세요 정렬됐는지 아닌지를 알려드립니다..").split()]

if isSorted(lst):
    print("정렬되어있음")
else:
    print("정렬안됨")

print("#17번")
import random
ball = eval(input("떨어뜨릴 공의 개수:"))
hole = eval(input("콩 기계의 슬롯 개수:"))
slots = [0] * hole
for i in range(ball):
    cntR = 0
    for j in range(hole-1):
        if random.randint(0,1):
            print("R",end="")
            cntR += 1
        else :
            print("L",end="")
    slots[cntR] += 1
    print("")    
M = max(slots)
for i in range(M,0,-1):
    for j in range(hole):
        if slots[j] >= i:
            print("0",end="")
        else:
            print("@",end="")
    print("")



print("#18번")

row1 = [eval(i) for i in input("3x4 행렬의 0번째 행:").split()]
row2 = [eval(i) for i in input("3x4 행렬의 1번째 행:").split()]
row3 = [eval(i) for i in input("3x4 행렬의 2번째 행:").split()]
row = [row1,row2,row3]

def sumColumn(m,columnIndex):
    j = 0
    res = 0
    for i in range(3):
        res += m[i][columnIndex]
    return res

print("0번원소 합 :",sumColumn(row,0))
print("1번원소 합 :",sumColumn(row,1))
print("2번원소 합 :",sumColumn(row,2))
print("3번원소 합 :",sumColumn(row,3))

print("#19번")
res = {}
for i in lst:
    if i not in res:
        res[i] = i
        res[i] = 0
    else:
        res[i] += 1

valuelist = res.values()
for key,val in res.items():
    if val == max(valuelist):
        print(key)

print("#20번")

def sortColumns(m):
    newarr = []
    resarr = []
    j = 0
    for k in range(3):
        for i in m:
            newarr.append(i[j])
        sort33(newarr)
        resarr.insert(j,newarr.copy())
        j+=1
        newarr.clear()
    for i in range(3):
        j = i
        while(j<3):
            if i != j :
                resarr[i][j] , resarr[j][i] = resarr[j][i] , resarr[i][j]
            j+=1
    return resarr
            
            
def sort33(arr):
    for j in range(2):
        for i in range(2):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        

lst = [eval(i) for i in input("3x3행렬을 한 행씩 입력하세요").split()]
lst1 = [eval(i) for i in input().split()]
lst2 = [eval(i) for i in input().split()]

l = [lst,lst1,lst2]
new = sortColumns(l)
print("열 정렬된 리스트는 다음과 같습니다")
for i in range(3):
    print(new[i])

print("#21번")
def getRightmostLowestPoint(points):
    for i in range(len(points)):
        j = i+1
        while(j<len(points)):
            if is_right(points[i],points[j]) == True:
                points[i] , points[j] = points[j], points[i]
            j+=1
    for i in range(len(points)):
        j = i+1
        while(j<len(points)):
            if is_bottom(points[i],points[j]) == True:
                points[i] , points[j] = points[j], points[i]
            j+=1
    return points[-1]
        

def is_right(a,b):
    if (a[0] - b[0]) > 0 : #오른쪽이면 True
        return True
    else:
        return False

def is_bottom(a,b):
    if (a[1] - b[1]) < 0: #아래면 True
        return True
    else:
        return False

lst = [eval(i) for i in input("정수를 입력하세요").split()]
i = 0
mytuplelist = []
while(i<len(lst)):
    mytuplelist.append((lst[i],lst[i+1]))
    i+=2
print("최우측 하단의 점은 {0} 입니다".format(getRightmostLowestPoint(mytuplelist)))
input()