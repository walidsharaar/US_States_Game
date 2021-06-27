import turtle


screen = turtle.Screen()
screen.title("States Game")
image= "states.gif"
screen.addshape(image)
turtle.shape(image)

#askk the user
answer= screen.textinput(title=" State Name ",prompt="Enter a state name: ")
print(answer)


