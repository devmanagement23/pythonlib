#########----------list----------------
from line import *

nameOfBoys = ["om","ram","dev","karan","raj","som","tom","rom"]
print(nameOfBoys)

nameOfGirls = list(("geeta","seeta","reeta","meeta"))
print(nameOfGirls)

line()

newListOfGirls = []

for x in nameOfGirls:
    newListOfGirls.append(x)

print("New list of girls are" , newListOfGirls)

line()

newBoyList =[]
for y in nameOfBoys:
    if "om" in y:
        newBoyList.append(y)

print(newBoyList)
print(nameOfBoys)
lin()
newlist2 = [z for z in nameOfBoys if "om" in nameOfBoys]
print(newlist2)

lin()
print(nameOfGirls)