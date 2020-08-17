import mysql.connector

try:
    mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="cHSothTCaR",
            database="cHSothTCaR",
            passwd="IJNRFI6eOd",
            )
except:
    print("Connect to the internet.")
    quit()
else:
    pass

cursor = mydb.cursor()
cursor.execute("delete from otplist where id='CHE001'")
#cursor.execute()
#cursor.execute()
#cursor.execute()
#cursor.execute()
#cursor.execute()
#cursor.execute()
mydb.commit()





