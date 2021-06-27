import turtle
import pandas


screen = turtle.Screen()
screen.title("States Game")
image= "states.gif"
screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")
states=data.state.to_list()
print(states)
guessed_states=[]
while len(guessed_states)<50:

    #askk the user
    answer= screen.textinput(title=f" {len(guessed_states)} State Name ",prompt="Enter a state name: ").title()
    print(answer)
    if answer in states:
        guessed_states.append(answer)
        my_turtle = turtle.Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        state_data= data[data.state == answer]
        my_turtle.goto(int(state_data.x),int(state_data.y))
        my_turtle.write(answer)


screen.exitonclick()





