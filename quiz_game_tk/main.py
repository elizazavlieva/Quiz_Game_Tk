import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from question_model import questions, choices, answers


# global variables
user_answer = []
qs_indexes = []
incorrect_qs = []


# restarting the game
def play_again():
    global ques
    text_label.destroy()
    score_label.destroy()
    new_game_btn.destroy()
    quit_button.destroy()
    qs_indexes.clear()
    user_answer.clear()
    ques = 1
    random_qs_index()
    game()


# quitting the game
def quit_game():
    window.quit()


# returning the results
def display_results():
    points = correct_answers
    if points >= 10:
        win_img = PhotoImage(file="images\\winner.png")
        score_label.config(image=win_img)
        score_label.image = win_img
        text_label.config(text=f"Amazing! {points}/{len(qs_indexes)}")
    elif 5 <= points < 10:
        average_img = Image.open("images\\good_job.png")
        rs_average_img = ImageTk.PhotoImage(average_img.resize((400, 350)))
        score_label.config(image=rs_average_img)
        score_label.image = rs_average_img
        text_label.config(text=f"Good job! {points}/{len(qs_indexes)}")
    else:
        game_over = Image.open("images\\game_over.png")
        rs_game_over = ImageTk.PhotoImage(game_over.resize((400, 300)))
        score_label.config(image=rs_game_over)
        score_label.image = rs_game_over
        text_label.config(text=f"Game over! {points}/{len(qs_indexes)}")


# returning the results
def end_game():
    global score_label, image_label, text_label, new_game_btn,  quit_button

    qs_label.destroy()
    btn_one.destroy()
    btn_two.destroy()
    btn_three.destroy()
    btn_four.destroy()
    submit_btn.destroy()

    score_label = Label(window,
                        font=('Comic Sans MS', 20, 'bold'), fg='black', bg='#D4A373', pady=20, height=470,
                        compound="center"
                        )
    score_label.pack()
    text_label = Label(window, font=('Comic Sans MS', 30, 'bold'), fg='black', bg='#D4A373', compound=CENTER
                       )
    text_label.pack()
    new_game_btn = Button(window, text="New game", font=('Comic Sans MS', 15, 'bold'), fg='black', bg="#FAEDCD",
                          activebackground="#FAEDCD", command=play_again, pady=10
                          )
    new_game_btn.pack(side=tk.RIGHT)

    quit_button = tk.Button(window, text="Exit", font=('Comic Sans MS', 15, 'bold'), fg='black', bg="#FAEDCD",
                            activebackground="#FAEDCD", command=quit_game, pady=10
                            )
    quit_button.pack(side=tk.RIGHT)
    display_results()


correct_answers = 0


def score():
    global correct_answers, incorrect_qs
    counter = 0

    for qs in qs_indexes:
        if user_answer[counter] == answers[qs]:
            correct_answers += 1
        else:
            incorrect_qs.append(qs_indexes[counter])
        counter += 1


ques = 1
# saving user answers in list and switching to next question till last question
def user_answer_storage():
    global var, user_answer, ques, qs_indexes, correct_answers
    global qs_label, btn_one, btn_two, btn_three, btn_four, submit_btn

    x = var.get()

    user_answer.append(x)

    var.set(-1)
    if ques < len(qs_indexes):

        qs_label.config(text=questions[qs_indexes[ques]])
        btn_one.config(text=choices[qs_indexes[ques]][0])
        btn_two.config(text=choices[qs_indexes[ques]][1])
        btn_three.config(text=choices[qs_indexes[ques]][2])
        btn_four.config(text=choices[qs_indexes[ques]][3])
        ques += 1
    else:
        btn_one.config(state=DISABLED)
        btn_two.config(state=DISABLED)
        btn_three.config(state=DISABLED)
        btn_four.config(state=DISABLED)
        submit_btn = Button(window, text='Submit', fg='black', bg="#FAEDCD", font=('Comic Sans MS', 15, 'bold'),
                            compound="bottom", command=end_game)
        submit_btn.pack(side=tk.LEFT)
        score()


# creating labels for the questions and radio buttons for the possible answers
def game():
    global qs_label, btn_one, btn_two, btn_three, btn_four, var

    entry_label.destroy()
    start_button.destroy()
    random_qs_index()

    qs_label = Label(window, text=questions[qs_indexes[0]], font=('Comic Sans MS', 20, 'bold'), fg='black',
                     bg='#FAEDCD', justify="center", wraplength=600, pady=20, padx=150
                     )

    qs_label.pack(pady=(100, 30))

    var = IntVar()
    var.set(-1)
    btn_one = Radiobutton(window,
                          text=choices[qs_indexes[0]][0], font=('Comic Sans MS', 15, 'bold'), fg='black', bg='#FAEDCD',
                          justify="center", pady=10, indicatoron=False, activeforeground='black',
                          activebackground='#FAEDCD', variable=var, value=0, width=20, command=user_answer_storage
                          )
    btn_one.pack()

    btn_two = Radiobutton(window,
                          text=choices[qs_indexes[0]][1], font=('Comic Sans MS', 15, 'bold'), fg='black',
                          bg='#FAEDCD', pady=10, indicatoron=False, activeforeground='black',
                          activebackground='#FAEDCD', variable=var, value=1, width=20, command=user_answer_storage
                          )
    btn_two.pack()

    btn_three = Radiobutton(window,
                            text=choices[qs_indexes[0]][2], font=('Comic Sans MS', 15, 'bold'), fg='black',
                            bg="#FAEDCD", pady=10, indicatoron=False, activeforeground='black',
                            activebackground='#FAEDCD', variable=var, value=2, width=20, command=user_answer_storage
                            )
    btn_three.pack()

    btn_four = Radiobutton(window,
                           text=choices[qs_indexes[0]][3], font=('Comic Sans MS', 15, 'bold'), fg='black', bg='#FAEDCD',
                           pady=10, indicatoron=False, activeforeground='black', activebackground='#FAEDCD',
                           variable=var, value=3, width=20, command=user_answer_storage
                           )
    btn_four.pack()


# selecting random questions by index
def random_qs_index():
    global qs_indexes
    while len(qs_indexes) < 15:
        index = random.randint(0, 49)
        if index in qs_indexes:
            continue
        else:
            qs_indexes.append(index)


# creating main window and setting some parameters
window = Tk()
window.geometry('700x600')
window.title("Quiz game")
window.config(bg='#D4A373')
icon = PhotoImage(file="images\\image.png")
window.iconphoto(True, icon)
window.resizable(width=False, height=False)

# creating label
img = Image.open("images\\start.png")
img = img.resize((250, 300))
final_img = ImageTk.PhotoImage(img)
entry_label = Label(window, text="Welcome to Quizzy!", font=('Comic Sans MS', 40, 'bold'), fg='black',
                    bg='#D4A373', pady=20, compound='top', image=final_img,
                    )
entry_label.pack()

img2 = Image.open("images\\start_btn.png")
img2 = img2.resize((200, 100))
final = ImageTk.PhotoImage(img2)
start_button = Button(window, bg="#D4A373", activebackground="#D4A373", image=final, command=game,
                      compound='bottom'
                      )
start_button.pack()
window.mainloop()
