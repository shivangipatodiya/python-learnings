from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "yellow", "orange", "blue", "purple"]
turtles = []

y = -180
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    y += 50
    turtle.goto(x=-230, y=y)
    turtles.append(turtle)

race_on = True
if user_bet:
    while race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You have won. The winner is {winner} turtle.")
                else:
                    print(f"You have lost. The winner is {winner} turtle.")

            step_distance = random.randint(0, 10)
            turtle.forward(step_distance)


screen.exitonclick()