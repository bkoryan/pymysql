# Mysql-Python Practice - dB Connection
# 15-07-2021 
# @bkoryan

import mysql.connector
import datetime 
def create_db():
    
    print("dB creating...")

def main():
    
    
    hostname = input("enter hostname:")
    username = input("enter username:")
    pwd = input("enter pass:")

    try:
        mydb = mysql.connector.connect(
        host=hostname,
        user=username,
        password=pwd
        )
        print("mydb connection...")
        create_db()
        del hostname
        del username
        del pwd
        mydb.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
main()

