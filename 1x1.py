'''Imports'''
import random
import tkinter as tk
from tkinter import ttk

'''Set Variables'''
score=0
total=0
ques = "hello"

'''Define Functions'''
def newcalc():
    global question_label
    global ques
    global res
    a = random.randint(0,10)#Get Random Numbers between 0 and 10
    b = random.randint(0,10)
    astr = str(a) #Make a and b strings
    bstr = str(b)
    xstr = "x"
    ques = f"{a} {xstr} {bstr}"#Combine the Strings
    '''Set the first 2 labels'''
    question_label = ttk.Label(main, text=ques) 
    question_label.grid(column=0, row=0, columnspan=1, sticky=tk.EW)
    scorelabel = ttk.Label(main, text=(score, "/", total))
    scorelabel.grid(column=0, row= 3, sticky=tk.EW)
    #Get Solution
    res= a*b



def ginp():
    global score
    global res
    global total
    ctrlvar = input_label.get()#get input
    if int(ctrlvar) == int(res):#check if awnser correct
        print("Nice")
        score += 1
    else:
        print("The right awnser would've been ",res)
    total += 1
    clearentry()#call functions
    newcalc()

def clearentry():
    input_label.delete(0, 'end')#clear entry label

'''Setting the window up'''
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

newcalc()#start the cycle



'''Define some more labels'''
input_label = ttk.Entry(main)
input_label.grid(column=0, row= 1, columnspan=1, sticky=tk.EW)

controll_button = ttk.Button(main, text="Check", command=ginp)
controll_button.grid(column=0, row=2, columnspan=1, sticky=tk.EW)





main.mainloop()

