
import mysql.connector

cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
cur=cnx.cursor()
#cur.execute("create database mydb;")
cur.execute("use mydb;")
cnx.commit()
cnx.close()

from manages import *

op=input("Do you want to run this program?[Y:N] ")

while(op=='Y'):

    print("Menu Program for the App!!!")
    print("")
    print("1. Add a new Player....!!!!")
    print("2. Search for a new Player.....????")
    print("3. Update/Upgrade your players....!!!!")
    print("4. Delete record of a player")
    print("5. See the entire list of FIFA_20 FUT")
    print("")
    ch=input("Enter your choice: ")

    if(ch=="1"):
        name=input("Enter Name of the Player: ")
        club=input("Enter Club of the Player: ")
        country=input("Enter the nationality of the Player: ")
        age=int(input("Enter the age of the Player: "))
        ovr=int(input("Enter the OVR of the Player: "))
        position=input("Enter the position of the Player: ")

        insert(name,club,country,age,ovr,position)
        print("")
        print("Player Inserted!!!")

    elif(ch=="2"):
        print("Menu for searching.....")
        print("")
        print("Press 'a' for searching using Name")
        print("Press 'b' for searching using OVR")
        print("Press 'c' for searching using Club")
        print("Press 'd' for searching using Country")
        print("Press 'e' for searching using Position")
        print("")
        u=input("Enter  your choice: ")

        if(u=="a"):
            name=input("Enter Name of the Player: ")
            find_name(name)
            print("")
        
        elif(u=="b"):
            ovr=int(input("Enter the OVR of the Player: "))
            find_ovr(ovr)
            print("")

        elif(u=="c"):
            club=input("Enter club of the player: ")
            find_club(club)
            print("")

        elif(u=="d"):
            country=input("Enter country of the player: ")
            find_country(country)
            print("")

        elif(u=="e"):
            position=input("Enter the position of the Player: ")
            find_position(position)
            print("")

    
    elif(ch=="3"):

        print("Menu for updating.....")
        print("")
        print("Press 'a' for updating OVR")
        print("Press 'b' for updating Club")
        print("Press 'c' for updating Position")
        print("")
        u=input("Enter  your choice: ")

        if(u=="b"):
            club=input("Enter newClub of the Player: ")
            name=input("Enter Name of the Player: ")
            update_club(club,name)
            print("")
        
        elif(u=="a"):
            ovr=int(input("Enter newOVR of the Player: "))
            name=input("Enter Name of the Player: ")
            update_ovr(ovr,name)
            print("")

        elif(u=="c"):
            position=input("Enter newPosition of the player: ")
            name=input("Enter Name of the Player: ")
            update_position(club,name)
            print("")


    elif(ch=='4'):
        name=input("Enter name of the Player: ")
        del_record(name)


    elif(ch=='5'):
        print("")
        show_full()
        print("")



    op=input("Do you want to run this program?[Y:N] ")
