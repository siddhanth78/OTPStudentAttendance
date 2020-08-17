from tkinter import messagebox
from tkinter import *
import mysql.connector
import datetime

class win:

    def __init__(self , master , db):

        self.master = master
        self.db = db

        self.cursor = self.db.cursor()
        
        self.master.geometry("500x120+500+300")
        self.master.title("Attendance")
        
        win.v1 = StringVar()
        win.v2 = StringVar()
        win.v3 = StringVar()

        self.titlelab = Label(self.master,text = "Student Attendance",width=25)
        self.titlelab.grid(row=0,column=0)

        self.idlab = Label(self.master,text = "Teacher ID",width=25)
        self.idlab.grid(row=1,column=0)

        self.identry = Entry(self.master,textvariable=win.v3,width=20,relief=SUNKEN)
        self.identry.grid(row=1,column=1)

        self.idlab = Label(self.master,text = "Student ID",width=25)
        self.idlab.grid(row=2,column=0)

        self.identry = Entry(self.master,textvariable=win.v1,width=20,relief=SUNKEN)
        self.identry.grid(row=2,column=1)

        self.otplab = Label(self.master,text = "OTP",width=25)
        self.otplab.grid(row=3,column=0)

        self.otpentry = Entry(self.master,textvariable=win.v2,width=20,relief=SUNKEN)
        self.otpentry.grid(row=3,column=1)

        self.enterbutton = Button(self.master,text = "OK",width=25,command=self.verification)
        self.enterbutton.grid(row=4,column=0)

        self.msgbox = messagebox
    

    def verification(self):
        
        listud=[]
        liteach=[]
        sid = win.v1.get()
        sid = sid.strip()
        sotp = win.v2.get()
        sotp = sotp.strip()
        tid = win.v3.get()
        tid = tid.strip()
        
        self.cursor.execute("select id from studentlist")
        
        for x in self.cursor:
            listud.append(x[0])
        if sid not in listud:
            self.msgbox.showwarning("Invalid","Check credentials and try again.")
            return
        else:
            pass
        
        self.cursor.execute("select id from teacherlist")
        
        for x in self.cursor:
            liteach.append(x[0])
        if tid not in liteach:
            self.msgbox.showwarning("Invalid","Check credentials and try again.")
            return
        else:
            pass
        
        self.cursor.execute(f"select name,class,section from studentlist where id = '{sid}'")
        
        for x in self.cursor:
            nam , cl , sec = x
            
        self.cursor.execute(f"select otp from otplist where id = '{tid}'")
        
        for x in self.cursor:
            otp = x[0]
        otp = str(otp)
        
        if otp==sotp:
            self.cursor.execute(f"select name,subject from teacherlist where id = '{tid}'")
            for x in self.cursor:
                na , su = x
            na = na.strip().upper()
            su = su.strip().upper()
            su = su.replace(" ","_")
            
            if su in ["KANNADA","HINDI","SANSKRIT",
                      "KAN","HIN","SAN","SANS","K","H","S","FRENCH","F",
                      "III_LANG_FRENCH","II_LANG_FRENCH",
                      "II_LANG_KAN","II_LANG_HIN","II_LANG_SAN","II_LANG_SANS",
                      "III_LANG_KAN","III_LANG_HIN","III_LANG_SAN","III_LANG_SANS"]:
                sec=""
            elif "COMP" in su and cl == "11":
                sec=""
            elif "COMP" in su and cl == "12":
                sec=""
            elif "BIO" in su and cl == "11":
                sec=""
            elif "BIO" in su and cl == "12":
                sec=""
            elif "PE" in su and cl == "11":
                sec=""
            elif "PE" in su and cl == "12":
                sec=""
                
            dd = datetime.datetime.now().date()
            date = dd.strftime("%x")
            date = date.replace("/","_")
            self.cursor.execute(f"update {na}_{cl}{sec}_{su}_{date} set {date}='present' where id = '{sid}'")
            self.db.commit()
            self.msgbox.showinfo("Verified","You have been marked 'Present'.\nThis page will close automatically.")
            self.master.destroy()
        else:
            self.msgbox.showwarning("Invalid","Check credentials and try again.")
            return
        

def main():
    try:
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="cHSothTCaR",
            database="cHSothTCaR",
            passwd="IJNRFI6eOd",
            )
    except:
        messagebox.showwarning("Error","Connect to the internet and try again.")
        quit()
    else:
        pass
    root = Tk()
    win(root , mydb)
    root.mainloop()
    

if __name__ == "__main__":
    main()



