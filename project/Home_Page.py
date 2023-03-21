from setting import *
from Tadasana import Tadasana
from Sukhasana import Sukhasana
from Vrikshasana import Vrikshasana
from Virabhadrasana import Virabhadrasana
from Real_Time_Color_Detection import real_time_color
from Image_Color_Detection import image_color_detection
from MathematicOperations import Mathematicoperaation
from hand_sign_detection import Hand_detection
from IT_searches import It_searches

def Back(master):
    master.destroy()
    Home_page()

def KG():
    root=Tk()  
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    img = PhotoImage(file='project\\assets\\online-kindergarten.png')
    Label(root,image=img,bg='white').place(x=50,y=90)

    frame=Frame(root,width=400,height=600,bg="white")
    frame.place(x=480,y=0)

    heading=Label(frame,text='Kinder-Garten',fg='#87cff0',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=75,y=5)


            ####################### Button
    Button(frame,width=30,pady=7,text='Sign language',command=Hand_detection,bg='#d6b935',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=70)
    Button(frame,width=30,pady=7,text='Identifying Colours',command=image_color_detection,bg='#87cff0',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=160)
    Button(frame,width=15,pady=7,text='GO TO HOME',command=lambda :Back(root),bg='#d6b935',fg='white',border=0,font=('Microsoft YaHei UI Light',8,'bold')).place(x=170,y=425)
    root.mainloop()

def primary():
    root=Tk()  
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    img = PhotoImage(file='project\\assets\\Primary.png')
    Label(root,image=img,bg='white').place(x=50,y=90)

    frame=Frame(root,width=400,height=600,bg="white")
    frame.place(x=480,y=0)

    heading=Label(frame,text='Primary',fg='#5459fe',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=75,y=5)

            ####################### Button
    Button(frame,width=30,pady=7,text='Moral Scienece',command=lambda:Moral_sc_button(root),bg='#5459fe',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=160)
    Button(frame,width=30,pady=7,text='Fun with Maths',command=Mathematicoperaation,bg='#fd9393',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=250)
    Button(frame,width=15,pady=7,text='GO TO HOME',command=lambda :Back(root),bg='#5459fe',fg='white',border=0,font=('Microsoft YaHei UI Light',8,'bold')).place(x=170,y=425)
    root.mainloop()

def Secondary():
    root=Tk()  
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    img = PhotoImage(file='project\\assets\\secondary.png')
    Label(root,image=img,bg='white').place(x=50,y=90)

    frame=Frame(root,width=400,height=600,bg="white")
    frame.place(x=480,y=0)

    heading=Label(frame,text='Secondary',fg='#5459fe',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=75,y=5)


            ####################### Button
    Button(frame,width=30,pady=7,text='Information Technology', command=It_searches,bg='#fd9393',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=70)
    Button(frame,width=15,pady=7,text='GO TO HOME',command=lambda :Back(root),bg='#5459fe',fg='white',border=0,font=('Microsoft YaHei UI Light',8,'bold')).place(x=170,y=425)
    root.mainloop()

def Academics():

    root=Tk()  
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    img = PhotoImage(file='project\\assets\\color_det_2.png')
    Label(root,image=img,bg='white').place(x=50,y=90)

    frame=Frame(root,width=400,height=600,bg="white")
    frame.place(x=480,y=0)

    heading=Label(frame,text='Select Standard',fg='#f86c57',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=75,y=5)


        ####################### Button
    Button(frame,width=30,pady=7,text='KG',command=lambda:KG_BUTTON(root),bg='#F8AE57',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=65)
    Button(frame,width=30,pady=7,text='PRIMARY',command=lambda:primary_button(root),bg='#f86c57',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=125)
    Button(frame,width=30,pady=7,text='SECONDARY',command=lambda:Secondary_button(root),bg='#F8AE57',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=185)
    Button(frame,width=15,pady=7,text='GO TO HOME',command=lambda :Back(root),bg='#f86c57',fg='white',border=0,font=('Microsoft YaHei UI Light',8,'bold')).place(x=170,y=425)
    root.mainloop()

def Asana_page():
    root=Tk()  
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    img = PhotoImage(file='project\\assets\\Yoga_Asana.png')
    Label(root,image=img,bg='white').place(x=50,y=90)

    frame=Frame(root,width=350,height=370,bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame,text='Yoga Postures',fg='#f86c57',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=90,y=5)

    Button(frame,width=30,pady=7,text='TADASANA',command=Tadasana ,bg='#f86c57',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=70)
    Button(frame,width=30,pady=7,text='SUKHASANA',command=Sukhasana,bg='#F8AE57',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=140)
    Button(frame,width=30,pady=7,text='VRIKSHASANA',command=Vrikshasana,bg='#f86c57',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=210)
    Button(frame,width=30,pady=7,text='Virabhadrasana', command=Virabhadrasana,bg='#F8AE57',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=280)
    Button(frame,width=15,pady=7,text='GO TO HOME',command=lambda :Back(root),bg='#f86c57',fg='white',border=0,font=('Microsoft YaHei UI Light',8,'bold')).place(x=160,y=340)
    
    root.mainloop()
    
def Moral_sci():
    root=Tk()  
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    img = PhotoImage(file='project\\assets\\secondary.png')
    Label(root,image=img,bg='white').place(x=50,y=90)

    frame=Frame(root,width=400,height=600,bg="white")
    frame.place(x=480,y=0)

    heading=Label(frame,text='Kinder-Garten',fg='#87cff0',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=75,y=5)

    Button(frame,width=30,pady=7, command=lambda:webbrowser.open_new_tab("https://www.vedantu.com/stories/short-story-on-loyalty"),text='Short Story on LOYALTY',bg='#d6b935',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=70)
    Button(frame,width=30,pady=7, command=lambda:webbrowser.open_new_tab("https://www.moralstories.org/the-shepherd-boy-and-the-wolf/"),text='Short Story on HONESTY',bg='#87cff0',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=160)
    Button(frame,width=30,pady=7, command=lambda:webbrowser.open_new_tab("https://www.moralstories.org/needy-king-sage/"),text='Short Story on CONTENTMENT',bg='#d6b935',fg='white',border=0,font=('Microsoft YaHei UI Light',10,'bold')).place(x=70,y=250)
    Button(frame,width=15,pady=7, command=lambda :Back(root),text='GO TO HOME',bg='#87cff0',fg='white',border=0,font=('Microsoft YaHei UI Light',8,'bold')).place(x=170,y=425)
    root.mainloop()
    
def Asana_button(master):
    master.destroy()
    Asana_page()

def Academics_button(master):
    master.destroy()
    Academics()
    
def KG_BUTTON(master):
    master.destroy()
    KG()
    
def primary_button(master):
    master.destroy()
    primary()

def Secondary_button(master):
    master.destroy()
    Secondary()
    
def Moral_sc_button(master):
    master.destroy()
    Moral_sci()
    

def Home_page():
    root=Tk()  
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)
    
    img = PhotoImage(file='project\\assets\\yoga_login.png')
    Label(root,image=img,bg='white').place(x=50,y=50)
    
    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame,text='Welcome to AI \n powered Learning App',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',22,'bold'))
    heading.place(x=10,y=5)

    ####################### Button
    Button(frame,width=39,pady=7,text='CO-CURRICULAR', command=lambda:Asana_button(root), bg='#57a1f8',fg='white',border=0).place(x=35,y=107)
    Button(frame,width=39,pady=7,text='ACADEMICS', command=lambda:Academics_button(root), bg='#57a1f8',fg='white',border=0).place(x=40,y=177)

    root.mainloop()

