from line import line
from cls import clear
import inspect

clear()

x=1
y=353434
z = -343

print(type(x))
print(type(y))
print(type(z))

line()

a = 1.10
b = 1.0
c = -34.43

print(type(a))
print(type(b))
print(type(c))

line()

d = 35e3
e = 12E4
f = -87.7e100
g = 5.5e+12
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(g,type(g))
line()
h = 3+5j
i = 5j
j = -5j
print(h,type(h))
print(i,type(i))
print(j,type(j))
line()

print(inspect.getsource(line))
