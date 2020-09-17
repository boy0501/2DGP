import turtle
import random
# 쉬운 버전
#def draw_line_basic(p1, p2):
###  #  draw_big_point(p1)
##   # draw_big_point(p2)
##    x1, y1 = p1[0], p1[1]
##    x2, y2 = p2[0], p2[1]
##    a = (y2-y1)/(x2-x1)
##    b = y1 - x1 * a
##    for x in range(x1, x2 + 1, 10):
##        y = a * x + b
##        turtle.penup()
##        turtle.goto(x,y)
##        turtle.pendown()
##        turtle.stamp()
##    draw_point(p2)

#벡터 사용 버전 -> 이게 x축좌표계를 기준으로 하는 윗 함수보다 우수하다
##def draw_line(p1, p2):
##    for i in range(0, 100 + 1, 2):
##        t = i / 100
##        x = (1-t)*p1[0]+t*p2[0]
##        y = (1-t)*p1[1]+t*p2[1]
##        turtle.penup()
##        turtle.goto(x,y)
##        turtle.pendown()
##        turtle.stamp()
##    draw_point(p2)
##
##turtle.Canvas()
###prepare_turtle_canvas()
###draw_line_basic((-100,-100),(-90,100))
##draw_line((-200,-100),(-220,150))
##
##turtle.done()

numbers = [n for n in range(1,10)]
print(numbers)
even_numbers = [n for n in range(1,11) if n%2 == 0]
print(even_numbers)

random_numbers = [random.randint(1,100) for n in range(10)]
print(random_numbers)
