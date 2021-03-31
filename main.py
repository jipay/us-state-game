import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the U.S. States")
background = "blank_states_img.gif"
screen.addshape(background)
turtle.shape(background)

data = pandas.read_csv("50_states.csv")
print(data["state"].tolist())
guessed_list = []
states_list = data["state"].tolist()

is_on = True
while is_on and len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        print("Bye bye!")
        break
    if answer_state in states_list:
        print(f"well done. You have guessed {answer_state}")
        if answer_state not in guessed_list:
            city_datas = data[data["state"] == answer_state]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(city_datas.x), int(city_datas.y))
            t.write(city_datas.state.item())
            guessed_list.append(city_datas.state.item())
        else:
            print("already guessed")
    else:
        print(f"You're wrong {answer_state} is not one of the U.S. States.\nGAME OVER.")
        learning_list = []
        for state in states_list:
            if state not in guessed_list:
                learning_list.append(state)
        print(learning_list)
        df = pandas.DataFrame(learning_list)
        df.to_csv("states_learning_list.csv")
        is_on = False
screen.exitonclick()


