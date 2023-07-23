from datetime import datetime
#datetime()
#datetime.now()
#datetime.today()

dt = datetime(year=2023,month=7,day=21)
dt2 = datetime(year=2023,month=7,day=21,hour=15,minute=37)
dt3 = datetime(2023,7,21,15,37)

print(dt)
print(dt2)
print(dt3)

print("")

ct = datetime.now()
print(ct)
print(ct.year)

print(datetime.now())
print(datetime.now().year)

td = datetime.today()
print(td)

print(td.hour)

print(datetime.today())
print(datetime.today().hour)