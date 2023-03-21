import random
from tkinter import *

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def submt(master,var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(master, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.3, rely=0.2)
    else:
        wrong = Label(master, text="Wrong!!!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.3, rely=0.2)


def try_again(master):
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)
    newQ = Label(master, text=f"{try_again.num1update}+{try_again.num2update}", font=("Courier", 35)
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update + try_again.num2update

def Mathematicoperaation():
    app = Tk()
    app.title("Math For Kids")
    # canvas = Canvas(app, width=240, height=300)
    # canvas.pack()
    app.geometry("925x500")
    app.resizable(False, False)

    app.config(bg="lightblue")

    Button(app,width=30,pady=7,text='Start',bg='#f86c57',fg='black',border=0,command=lambda: try_again(app),font=('Microsoft YaHei UI Light',10,'bold')).place(x=310,y=107)


    solving = Entry(app, font=("Courier", 35))
    solving.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.23)

    Button(app,width=30,pady=7,text='Submit',bg='#f86c57',fg='black',border=0,command=lambda: submt(app,solving),font=('Microsoft YaHei UI Light',10,'bold')).place(x=310,y=360)
    Button(app,width=30,pady=7,text='Try Again',bg='#f86c57',fg='black',border=0,command=lambda:try_again(app),font=('Microsoft YaHei UI Light',10,'bold')).place(x=310,y=420)

    app.mainloop()
    
