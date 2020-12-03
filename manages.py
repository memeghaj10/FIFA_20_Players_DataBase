import mysql.connector


def connect():
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("create table if not exists FIFA_20(player_name varchar(100),player_club varchar(100),player_country varchar(100),player_age int,player_OVR int,player_position varchar(100));"
        )
    cnx.commit()
    cnx.close()


def insert(name,club,country,age,ovr,position):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute(
        "INSERT INTO FIFA_20 (player_name,player_club,player_country,player_age,player_ovr,player_position) VALUES(%s,%s,%s,%s,%s,%s);",(name,club,country,age,ovr,position,)
    )
    
    cnx.commit()
    cnx.close()


def find_name(name):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("SELECT * FROM FIFA_20 WHERE player_name ="+"'"+name+"'"+";")
   # cnx.commit()
    for x in cur:
        print(x)
    cnx.close()

def find_club(club):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("SELECT * FROM FIFA_20 WHERE player_club ="+"'"+club+"'"+";")
   # cnx.commit()
    for x in cur:
        print(x)
    cnx.close()

def find_country(country):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("SELECT * FROM FIFA_20 WHERE player_country ="+"'"+country+"'"+";")
   # cnx.commit()
    for x in cur:
        print(x)
    cnx.close()

def find_ovr(ovr):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("SELECT * FROM FIFA_20 WHERE player_ovr ="+"'"+ovr+"'"+";")
   # cnx.commit()
    for x in cur:
        print(x)
    cnx.close()

def find_position(position):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("SELECT * FROM FIFA_20 WHERE player_position ="+"'"+position+"'"+";")
   # cnx.commit()
    for x in cur:
        print(x)
    cnx.close()

def update_club(newclub,name):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("UPDATE FIFA_20 SET player_club ="+"'"+newclub+"'"+" WHERE player_name ="+"'"+name+"'"+";")
    cnx.commit()
    cnx.close()

def update_ovr(newovr,name):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("UPDATE FIFA_20 SET player_ovr ="+"'"+newovr+"'"+" WHERE player_name ="+"'"+name+"'"+";")
    cnx.commit()
    cnx.close()

def update_position(newposition,name):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("UPDATE FIFA_20 SET player_position ="+"'"+newposition+"'"+" WHERE player_name ="+"'"+name+"'"+";")
    cnx.commit()
    cnx.close()

def del_record(name):
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("DELETE FROM FIFA_20 WHERE player_name ="+"'"+name+"'"+";")
    cnx.commit()
    cnx.close()

def show_full():
    cnx=mysql.connector.connect(host="localhost",user="root",passwd="Current-Root-Password",database="mydb")
    cur=cnx.cursor()
    cur.execute("SELECT * FROM FIFA_20;")
    for x in cur:
        print(x)
    #cnx.commit()
    cnx.close()


connect()