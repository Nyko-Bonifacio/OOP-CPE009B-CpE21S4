from tkinter import*

class MyWindow:
    def __init__(self, win):
        self.Label1=Label(win, bg="Blue", fg="Red", text="Calculator", font=("Impact", 35))
        self.Label1.place(x=100, y=10)

        self.Label2=Label(win, bg="Red", fg="Blue", text="Number 1:", font=("Impact", 18))
        self.Label2.place(x=75, y=90)
        self.Entry1=Entry(win, bd=8)
        self.Entry1.place(x= 190, y=90)

        self.Label3 = Label(win, bg="Black", fg="Gray", text="Number 2:", font=("Impact", 18))
        self.Label3.place(x=75, y=130)
        self.Entry2 = Entry(win, bd=8)
        self.Entry2.place(x=190, y=130)

        self.Label4 = Label(win, bg="Yellow", text="Result:", font=("Impact", 18))
        self.Label4.place(x=75, y=170)
        self.Entry3 = Entry(win, bd=8)
        self.Entry3.place(x=190, y=170)

        self.Button1=Button(win, bd=4, bg="LightGreen", fg="Blue", text="ADD", font=("Impact", 14), command=self.add)
        self.Button1.place(x=50, y=230)

        self.Button2 = Button(win, bd=4, bg="LightBlue", fg="Violet", text="SUBTRACT", font=("Impact", 14), command=self.sub)
        self.Button2.place(x=100, y=230)

        self.Button3 = Button(win, bd=4, bg="Brown", fg="White", text="MULTIPLY", font=("Impact", 14), command=self.multiply)
        self.Button3.place(x=200, y=230)

        self.Button4 = Button(win, bd=4, bg="Gray", fg="Brown", text="DIVIDE", font=("Impact", 14), command=self.divide)
        self.Button4.place(x=290, y=230)

    def add(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def multiply(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def divide(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))
window = Tk()
MyWin=MyWindow(window)

window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.configure(bg='Orange')
window.mainloop()
