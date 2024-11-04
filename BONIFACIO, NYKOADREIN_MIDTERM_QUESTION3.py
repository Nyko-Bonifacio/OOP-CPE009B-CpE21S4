from tkinter import Tk, Label, Button, Entry, END

class MyWindow:
    def __init__(self, win):
        self.label1 = Label(win, text="Enter your fullname:", fg="red")
        self.label1.place(x=50, y=90)
        self.Entry1=Entry(win, bd=5)
        self.Entry1.place(x=280, y=90)
        
        self.button = Button(win, text="Click to display your Fullname", fg="red", command=self.display)
        self.button.place(x=50, y=140)
        self.Entry2=Entry(win, bd=5)
        self.Entry2.place(x=280, y=140)

    def display(self):
        self.Entry2.delete(0, 'end')
        name = str(self.Entry1.get())
        self.Entry2.insert(END, str(name))


window = Tk()
MyWin = MyWindow(window)
window.geometry("600x300")
window.title("Midterm in OOP")
window.mainloop()