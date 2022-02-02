import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#262626')
t.pencolor('#7C909C')
t.speed (100)
col=('#ED9864', '#9E644F', '#392F2F', '#4E682E')
for n in range(6):
    for x in range (8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()
