from time import time,ctime,localtime
from line import *

date = localtime().tm_mday
month = localtime().tm_mon
year = localtime().tm_year

hour = localtime().tm_hour
minute = localtime().tm_min
second = localtime().tm_sec


def mydate():
    print(date,"/",month,"/",year)

def mytime():
    print(hour,":",minute,":",second)

mydate()
mytime()