#strftime() ->  This method convert the object into a specified format and returns the formatted string

from datetime import datetime

dt = datetime.today()

print(dt)
print()

newd1 = dt.strftime("%a  %B,%d,%Y")
print(newd1)                    # Sun  July,23,2023
print()

newd2 = dt.strftime("%A  %d,%b,%Y")
print(newd2)                   # Sunday  23,Jul,2023
print()

newd3 = dt.strftime("%d/%b/%Y")
print(newd3)
print()                       #   23/Jul/2023

newd4 = dt.strftime("%d-%m-%Y")
print(newd4)
print()                        #   23-07-2023

newd5 = dt.strftime("%H:%M:%S")
print(newd5)
print()                         #  17:20:42

newd6 = dt.strftime("%I:%M:%S")
print(newd6)
print()                         #  05:20:42

newd7 = dt.strftime("%B,%d,%Y")
print(newd7)
print()                            # July,23,2023