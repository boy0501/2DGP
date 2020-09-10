import turtle
#turtle.shape('turtle')

turtle.penup()
##########

## l 를 그리는
#함수 인자 : ㅣ가 그려질 x,y
#           ㅣ의 두께,높이
def makel(x,y,width,height):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(width)
        else:
            turtle.forward(height)
        turtle.right(90)
        i+=1
    turtle.setheading(45)
    turtle.forward(width)
    turtle.right(45)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.penup()
    turtle.goto(x+width,y-height)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(width)
    turtle.penup()
    turtle.goto(x+width,y)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(width)

# COMMAND가 1이면 ㅁ을 그려주고 
# COMMAND 가 0이면 좌표이동 후 아래를 보게 하는 함수이다.
def setaa(x,y,width,COMMAND):
    turtle.penup()
    turtle.setheading(270)
    turtle.goto(x,y)
    turtle.pendown()
    if COMMAND==1:
        for i in range(4):
            turtle.forward(width)
            turtle.left(90)
            
def setuptt():
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-50,250)
    turtle.pendown()


def setupnn():
    turtle.penup()
    turtle.goto(-150,100)
    turtle.pendown()

makel(-100,-100,50,50)
makel(-50,-150,50,25)

turtle.penup()
turtle.back(350)
turtle.down()
turtle.circle(100)
turtle.penup()
turtle.goto(-350,40)
turtle.pendown()
turtle.circle(60)
turtle.circle(45,-90)
turtle.circle(180,-10)
turtle.circle(50,-80)
turtle.penup()
turtle.goto(-350,205)
turtle.pendown()
turtle.circle(60,35)
turtle.penup()
turtle.goto(-350,205)
turtle.pendown()
turtle.setheading(0)
turtle.circle(-110,90)
turtle.circle(-80,73)
turtle.penup()


makel(-230,250,30,250)

#----수 만든거

setuptt()
turtle.right(90)
turtle.forward(50)
turtle.right(45)
turtle.forward(70)
turtle.left(90)
turtle.forward(30)
turtle.left(80)
turtle.forward(57)


setuptt()
turtle.forward(30)

turtle.right(90)
turtle.forward(50)
turtle.left(45)
turtle.forward(70)
turtle.right(90)
turtle.forward(30)
turtle.right(80)
turtle.forward(57)

setuptt()

turtle.left(45)
turtle.forward(15)
turtle.right(45)
turtle.forward(30)
turtle.setheading(270)
turtle.forward(60)
turtle.left(45)
turtle.forward(60)
turtle.right(90)
turtle.forward(10)

setuptt()


setupnn()
turtle.forward(220)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(30)
turtle.right(45)
turtle.forward(20)
turtle.setheading(0)
turtle.forward(220)
turtle.right(90)
turtle.forward(30)
turtle.right(45)
turtle.forward(20)
turtle.penup()
turtle.goto(-20,0)
turtle.pendown()
turtle.setheading(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(56)
setupnn()

    
setaa(100,230,100,1)

setaa(120,210,60,1)
setaa(140,210,0,0)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)

setaa(100,230,0,0)

turtle.setheading(45)
turtle.forward(30)
turtle.setheading(0)
turtle.forward(100)
turtle.setheading(270)
turtle.forward(100)
turtle.setheading(225)
turtle.forward(30)


setaa(240,260,0,0)
makel(240,260,30,140)

setaa(130,80,0,0)
turtle.forward(80)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(30)
turtle.setheading(45)
turtle.forward(15)
turtle.setheading(0)
turtle.forward(30)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(29)
turtle.setheading(225)
turtle.forward(15)

setaa(0,0,0,0)

turtle.exitonclick()
