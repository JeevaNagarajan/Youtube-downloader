from pytube import YouTube
from tkinter import *

gui = Tk()

gui.title('youtube downloader')

gui.geometry('820x500')

filename = PhotoImage(file="bg_img/YT.png")
background_label = Label(gui,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1.7)

str_var = StringVar()

label_1 = Label(gui,text='Video Url',fg='royalblue4',font=("Helvetica",20)).place(x=10,y=45,height=50,width=150)
entry_1 = Entry(gui,text=str_var,font=("Helvetica",17),fg='dim grey').place(x=150,y=50,height=40,width=540)

def download():
    try:
        yt = YouTube(str_var.get()).streams.first().download('Downloads')

        e2_var = StringVar(value=yt.title())
        entry_2 = Entry(gui, textvariable=e2_var,font=("Helvetica",16),fg='black').place(x=30,y=150,height=60,width=750)

        e3_var = StringVar(value='  downloaded successfully!!!')
        entry_3 = Entry(gui,textvariable=e3_var,font=("Helvetica",17),fg='medium purple').place(x=250,y=250,height=55,width=300)

    except:
        e4_var = StringVar(value='Error!!')
        entry_4 = Entry(gui,textvariable=e4_var,font=("Helvetica",17),fg='black').place(x=30,y=150,height=60,width=750)

def clear():
    str_var.set("")

def exit():
    gui.destroy()

button_1 = Button(gui,text='Download',font=("Helvetica",13),fg='gainsboro',bg='royalblue4',command=download,height=2,width=7).place(x=700,y=45,height=50,width=100)
button_2 = Button(gui,text='Clear',font=("Helvetica",14),fg='white',bg='red',command=clear,height=2,width=7).place(x=10,y=250,height=50,width=100)
button_3 = Button(gui,text='Exit',font=("Helvetica",14),fg='gainsboro',bg='gray23',command=exit,height=2,width=7).place(x=700,y=250,height=50,width=100)

gui.mainloop()


