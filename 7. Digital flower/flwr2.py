import turtle

turtle.screensize(500, 500)
turtle.Screen().bgcolor( "grey")
pat = turtle.Turtle()
pat.color( "cyan")

def flakes():
    for i in range(12):
        for j in range(2):
            pat.forward( 100)
            pat.right(60)
            pat.forward(100)
            pat.right(120)
        pat.right(30)
turtle.ontimer(flakes, 3000)
turtle.exitonclick()