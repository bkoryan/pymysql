# Mysql-Python Practice - dB Connection 
# 15-07-2021 
# @bkoryan 

import mysql.connector
import datetime 

def main():
        
    #hostname = input("enter hostname:")
    #username = input("enter username:")
    #pwd = input("enter pass:")

    try:
       
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="191200"
        )

        print("dB connection... OK")
        mydb.autocommit = True
        if(mydb.autocommit==True):
            print("autocommit to dB... OK")
        else:
             print("autocommit to dB... error")

        db = mydb.cursor()
        db.execute("create database if not exists testdb")   
        print("creating dB... OK")   
        db.execute("SHOW databases")  
        pingStatus = mydb.ping(reconnect=True,attempts=1,delay=0)

        if pingStatus != None:
            print("PingStatus = ", pingStatus)
        db.execute("use testdb")
        db.execute("CREATE TABLE if not exists stdnt (name VARCHAR(25),lastname VARCHAR(25),id INT(10) auto_increment,primary key (id),std_id INT(10),dateEntry VARCHAR(25),timeEntry VARCHAR(25))")
        mydb.commit()

        print("Select one of the options:\n")
        print("1) Search an entry")
        print("2) Create an entry")
        print("3) Delete an entry")
        print("4) Modify an entry")
        print("5) Exit\n")
        usr_slct = input("Enter :")
        
        if(usr_slct.isalpha()==True or int(usr_slct) > 5 or int(usr_slct) < 1):
            print("wrong! Bye")
            exit()
        elif int(usr_slct) == 1:
            print("How would like to search an entry?")
            print("1) by student number?")
            print("2) by first name?")
            print("3) by last name?")
            usr_src_slct = input("Enter:")
            if(usr_src_slct.isalpha()==True or int(usr_src_slct) > 3 or int(usr_src_slct) < 1):
                print("wrong! Bye")
                exit()
            elif int(usr_src_slct) == 1:
                src_id = input("enter the student id:")
                if(src_id.isalpha()==True):
                    print("wrong entry!")
                    exit()
                else:
                    db.execute("SELECT * FROM stdnt where std_id = @src_id")
            elif int(usr_src_slct) == 2:
                src_id = input("enter the firstname:")
            elif int(usr_src_slct) == 3:
                src_id = input("enter the lastname:")



        elif int(usr_slct) == 5:
            print("Goodbye!...")
            exit()
        elif int(usr_slct) == 2:
            std_name = input("enter std name:")
            std_lname = input("enter std lastname:")
            std_id = input("enter std id:")
            dateEntry = datetime.date.today()
            timeEntry = datetime.datetime.now()
            try:
                std_id = int(std_id)
            except:
                print("error in std id")
                exit()
            if(std_name.isalpha() == False or std_lname.isalpha() == False):
                print("error in std name or lname")
                exit()
            sql_cmd = "INSERT INTO stdnt (name, lastname,std_id,dateEntry,timeEntry) VALUES (%s, %s,%s,%s,%s)"
            val = (std_name, std_lname,std_id,dateEntry,timeEntry)
            db.execute(sql_cmd, val)
            mydb.commit()
            db.execute("SELECT * FROM stdnt")
            #print(db.fetchall(),'\n')
        
            mydb.close()
            print("all ok")
            #db.execute("drop database testdb")
    except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err)) 
main()
