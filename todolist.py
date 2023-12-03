import tkinter
from tkinter import *

root = Tk()
root.title("To Do List")
root.geometry("400 * 650+400+100")
root.resizable(False, False)

task_list = []


ImageIcon = PhotoImage(file="image/aaa.png")
root.iconphoto(False, ImageIcon)

TopImage = PhotoImage(file="image/aaa.png")
Label(root, image= TopImage).pack()

DockImage = PhotoImage(file= "image/aaa.png")
Label(root, image = DockImage, bg="#32405b").place(x=30 , y = 25)



noteImage = PhotoImage(file="image/aaa.png")
Label(root, image=noteImage, bg= "#32405b" ).place(x = 30, y=25)


heading = Label(root, text="ALL TASK", font= "arial 20 bold", fg= "white", bg="#32405b")
heading.place(x=130, y=10)

# main
frame = Frame(root , width=400, height= 50 ,bg= "white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font= "arial", bd=0)
task_entry.place(x=10, y=7)

button = Button(frame, text="ADD", font="arial 20 bold",width=6, bg="#32405b", fg="#fff", bd=0)
button.place(x=300, y=0)



root.mainloop()