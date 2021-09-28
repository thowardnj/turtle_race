from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ['tim', 'tom', 'ed', 'fred', 'zied', 'pearl']
x = -225
y = -100
all_turtles = []

for index in range(len(names)):
    names[index] = Turtle(shape="turtle")
    names[index].color(colors[index])
    names[index].pu()
    names[index].goto(x, y )
    y += 30

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in names:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
