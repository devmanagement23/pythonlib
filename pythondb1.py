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
# curs3.execute(str3,myvalues)
# myconn.commit()

#5 enter another value in table --------------------------
myvalues2 = (102,"Inner Wisedom","1000")
# curs3.execute(str3,myvalues2)
# myconn.commit()

#6 enter multiple values in the table at once ----------------------
myvalues3 = [(103,'The fake Independence',555),(104,'Four Directions',360),(105,'Living Gods amoung us',870)]
# curs4 = myconn.cursor()
# curs4.executemany(str3,myvalues3)
# myconn.commit()

#7 Extracting datas
'''
str7 = "SELECT * FROM book"
curs7 = myconn.cursor()
curs7.execute(str7)
data = curs7.fetchall()

for booksdata in data:
    print(booksdata)

'''

#8 Deleting data ------------------------------
'''
str8 = "DELETE FROM book where Amount =555"
curs8 = myconn.cursor()
curs8.execute(str8)
myconn.commit()
'''

#9 Updating data --------------------------------
str9 = "UPDATE book SET Amount = 440 WHERE Amount = 360"
curs9 = myconn.cursor()
curs9.execute(str9)
myconn.commit()

# connection close ---------------------------------------
myconn.close()

if(myconn.is_connected()):
    print("Connection is there")
else:
    print("Connection close from user")