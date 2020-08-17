from tkinter import messagebox
import mysql.connector

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

cursor = mydb.cursor()


cursor.execute("SHOW TABLES")
for (table_name,) in cursor:
        print(table_name)

print()

print("OTP\n")
cursor.execute("select * from otplist")
for x in cursor:
    print(x)

print("Teachers\n")
cursor.execute("select * from teacherlist")
for x in cursor:
    print(x)

print("\nStudents\n")
cursor.execute("select * from studentlist")
for x in cursor:
    print(x)
#RunFile
