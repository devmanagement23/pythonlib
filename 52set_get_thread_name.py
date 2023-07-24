from threading import Thread,current_thread

def disp():
    print("Child Thread Object",current_thread())       
    print("child thread name:",current_thread().getName())

t = Thread(target=disp)
t.start()

print("Main Thread / Main thread Object",current_thread)
print("Main Thread Name:",current_thread().getName())
print("Main Thread  Name property:",current_thread().name)
