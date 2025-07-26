import tkinter

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, background='white')
        self.canvas.grid(row=1, columnspan=2, column=0, pady=50)

        self.question_text=self.canvas.create_text(
            150,
            125,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, 'italic')
        )

        correct = tkinter.PhotoImage(file='images/true.png')
        incorrect = tkinter.PhotoImage(file='images/false.png')
        
        self.correct_button = tkinter.Button(image=correct, highlightthickness=0)
        self.incorrect_button = tkinter.Button(image=incorrect, highlightthickness=0)

        self.correct_button.grid(row=2, column=0)
        self.incorrect_button.grid(row=2, column=1)
        
        
        
        self.window.mainloop()


