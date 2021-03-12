print("#1번")
width = 4.5
height = 7.9
rect_area = int(width * height*100)/100
rect_perimeter = 2 * (width + height)
print(rect_area,rect_perimeter)

print("#2번")
time = (45 * 60 + 30)/3600
mile = 14 / 1.6
mileperhour = int(mile/time*100)/100
print(mileperhour)
print("{0:.2f}",format(mileperhour))

print("#3번")
birth = 365*24*3600//7
death = 365*24*3600//13
migrate = 365*24*3600//45
person = 312032486
for a in range(5):
    person = person+ birth - death + migrate
    print(person)

print("#4번")
pound = eval(input("파운드값 입력:"))
kilo = pound * 0.454
print("{0:.2f} 파운드는 {1:.2f} 킬로그램".format(pound,kilo))

print("#5번")
subtotal,rate = eval(input("소계와 팁 비율 입력:"))
tip = subtotal * rate / 100
total = subtotal + tip
print("팁은 {0:.2f} 총액은 {1:.2f}".format(tip,total))

print("#6번")
number = eval(input("0~1000사이 숫자입력:"))
result = 0
while number:
    result = result + number % 10
    number = number // 10
print(result)

print("#7번")
min = eval(input("분에대한 숫자 입력:"))
hour = min / 60
day = hour / 24 % 365
year = hour // 24 //365
print("{0:.0f}년 {1:.0f}일 입니다".format(year,day))

print("#8번")
tempur = eval(input("화씨 -58f 와 41f 사이의 온도를 입 력하세요:"))
wind = eval(input("풍속을 시간 당 마일 단위로 입력하세요:"))
tem = 35.74 + 0.6215 * tempur - 35.75 * wind **0.16 + 0.4275 *tempur * wind **0.16
print("{0:.5f} 는 체감온도입니다.".format(tem))

print("#9번")
money = eval(input("약정 금액을 입력하세요:"))
rate = eval(input("연이율(%)을 입력하세요:"))
year = eval(input("약정 기간(년) 을 입력하세요:"))
result = money / ((1+rate/12/100) ** (year*12))
print("월 납입금은 {0:.5f} 입니다.".format(result))

print("#10번")
pound = eval(input("몸무게를 파운드로 입력하세요:"))
inch = eval(input("키를 인치로 입력하세요:"))
kg = pound * 0.4539237
m = inch * 0.0254
BMI = kg / m**2
print("BMI는 {0:.5} 입니다.".format(BMI))

eval(input())
