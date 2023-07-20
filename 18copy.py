from line import*
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

line()
lin()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y = car.values()

print(x) #before the change
print(y) #before the change

car["color"] = "white"

print(x) #after the change
print(y)

if "model" in thisdict:
  print("Yes, 'model' is one of the keys")