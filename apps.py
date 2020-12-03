
import mysql.connector

cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
cur=cnx.cursor()
#cur.execute("create database mydb;")
cur.execute("use mydb;")
cnx.commit()
cnx.close()

from manages import *
y=input("Do you want to continue with our program: ")

connect()

while(y=='y'):
    a=int(input("To perform insert press 1, else for search press 2"))
    if(a==1):
        name=input("Give the name ")
        club=input("Give the club ")
        country=input("Give the name of the country ")
        age=int(input("Give the age "))
        ovr=int(input("Give the ovr "))
        position=input("Give the position ")
        insert(name,club,country,age,ovr,position)

    elif(a==2) :
       name=input("Give the name: ")
       find_name(name)

    elif(a==3) :
        show_full()

    
    y=input("Do you still want to continue? ")