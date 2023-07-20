from databaseconnection import myconn

'''
# 2. Create database-------------------------------------
str1 = "CREATE DATABASE pythondb1"
curs = myconn.cursor()
curs.execute(str1)

'''

#3 create table---------------------------
# str2 = "CREATE TABLE book(u_id int(4),title varchar(20),Amount float(5,2))"
# curs2 = myconn.cursor()
# curs2.execute(str2)

#4 enter value into table ------------------------------
str3 = "INSERT INTO book VALUES(%s,%s,%s)"
myvalues = (101,"The truth",120)
curs3 = myconn.cursor()
curs3.execute(str3,myvalues)
myconn.commit()


# connection close ---------------------------------------
myconn.close()

if(myconn.is_connected()):
    print("Connection is there")
else:
    print("Connection close from user")