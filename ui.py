from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 125, text="Some question", width=280, fill=THEME_COLOR, font=("Arial", 20, "italic")
        )
        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=self.true_img, height=100, width=97, highlightthickness=0, bg=THEME_COLOR, command=self.answer_true
        )
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=self.false_img, height=100, width=97, highlightthickness=0, bg=THEME_COLOR, command=self.answer_false
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(ms=1000, func=self.get_next_question)
