from tkinter import Tk, Button

class MyWindow:
    def __init__(self, win):
        self.button = Button(win, text="Click to Change Color", command=self.change)
        self.button.place(x=175, y=175)
        
    def change(self):
        self.button.config(bg="yellow")

window = Tk()
MyWin = MyWindow(window)
window.geometry("500x400")
window.title("Special Midterm Exam in OOP")
window.mainloop()
