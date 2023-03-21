from setting import *
from Home_Page import Home_page

root=Tk()
root.title('Login')
root.geometry('925x500+200+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='project\\assets\\Avatar-login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

######################  USERNAME 
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'UserName')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#######################  Password
def signup(master):
    data = np.load("data.npy")
    a = [user.get(), dob_entry.get()]
    data = np.vstack((data,a))
    np.save("data", data)
    root.destroy()
    Home_page()

##############################  DateOFBirth

def pick_date(event):
    global cal,date_window
    date_window=Toplevel()
    date_window.grab_set()
    date_window.title('Choose Date of birth')
    date_window.geometry('250x220+590+370')
    cal=Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")
    cal.place(x=0,y=0)
    submit_btn=Button(date_window,text="Submit",command=grab_date)
    submit_btn.place(x=80,y=190)

def grab_date():
    dob_entry.delete(0,END)
    dob_entry.insert(0,cal.get_date())
    date_window.destroy()

#create entry that will accept date of birth after clicking on submit

dob_entry= Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))

dob_entry.place(x=30,y=150)
dob_entry.insert(0, "Calendar")
dob_entry.bind("<1>",pick_date)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

####################### Button
Button(frame,command=lambda : signup(root),width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0).place(x=35,y=204)

root.mainloop()

