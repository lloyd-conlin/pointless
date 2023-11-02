import tkinter as tk
from tkinter.ttk import *
import time

def setMaxProgress():
    global value_progress
    global value_string
    global answer_string
    global s
    value_progress.set(100)
    value_string.set("100")
    answer_string.set("")
    s.configure("score.Vertical.TProgressbar", foreground='blue', background='blue')
    

def countDown(stopPoint):
    global value_string
    progress = value_progress.get()
    value_string.set(str(progress))
    if progress != stopPoint:
        progressbar.step(-1)
        window.after(50, lambda: countDown(stopPoint))

def wrongAnswer():
    global value_string
    s.configure("score.Vertical.TProgressbar", foreground='red', background='red')
    value_string.set("X")
    


def checkAnswer(answers, answer):
    time.sleep(2)
    if answer in answers:
        countDown(answers[answer])
    else:
        wrongAnswer()

answers = {"red": 57, "green": 24, "yellow": 9, "white": 4}
numberOfTeams = 5

window = tk.Tk()
window.geometry("700x700")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

value_progress = tk.IntVar()
value_string = tk.StringVar()
answer_string = tk.StringVar()
teams = {f"Team {i+1}": {"name": "", "score": tk.IntVar(), "out": False} for i in range(5) }


barFrame = tk.Frame(window)
barFrame.grid(row=0, column=1, pady=8, padx=8)

textFrame = tk.Frame(window)
textFrame.grid(row=0, column=0, pady=8, padx=8)

teamFrame = tk.Frame(window)
teamFrame.grid(row=1, column=0, columnspan=2, pady=8, padx=8)

labelProgress = tk.Label(barFrame, textvariable=value_string)
labelProgress.pack()

s = Style()
s.theme_use('clam')
s.configure("score.Vertical.TProgressbar", foreground='blue', background='blue')

setMaxProgress()

progressbar = Progressbar(barFrame, orient=tk.VERTICAL,
                          length=400, mode="determinate",
                          variable=value_progress,value=100,
                          style="score.Vertical.TProgressbar"
                          )
progressbar.pack(ipadx=30)

buttonReset = tk.Button(barFrame, text="Reset", command=setMaxProgress)
buttonReset.pack()

labelQuestion = tk.Label(textFrame, text="Name a colour on the flag of Suriname")
labelQuestion.pack()

labelAnswer = tk.Label(textFrame, text="Answer")
labelAnswer.pack()

answerField = tk.Entry(textFrame, textvariable=answer_string, width=30)
answerField.pack()

buttonS = tk.Button(textFrame, text="Check Answer", command=lambda: checkAnswer(answers, answer_string.get()))
buttonS.pack()

window.mainloop()
