import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain

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
            width=280,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, 'italic')
        )

        correct = tkinter.PhotoImage(file='images/true.png')
        incorrect = tkinter.PhotoImage(file='images/false.png')
        
        self.correct_button = tkinter.Button(image=correct, highlightthickness=0, command=self.true_pressed)
        self.incorrect_button = tkinter.Button(image=incorrect, highlightthickness=0, command=self.false_pressed)

        self.correct_button.grid(row=2, column=0)
        self.incorrect_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the game")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")

    def true_pressed(self) -> bool:
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self) -> bool:
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)