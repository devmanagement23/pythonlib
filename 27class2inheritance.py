#single Inheritance
class Father:
    money = 1000

    def show(self):
        print("parent class instance method")

    @classmethod
    def showmoney(cls):
        print("ParentClass class method",cls.money)

    @staticmethod
    def stat():
        a = 10
        print("Parent class static method",a)

class Son(Father):
    def disp(self):
        print("child class instance method")

s = Son()
s.disp()
s.showmoney()
print(s.money)
s.show()
s.stat()

print()

f = Father()
f.show()
f.showmoney()
f.stat()