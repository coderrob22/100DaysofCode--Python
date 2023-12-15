import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape("blank_states_img.gif", None)
turtle.shape("blank_states_img.gif")

# --------Used to find the coordinates of where the states should go---------
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

player_answer = turtle.textinput("Guess a state", "Type the name of a state below")


screen.exitonclick()