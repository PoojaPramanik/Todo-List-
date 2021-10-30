from tkinter import *
import pickle
window = Tk()
window.title("TODO List")
window.geometry("600x400")
window.resizable(False,False)
window.config(bg="salmon")
#window.overrideredirect(True)

def add():
    get = entry.get()
    text.insert(END,get)
def delete():
    text.delete(ANCHOR)
def save():
    task = text.get(0,text.size())
    pickle.dump(task, open("task.txt", "wb"))
def load_task():
    task = pickle.load(open("task.txt", "rb"))
    text.delete(0,END)
    for tasks in task:
        text.insert(END,tasks)

def reset():
    entry_value.set(" ")
def exit():
    window.destroy()

label1 = Label(window,text= "ENTER YOUR TASK",font="lucida 15 bold",bg="salmon",fg="#660033").place(x=200,y=20)
entry_value = StringVar()
entry = Entry(textvariable=entry_value,bd=6,width=30)
entry.place(x=200,y=60)


button1=Button(window,text="ADD TASK",command=add,font=("Helvetica",10,"bold"),fg="#660033",bg="#99ccff",height=2,width=16).place(x=25,y=130)
button2=Button(window,text="DELETE TASK",command=delete,font=("Helvetica",10,"bold"),fg="#660033",bg="#99ccff",height=2,width=16).place(x=25,y=200)
button5=Button(window,text="SAVE TASK",command=save,font=("Helvetica",10,"bold"),fg="#660033",bg="#99ccff",height=2,width=16).place(x=25,y=270)
button6=Button(window,text="SHOW TASK",command=load_task,font=("Helvetica",10,"bold"),fg="#660033",bg="#99ccff",height=2,width=16).place(x=180,y=130)
button3=Button(window,text="RESET",command=reset,font=("Helvetica",10,"bold"),fg="#660033",bg="#99ccff",height=2,width=16).place(x=180,y=200)
button4=Button(window,text="EXIT ",command=exit,font=("Helvetica",10,"bold"),fg="#660033",bg="#99ccff",height=2,width=16).place(x=180,y=270)
text=Listbox(window,width=35,height=11,bd=5)
text.place(x=335,y=130)
window.mainloop()


