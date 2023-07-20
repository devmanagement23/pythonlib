import mysql.connector

'''
myconn = mysql.connector.connect(host="localhost",user="root",passwd="")

if(myconn.is_connected()):
    print("Connection successfull")
else:
    print("ConnectionError")
'''

myconn = mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb1")

if(myconn.is_connected()):
    print("Connection successfull")
else:
    print("ConnectionError")