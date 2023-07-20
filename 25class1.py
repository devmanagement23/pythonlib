from line import*

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#----------------------------------------
class Student:
    name2 = None
    age2 = None

    def __init__(self,name,age):
        self.name2 = name
        #self.age2 = age

s1 = Student("ram",32)

print(s1.name2)
print(s1.age2)
#----------------------------------------    
lin()

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person1("John", 36)

print(p2)
#----------------------------------------
lin()

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p3 = Person2("John", 36)

print(p3)

line()

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
print("Hello, My name is "+name+" and I'm "+str(age)+" years old.")