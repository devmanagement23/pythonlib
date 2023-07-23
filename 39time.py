# time() - return time in seconds from epoch

# ctime() - return current date and time when no parameter pass
#         - return time in seconds when epoch as a parameter passed

#localtime() - it return object 

            # convert seconds to date and time.
            # this object has many values along with index no.

from time import time,ctime,localtime
from line import *
from time40 import *

epoch = time()
print(epoch)

lin()   

print(time())

lin()

datetime = ctime(epoch)
print(datetime)

lin()

print(ctime(time()))

lin()

stobj = localtime()
print(stobj)

print("")

print(stobj.tm_year)

lin()

print(localtime())

print("")

print(localtime().tm_year)

print("Today is ",localtime().tm_mday,"/",localtime().tm_mon,"/",localtime().tm_year)

print("")

print("Today is ",stobj.tm_mday,"/",stobj.tm_mon,"/",stobj.tm_year)

print("")

mydate()
mytime()