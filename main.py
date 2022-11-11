import random
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="race", prompt="Which turtle color you choose?: ")

tim = Turtle(shape="turtle")
tim.color("red")
tim.penup()
tim.goto(-230, -130)


timmy = Turtle(shape="turtle")
timmy.color("orange")
timmy.penup()
timmy.goto(-230, -70)


tommy = Turtle(shape="turtle")
tommy.color("yellow")
tommy.penup()
tommy.goto(-230, -20)


tonny = Turtle(shape="turtle")
tonny.color("green")
tonny.penup()
tonny.goto(-230, 20)


trevor = Turtle(shape="turtle")
trevor.color("blue")
trevor.penup()
trevor.goto(-230, 70)


jenny = Turtle(shape="turtle")
jenny.color("purple")
jenny.penup()
jenny.goto(-230, 130)


reach_end = True
while reach_end:
    if tim.xcor() > 230 or timmy.xcor() > 230 or tommy.xcor() > 230 or tonny.xcor() > 230 or trevor.xcor() > 230 or jenny.xcor() > 230:
        reach_end = False
    tim.forward(random.randint(0, 10))
    timmy.forward(random.randint(0, 10))
    tommy.forward(random.randint(0, 10))
    tonny.forward(random.randint(0, 10))
    trevor.forward(random.randint(0, 10))
    jenny.forward(random.randint(0, 10))



screen.exitonclick()
