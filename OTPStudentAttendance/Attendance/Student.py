from tkinter import messagebox
from tkinter import *
import mysql.connector
import datetime

class win:

    def __init__(self , master , db):

        self.master = master
        self.db = db

        self.cursor = self.db.cursor()
        
        self.master.geometry("500x200+500+300")
        self.master.title("Attendance")
        self.master.configure(background='black')
        
        win.v1 = StringVar()
        win.v2 = StringVar()
        win.v3 = StringVar()

        self.titlelab = Label(self.master,text = "Press 'Enter' to lock your response",width=30,justify=CENTER,bg='black',fg='orange')
        self.titlelab.pack(anchor=CENTER)

        self.seplab1 = Label(master,bg='black')
        self.seplab1.pack(anchor=CENTER)

        self.tidentry = Entry(self.master,textvariable=win.v3,width=30,relief=SUNKEN,justify=CENTER,bg='black',fg='orange')
        self.tidentry.insert(0,'Teacher ID')
        self.tidentry.bind("<Enter>",self.tidenter)
        self.tidentry.bind("<Leave>",self.tidleave)
        self.tidentry.bind("<Return>",self.tidclose)
        self.tidentry.pack(anchor=CENTER)

        self.identry = Entry(self.master,textvariable=win.v1,width=30,relief=SUNKEN,justify=CENTER,bg='black',fg='orange')
        self.identry.insert(0,'Student ID')
        self.identry.bind("<Enter>",self.identer)
        self.identry.bind("<Leave>",self.idleave)
        self.identry.bind("<Return>",self.idclose)
        self.identry.pack(anchor=CENTER)

        self.otpentry = Entry(self.master,textvariable=win.v2,width=30,relief=SUNKEN,justify=CENTER,bg='black',fg='orange')
        self.otpentry.insert(0,'OTP')
        self.otpentry.bind("<Enter>",self.otpenter)
        self.otpentry.bind("<Leave>",self.otpleave)
        self.otpentry.bind("<Return>",self.otpclose)
        self.otpentry.pack(anchor=CENTER)

        self.seplab2 = Label(master,bg='black')
        self.seplab2.pack(anchor=CENTER)

        self.enterbutton = Button(self.master,text = "OK",width=30,command=self.verification,bg='black',fg='orange')
        self.enterbutton.bind("<Enter>",self.butenter)
        self.enterbutton.bind("<Leave>",self.butleave)
        self.enterbutton.pack(anchor=CENTER)

        self.msgbox = messagebox


    def identer(self,event):
        self.identry.config(fg='black',bg='orange')
        self.identry.delete(0,'end')

    def idleave(self,event):
        self.identry.delete(0,'end')
        self.identry.insert(0,'Student ID')
        self.identry.config(bg='black',fg='orange')

    def idclose(self,event):
        ident = self.identry.get()
        if ident.strip()=='':
            return
        self.identry.config(bg='black',fg='orange')
        self.identry.unbind("<Enter>")
        self.identry.unbind("<Leave>")


    def tidenter(self,event):
        self.tidentry.config(fg='black',bg='orange')
        self.tidentry.delete(0,'end')

    def tidleave(self,event):
        self.tidentry.delete(0,'end')
        self.tidentry.insert(0,'Teacher ID')
        self.tidentry.config(bg='black',fg='orange')

    def tidclose(self,event):
        tident = self.tidentry.get()
        if tident.strip()=='':
            return
        self.tidentry.config(bg='black',fg='orange')
        self.tidentry.unbind("<Enter>")
        self.tidentry.unbind("<Leave>")

    def otpenter(self,event):
        self.otpentry.config(fg='black',bg='orange')
        self.otpentry.delete(0,'end')

    def otpleave(self,event):
        self.otpentry.delete(0,'end')
        self.otpentry.insert(0,'OTP')
        self.otpentry.config(bg='black',fg='orange')

    def otpclose(self,event):
        otpent = self.otpentry.get()
        if otpent.strip()=='':
            return
        self.otpentry.config(bg='black',fg='orange')
        self.otpentry.unbind("<Enter>")
        self.otpentry.unbind("<Leave>")


    def butenter(self,event):
        self.enterbutton.config(fg='black',bg='orange')

    def butleave(self,event):
        self.enterbutton.config(fg='orange',bg='black')
    

    def verification(self):
        
        listud=[]
        liteach=[]
        sid = win.v1.get()
        sid = sid.strip().upper()
        sotp = win.v2.get()
        sotp = sotp.strip()
        tid = win.v3.get()
        tid = tid.strip().upper()

        if tid == 'Teacher ID'.upper():
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            self.tidentry.bind("<Enter>",self.tidenter)
            self.tidentry.bind("<Leave>",self.tidleave)
            return

        if sid == 'Student ID'.upper():
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            self.identry.bind("<Enter>",self.identer)
            self.identry.bind("<Leave>",self.idleave)
            return

        if sotp == 'OTP':
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            self.otpentry.bind("<Enter>",self.otpenter)
            self.otpentry.bind("<Leave>",self.otpleave)
            return
        
        self.cursor.execute("select id from studentlist")
        
        for x in self.cursor:
            listud.append(x[0])
        if sid not in listud:
            self.msgbox.showwarning("Invalid","Check credentials and try again.")
            self.identry.bind("<Enter>",self.identer)
            self.identry.bind("<Leave>",self.idleave)
            return
        else:
            pass
        
        self.cursor.execute("select id from teacherlist")
        
        for x in self.cursor:
            liteach.append(x[0])
        if tid not in liteach:
            self.msgbox.showwarning("Invalid","Check credentials and try again.")
            self.tidentry.bind("<Enter>",self.tidenter)
            self.tidentry.bind("<Leave>",self.tidleave)
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
            self.otpentry.bind("<Enter>",self.otpenter)
            self.otpentry.bind("<Leave>",self.otpleave)
            return
        

def main():
    try:
        mydb = mysql.connector.connect(
            host="sql12.freemysqlhosting.net",
            user="sql12390476",
            database="sql12390476",
            passwd="CapfLbV68i"
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



