from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ############  Using Pandas to read the file with the french words and create function  ################

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

def next_card():
    global current_card
    global flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    
    canvas.itemconfig(title, text="French", fill='black')
    canvas.itemconfig(word, text=current_card['French'], fill='black')
    canvas.itemconfig(background, image= card_front)
    flip_timer= window.after(3000, func=flip_it)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    
def flip_it():
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(word, text=current_card["English"], fill='white')
    canvas.itemconfig(background, image= card_back)



# ############   UI for the flash cards  ##############

window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title('French Flashcards')

flip_timer = window.after(3000, func=flip_it)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
background = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)

title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text= 'Word', font=('Ariel', 60, 'bold'))


right_answer = PhotoImage(file='images/right.png')
correct = Button(image=right_answer, command=is_known)
correct.grid(row=1, column=1)

wrong_answer = PhotoImage(file='images/wrong.png')
incorrect= Button(image=wrong_answer, command=next_card)
incorrect.grid(row=1, column=0)

next_card()

window.mainloop()