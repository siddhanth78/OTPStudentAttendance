from tkinter import *
from tkinter import messagebox
import os

class win:

    x = os.getcwd()
    x = x.replace('\\','/')

    def __init__(self , master):
        
        self.master = master
        master.geometry("500x150+500+300")
        master.title("Attendance")
        
        win.v1 = IntVar()
        win.v2 = IntVar()
        
        self.titlelab = Label(self.master,text = "Student Attendance",width=25)
        self.titlelab.grid(row=0,column=0)
        
        self.c1 = Checkbutton(self.master,variable=win.v1,text="Teacher")
        self.c1.grid(row=1,column=0)

        self.c2 = Checkbutton(self.master,variable=win.v2,text="Student")
        self.c2.grid(row=1,column=1)

        self.okbutton = Button(self.master,text="OK",width=25,command = self.choice)
        self.okbutton.grid(row=2,column=0)

        self.msgbox = messagebox

    def choice(self):
        
        teach = win.v1.get()
        stud = win.v2.get()
        
        if teach==1 and stud==0:
            self.master.destroy()
            os.system(win.x+"/Teacher.py")
        elif teach==0 and stud==1:
            self.master.destroy()
            os.system(win.x+"/Student.py")
        else:
            self.msgbox.showwarning("Invalid","Please select one box.")
            return


def main():
    root = Tk()
    win(root)
    root.mainloop()

if __name__ == "__main__":
    main()

