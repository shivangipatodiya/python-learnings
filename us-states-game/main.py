import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S.States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


while all_states:
    correct_guesses = 50 - len(all_states)
    answer = screen.textinput(f"{correct_guesses}/50 States correct", "What's another state's name? ")
    answer = answer.title()

    if answer == "Exit":
        df = pandas.DataFrame(all_states)
        df.to_csv("missing_states.csv")
        print(all_states)
        break

    if answer in all_states:
        info = data[data.state == answer]
        x = int(info["x"])
        y = int(info["y"])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(answer, align="center", font=("Courier", 12, "normal"))
        all_states.remove(answer)
