from tkinter import * 
root = Tk()

root.title("My Name")
root.geometry("500x500")

enter = Entry(root)
enter.place(relx=0.5,rely=0.5,anchor=CENTER)

label = Label(root)
label.place(relx=0.5,rely=0.7,anchor=CENTER)

def get():
    name = enter.get()
    all_let = name.split()
    let = name[0]
    label["text"]="Your Name First Letter Is: "+let


btn = Button(root,text="Get First Letter",command=get)
btn.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()