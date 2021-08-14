import random
import tkinter as tk
from tkinter import ttk

score=0
total=0

ques = "hello"

def newcalc():
    global question_label
    global ques
    global res
    a = random.randint(0,10)
    b = random.randint(0,10)
    astr = str(a)
    bstr = str(b)
    xstr = "x"
    ques = f"{a} {xstr} {bstr}"
    question_label = ttk.Label(main, text=ques)
    question_label.grid(column=0, row=0, columnspan=1, sticky=tk.EW)
    scorelabel = ttk.Label(main, text=(score, "/", total))
    scorelabel.grid(column=0, row= 3, sticky=tk.EW)

    res= a*b



def ginp():
    global score
    global res
    global total
    ctrlvar = input_label.get()
    if int(ctrlvar) == int(res):
        print("Bravo")
        score += 1
    else:
        print("Die Richtige antwort, wäre",res, "gewesen")
    total += 1
    clearentry()
    newcalc()

def clearentry():
    input_label.delete(0, 'end')

main = tk.Tk()
main.geometry("600x300")
main.title('1x1 Trainer')
main.resizable(True, True)

main.columnconfigure(0)
main.columnconfigure(1)
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=1)
main.rowconfigure(2, weight=1)
main.rowconfigure(3, weight=1)

newcalc()




input_label = ttk.Entry(main)
input_label.grid(column=0, row= 1, columnspan=1, sticky=tk.EW)

controll_button = ttk.Button(main, text="Kontrollieren", command=ginp)
controll_button.grid(column=0, row=2, columnspan=1, sticky=tk.EW)





main.mainloop()

