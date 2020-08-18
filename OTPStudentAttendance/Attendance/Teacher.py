import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random
import datetime
import os
import time


class win:

    x = os.getcwd()
    x = x.replace("\\","/")
    x = x+"/Attendance"

    def __init__(self , master , db):

        self.master = master
        self.db = db
        
        self.master.geometry("730x300+300+300")
        self.master.title("Attendance")
        
        self.cursor = self.db.cursor(buffered=True)

        win.v1 = StringVar()
        win.v2 = StringVar()
        win.v3 = StringVar()
        win.v4 = StringVar()

        win.v5c = IntVar()
        win.v5b = IntVar()
        win.v5p = IntVar()
        
        win.v6h = IntVar()
        win.v6k = IntVar()
        win.v6s = IntVar()
        win.v6f = IntVar()
        
        win.v7h = IntVar()
        win.v7k = IntVar()
        win.v7s = IntVar()
        win.v7f = IntVar()

        self.titlelab = Label(self.master,text = "Press 'Enter' to lock your response",width=50)
        self.titlelab.pack(anchor=CENTER)

        self.attbut = Button(self.master,text = "Attendance Records",width=50,bg="powder blue",command = self.att)
        self.attbut.pack(anchor=CENTER)

        self.seplab1 = Label(master)
        self.seplab1.pack(anchor=CENTER)

        self.identry = Entry(self.master,textvariable=win.v1,width=50,relief=SUNKEN,justify=CENTER)
        self.identry.insert(0,'Teacher ID')
        self.identry.config(state='disabled')
        self.identry.bind("<Enter>",self.identer)
        self.identry.bind("<Leave>",self.idleave)
        self.identry.bind("<Return>",self.idclose)
        self.identry.pack(anchor=CENTER)

        self.passentry = Entry(self.master,textvariable=win.v4,width=50,relief=SUNKEN,justify=CENTER)
        self.passentry.insert(0,'Password')
        self.passentry.config(state='disabled')
        self.passentry.bind("<Enter>",self.passenter)
        self.passentry.bind("<Leave>",self.passleave)
        self.passentry.bind("<Return>",self.passclose)
        self.passentry.pack(anchor=CENTER)

        self.classentry = Entry(self.master,textvariable=win.v2,width=50,relief=SUNKEN,justify=CENTER)
        self.classentry.insert(0,'Class')
        self.classentry.config(state='disabled')
        self.classentry.bind("<Enter>",self.classenter)
        self.classentry.bind("<Leave>",self.classleave)
        self.classentry.bind("<Return>",self.classclose)
        self.classentry.pack(anchor=CENTER)

        self.secentry = Entry(self.master,textvariable=win.v3,width=50,relief=SUNKEN,justify=CENTER)
        self.secentry.insert(0,'Section')
        self.secentry.config(state='disabled')
        self.secentry.bind("<Enter>",self.secenter)
        self.secentry.bind("<Leave>",self.secleave)
        self.secentry.bind("<Return>",self.secclose)
        self.secentry.pack(anchor=CENTER)

        self.seplab2 = Label(master)
        self.seplab2.pack(anchor=CENTER)

        self.menubutton4 = Menubutton(self.master, text = "IV Subject", relief = RAISED,bg="powder blue",width=50)  
        self.menubutton4.pack(anchor=CENTER)
        self.menubutton4.menu = Menu(self.menubutton4)  
        self.menubutton4["menu"]=self.menubutton4.menu  
        self.menubutton4.menu.add_checkbutton(label = "Computers", variable=win.v5c)  
        self.menubutton4.menu.add_checkbutton(label = "Biology", variable=win.v5b)  
        self.menubutton4.menu.add_checkbutton(label = "PE", variable = win.v5p)
        self.menubutton4.pack()

        self.menubutton = Menubutton(self.master, text = "II Language", relief = RAISED,bg="powder blue",width=50)  
        self.menubutton.pack(anchor=CENTER)
        self.menubutton.menu = Menu(self.menubutton)  
        self.menubutton["menu"]=self.menubutton.menu  
        self.menubutton.menu.add_checkbutton(label = "Hindi", variable=win.v6h)  
        self.menubutton.menu.add_checkbutton(label = "Kannada", variable=win.v6k)  
        self.menubutton.menu.add_checkbutton(label = "Sanskrit", variable = win.v6s)
        self.menubutton.menu.add_checkbutton(label = "French", variable = win.v6f)
        self.menubutton.pack()

        self.menubutton2 = Menubutton(self.master, text = "III Language", relief = RAISED,bg="powder blue",width=50)  
        self.menubutton2.pack(anchor=CENTER)
        self.menubutton2.menu = Menu(self.menubutton2)  
        self.menubutton2["menu"]=self.menubutton2.menu  
        self.menubutton2.menu.add_checkbutton(label = "Hindi", variable=win.v7h)  
        self.menubutton2.menu.add_checkbutton(label = "Kannada", variable=win.v7k)  
        self.menubutton2.menu.add_checkbutton(label = "Sanskrit", variable = win.v7s)
        self.menubutton2.menu.add_checkbutton(label = "French", variable = win.v7f)
        self.menubutton2.pack()

        self.nslab = Label(self.master,text = "-----",width=50)
        self.nslab.pack(anchor=CENTER)

        self.enterbutton = Button(self.master,text = "OK",width=50,bg="powder blue",command=self.generate)
        self.enterbutton.pack(anchor=CENTER)

        self.msgbox = messagebox


    def identer(self,event):
        self.identry.config(state='normal')
        self.identry.delete(0,'end')

    def idleave(self,event):
        self.identry.insert(0,'Teacher ID')
        self.identry.config(state='disabled')

    def idclose(self,event):
        ident = self.identry.get()
        if ident.strip()=='':
            return
        self.identry.config(state='disabled')
        self.identry.unbind("<Enter>")
        self.identry.unbind("<Leave>")

    def passenter(self,event):
        self.passentry.config(show='*',state='normal')
        self.passentry.delete(0,'end')

    def passleave(self,event):
        self.passentry.insert(0,'Password')
        self.passentry.config(show='',state='disabled')

    def passclose(self,event):
        passent = self.passentry.get()
        if passent.strip()=='':
            return
        self.passentry.config(show='*',state='disabled')
        self.passentry.unbind("<Enter>")
        self.passentry.unbind("<Leave>")

    def classenter(self,event):
        self.classentry.config(state='normal')
        self.classentry.delete(0,'end')

    def classleave(self,event):
        self.classentry.insert(0,'Class')
        self.classentry.config(state='disabled')

    def classclose(self,event):
        clent = self.classentry.get()
        if clent.strip()=='':
            return
        self.classentry.config(state='disabled')
        self.classentry.unbind("<Enter>")
        self.classentry.unbind("<Leave>")

    def secenter(self,event):
        self.secentry.config(state='normal')
        self.secentry.delete(0,'end')

    def secleave(self,event):
        self.secentry.insert(0,'Section')
        self.secentry.config(state='disabled')

    def secclose(self,event):
        self.secentry.config(state='disabled')
        self.secentry.unbind("<Enter>")
        self.secentry.unbind("<Leave>")
        

    def generate(self):
        
        liteach=[]
        tid = win.v1.get()
        tid = tid.strip().upper()
        cl = win.v2.get()
        cl = cl.strip()
        sec = win.v3.get()
        sec = sec.strip().upper()
        passw = win.v4.get()
        passw = passw.strip()

        if tid == 'Teacher ID'.upper():
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            self.identry.bind("<Enter>",self.identer)
            self.identry.bind("<Leave>",self.idleave)
            return

        if cl == 'Class':
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            self.classentry.bind("<Enter>",self.classenter)
            self.classentry.bind("<Leave>",self.classleave)
            return

        if sec == 'Section'.upper():
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            self.secentry.bind("<Enter>",self.secenter)
            self.secentry.bind("<Leave>",self.secleave)
            return

        if passw == 'Password':
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            self.passentry.bind("<Enter>",self.passenter)
            self.passentry.bind("<Leave>",self.passleave)
            return
        
        ssc = win.v5c.get()
        ssb = win.v5b.get()
        ssp = win.v5p.get()

        h2 = win.v6h.get()
        k2 = win.v6k.get()
        f2 = win.v6f.get()
        s2 = win.v6s.get()

        h3 = win.v7h.get()
        k3 = win.v7k.get()
        f3 = win.v7f.get()
        s3 = win.v7s.get()

        if ssc==1 and ssb==0 and ssp==0:
            ss = 'Comp'
        elif ssc==0 and ssb==1 and ssp==0:
            ss = 'Bio'
        elif ssc==0 and ssb==0 and ssp==1:
            ss = 'PE'
        elif ssc==0 and ssb==0 and ssp==0:
            ss=""
        else:
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            return

        if h2==1 and k2==0 and f2==0 and s2==0:
            l2 = 'Hin'
        elif h2==0 and k2==1 and f2==0 and s2==0:
            l2 = 'Kan'
        elif h2==0 and k2==0 and f2==0 and s2==1:
            l2 = 'Sans'
        elif h2==0 and k2==0 and f2==1 and s2==0:
            l2 = 'French'
        elif h2==0 and k2==0 and f2==0 and s2==0:
            l2 = ""
        else:
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            return

        if h3==1 and k3==0 and f3==0 and s3==0:
            l3 = 'Hin'
        elif h3==0 and k3==1 and f3==0 and s3==0:
            l3 = 'Kan'
        elif h3==0 and k3==0 and f3==0 and s3==1:
            l3 = 'Sans'
        elif h3==0 and k3==0 and f3==1 and s3==0:
            l3 = 'French'
        elif h3==0 and k3==0 and f3==0 and s3==0:
            l3 = ""
        else:
            self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
            return

        ss = ss.strip().upper()
        l2 = l2.strip().upper()
        l3 = l3.strip().upper()

        self.menubutton4.config(text=ss)
        self.menubutton.config(text=l2)
        self.menubutton2.config(text=l3)
        
        try:
            
            self.cursor.execute("select id from teacherlist")
            
            for x in self.cursor:
                liteach.append(x[0])
            if tid not in liteach:
                self.msgbox.showwarning("Invalid","Check credentials and try again.")
                self.identry.bind("<Enter>",self.identer)
                self.identry.bind("<Leave>",self.idleave)
                return
            else:
                self.cursor.execute(f"select name,subject from teacherlist where id = '{tid}'")
                for x in self.cursor:
                    na , su = x
                na = na.strip().upper()
                su = su.strip().upper()
                
            self.cursor.execute(f"select passw from teacherlist where id = '{tid}'")
            
            for x in self.cursor:
                passver = x[0]
                
            if passw != passver:
                self.msgbox.showwarning("Invalid","Check credentials and try again.")
                self.passentry.bind("<Enter>",self.passenter)
                self.passentry.bind("<Leave>",self.passleave)
                return
            else:
                pass
            
            self.nslab.config(text = na+" / "+su)
            newotp=random.randint(100000,999999)
            newotp = str(newotp)
            newotp=newotp.strip()

            self.cursor.execute(f"insert into otplist values('{tid}' , '{newotp}')")
            self.db.commit()
            
            dd = datetime.datetime.now().date()
            date = dd.strftime("%x")
            date = date.replace("/","_")
            
            val=[]
            
            if ss=="" and l2=="" and l3=="" and sec!="":
                pass
            elif ss!="" and l2=="" and l3=="" and sec=="":
                pass
            elif ss=="" and l2!="" and l3=="" and sec=="":
                pass
            elif ss=="" and l2=="" and l3!="" and sec=="":
                pass
            else:
                self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
                return

            self.cursor.execute(f"drop table if exists {na}_{cl}{sec}_{su}_{date}")
            self.cursor.execute(f"create table {na}_{cl}{sec}_{su}_{date} (id varchar(6) not null unique , name varchar(20) not null , {date} varchar(10) not null)")

            if ss=="" and l2=="" and l3=="" and sec!="":
                self.cursor.execute(f"select id,name from studentlist where class = '{cl}' and section = '{sec}'")
            elif ss!="" and l2=="" and l3=="" and sec=="":
                self.cursor.execute(f"select id,name from studentlist where class = '{cl}' and combo like '%{ss}%'")
            elif ss=="" and l2!="" and l3=="" and sec=="":
                self.cursor.execute(f"select id,name from studentlist where class = '{cl}' and II_lang = '%{l2}%'")
            elif ss=="" and l2=="" and l3!="" and sec=="":
                self.cursor.execute(f"select id,name from studentlist where class = '{cl}' and III_lang = '%{l3}%'")
            else:
                self.msgbox.showwarning("Invalid","Check the information submitted and try again.")
                self.classentry.bind("<Enter>",self.classenter)
                self.classentry.bind("<Leave>",self.classleave)
                self.secentry.bind("<Enter>",self.secenter)
                self.secentry.bind("<Leave>",self.secleave)
                return
            
            for x in self.cursor:
                idd,nm = x
                liii = (idd,nm,"absent")
                val.append(liii)
                
            sql = f"insert into {na}_{cl}{sec}_{su}_{date} values(%s,%s,%s)"
            self.cursor.executemany(sql,val)
            self.db.commit()
            
            self.msgbox.showinfo("OTP",
                                "OTP : "+newotp+"\nCaution : Leave this message open to accept attendance.\nClose this message to close attendance window.\nThis page will close automatically.")
            
            self.cursor.execute(f"delete from otplist where id = '{tid}'")
            self.db.commit()
            
            self.insertion(na , su , sec , cl , date)
            
            self.cursor.execute(f"drop table {na}_{cl}{sec}_{su}_{date}")
            self.db.commit()
    
            self.master.destroy()
            return
        except:
            dd = datetime.datetime.now().date()
            date = dd.strftime("%x")
            date = date.replace("/","_")
            self.msgbox.showwarning("Error","Something went wrong...")
            self.cursor.execute(f"drop table if exists {na}_{cl}{sec}_{su}_{date}")
            self.cursor.execute(f"delete from otplist where id = '{tid}'")
            self.db.commit()
            self.classentry.bind("<Enter>",self.classenter)
            self.classentry.bind("<Leave>",self.classleave)
            self.secentry.bind("<Enter>",self.secenter)
            self.secentry.bind("<Leave>",self.secleave)
            self.identry.bind("<Enter>",self.identer)
            self.identry.bind("<Leave>",self.idleave)
            self.passentry.bind("<Enter>",self.passenter)
            self.passentry.bind("<Leave>",self.passleave)
            return
        else:
            pass


    def insertion(self , n ,s ,se , c , d):
        
        na = n
        cl = c
        sec = se
        su = s
        cl = c
        date = d
        
        import csv
        
        try:
            self.cursor.execute(f"select * from {na}_{cl}{sec}_{su}_{date}")
            data = self.cursor.fetchall()
            data.insert(0,self.cursor.column_names)
        except:
            self.msgbox.showwarning("Error","Something went wrong...")
            self.cursor.execute(f"drop table if exists {na}_{cl}{sec}_{su}_{date}")
            self.cursor.execute(f"delete from otplist where id = '{tid}'")
            self.db.commit()
            return
        else:
            rows = []
            for j in data:
                sid,nam,p = j
                lii = [sid,nam,p]
                rows.append(lii)
            filen = f"{win.x}/{na}_{cl}{sec}_{su}_{date}.csv"
            with open(filen, 'w') as csvfile:  
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(rows)
            self.msgbox.showinfo("Report","Attendance report has been created and sent.")


    def att(self):
        filename = filedialog.askopenfilename(initialdir = win.x, 
                                        title = "Select a File", 
                                        filetypes = (("csv files", 
                                                    "*.csv*"),
                                                     ("all files", 
                                                    "*.*")))
        os.system(f"{filename}")
        



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
