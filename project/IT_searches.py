from tkinter import *
import webbrowser


def It_searches():

    ak = Tk()

    #normal functions------------------------------------------------------------------------
    ak.title("ANURAG's PROGRAM")
    ak.geometry('600x400+10+10')
    ak.config(bg='lightblue')
    ak.minsize(600, 400)


    gtube_input = Text(ak,
                    height = 1,
                    width = 40)
    
    def gsearch():
        S = str(gtube_input.get(1.0,'end'))
        
        S.replace(" ", "+")
        webbrowser.open_new_tab(f"https://en.wikipedia.org/wiki/Special:Search?go=Go&search={S}&ns0=1")


    gsearch_lab = Label(ak , text = "Search Over Wikipedia For \n Any IT Related Info",fg = 'cyan4',bd = 8,bg = 'lightgray' ,
                font = ("times new roman" , 19, "bold"))

    g_searchB = Button(ak , text = 'SEARCH' , command = gsearch,
                        font = ("times new roman" , 15 , "bold" ) ,bd = 4, bg = 'slategray2' , fg = 'blue4',
                        activebackground = 'gray' , activeforeground = 'azure')

    gsearch_lab.place(x=120, y= 50)
    gtube_input.place(x=120, y=160)
    g_searchB.place(x= 200, y=200)


    mainloop()


