from line import *

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

line()

class Person2:
  name = None
  age = None

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunct(name):
    print("Hello my name is " + name)

p2 = Person2("John", 36)
#p2.myfunct()
print(p2.name)