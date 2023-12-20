import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape("blank_states_img.gif", None)
turtle.shape("blank_states_img.gif")

# --------Used to find the coordinates of where the states should go---------
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

# Read the file
data = pandas.read_csv("50_states.csv")

guessed_states = []

while len(guessed_states) < 50 :
    player_answer = (turtle.textinput(f"{len(guessed_states)}/50", "Type the name of a state below")).title()

    guessed_states.append(player_answer)

    if player_answer == 'Exit':
        all_states = data.state.to_list()
        missing_states = [state for state in all_states if state not in guessed_states]
        
            
                
    # Write states that the player did not remember in a csv file for them to study.
        pandas.DataFrame(missing_states).to_csv('States_to_learn.csv')
        break

    if player_answer in data.state.to_list():
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()

        state_data = data[data.state == player_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(player_answer)

 



screen.exitonclick()