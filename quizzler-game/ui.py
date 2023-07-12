from tkinter import *
import html
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: ", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some question text", font=("Arial", 20, "italic"), fill=THEME_COLOR)

        check_image = PhotoImage(file="images/true.png")
        cross_image = PhotoImage(file="images/false.png")
        self.check_btn = Button(image=check_image, highlightthickness=0)
        self.check_btn.grid(column=0, row=2)
        self.cross_btn = Button(image=cross_image, highlightthickness=0)
        self.cross_btn.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = html.unescape(self.quiz.next_question())
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.quiz.check_answer