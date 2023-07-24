#setting name of your child thread while defining

from threading import Thread

def disp():
    pass

t = Thread(target=disp,name="Rajkumar Thread")
print(t.name)