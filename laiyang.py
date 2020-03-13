from turtle import *
speed(10)
bgcolor('orange')
# 字
def writ_word(num,num1,color1,write_word,size1):
    penup()
    goto(num,num1)
    pendown()
    pencolor(color1)
    write(write_word,font=('arial',size1))

writ_word(-30,380,'brown','灿烂的勇气',40)
writ_word(10,250,'red','莱阳',70)
writ_word(-300,-240,'black','在地球上化身为狮子的太阳',15)
writ_word(-360,-290,'black','无法隐藏的光芒成了它闪闪发光的鬃毛',15)
writ_word(-290,-340,'black','给人们带去无限勇气和希望',15)
writ_word(-290,-390,'brown',' #太阳 #发光的鬃毛 #勇气',15)

# 去哪
def goto_where(first,second):
    penup()
    goto(first,second)
    pendown()

def left_fd(num3,num4):
    lt(num3)
    fd(num4)

def right_fd(num5,num6):
    rt(num5)
    fd(num6)

# 头发
begin_fill()
color('red','red')
goto_where(80,180)
circle(-200)
end_fill()
speed(10)
# 脸
width(10)
goto_where(0,100)
begin_fill()
rt(150)
color('black','yellow')
circle(150,340)
end_fill()
# 刘海
goto_where(0,100)
width(1)
pencolor('red')
begin_fill()
width(9)
fillcolor('red')
left_fd(120,50)
left_fd(120,55)
end_fill()
begin_fill()
fillcolor('red')
right_fd(140,50)
left_fd(140,55)
end_fill()
width(20)
pencolor('red')
lt(105)
circle(150,33)
# 眉毛和眼睛
goto_where(0,30)
pencolor('black')
width(5)
right_fd(205,25)
goto_where(12,10)
width(2)
begin_fill()
fillcolor('black')
circle(-8)
end_fill()
goto_where(112,10)
width(2)
begin_fill()
fillcolor('black')
circle(-8)
end_fill()
goto_where(100,30)
width(5)
fd(25)
# 左胡须
goto_where(25,-100)
left_fd(200,35)
goto_where(0,-30)
right_fd(10,40)
goto_where(9,-60)
right_fd(-10,40)
# 鼻子和嘴巴
goto_where(50,-30)
begin_fill()
fillcolor('black')
lt(70)
circle(15,180)
end_fill()
left_fd(90,30)
goto_where(65,-45)
right_fd(270,30)
goto_where(57,-70)
right(360)
circle(10,180)
# 右胡须
goto_where(130,-30)
right_fd(105,45)
goto_where(130,-60)
right_fd(10,40)
# 身子
goto_where(25,-220)
width(5)
begin_fill()
color('black','yellow')
right_fd(70,140)
lt(40)
circle(20,60)
right_fd(100,60)
lt(40)
circle(10,180)
left_fd(320,50)
left_fd(-90,60)
right_fd(90,60)
lt(40)
circle(10,180)
left_fd(320,50)
rt(100)
circle(20,60)
left_fd(40,140)
end_fill()
# 头发
def hair(num1,num2,num3,num4):
    lt(num1)
    fd(num2)
    rt(num3)
    fd(num4)
goto_where(130,-100)
rt(120)
fd(35)
goto_where(90,180)
begin_fill()
color('black','red')
pendown()
hair(70,100,100,155)
hair(80,100,130,165)
end_fill()
begin_fill()
color('black','red')
hair(80,100,130,110)
hair(80,130,120,100)
end_fill()
begin_fill()
color('black','red')
hair(80,130,120,100)
hair(80,130,130,80)
end_fill()
begin_fill()
color('black','red')
hair(120,130,120,130)
hair(90,130,130,130)
end_fill()
begin_fill()
color('black','red')
hair(90,130,120,135)
hair(70,130,110,120)
end_fill()
# 光芒
pencolor('black')
width(10)
goto_where(-230,100)
left_fd(200,50)
goto_where(-210,160)
right_fd(360,80)
goto_where(-240,240)
left_fd(180,50)
# 手
goto_where(35,-300)
begin_fill()
color('black','white')
width(5)
rt(90)
circle(15)
goto_where(105,-300)
pencolor('black')
rt(360)
circle(15)
end_fill()
goto_where(25,-250)
left_fd(57,55)
goto_where(25,-280)
right_fd(10,20)
goto_where(150,-250)
right_fd(60,50)
begin_fill()
color('black','yellow')
goto_where(150,-280)
right_fd(2,30)
goto_where(37,-405)
left_fd(120,15)
goto_where(124,-405)
right_fd(180,12)
hideturtle()
done()