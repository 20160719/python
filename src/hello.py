from _ctypes_test import func

def printme(name) :
    print name
printme("aaa")

def add(x, y):
    return x + y
print add(3, 5)

class Peo(object):
    def __init__(self, name, age):
        self.name = name
        self.age =age
      
    def toStr(self):  
        print self.name, self.age
p = Peo("bbb", 20)
print p.toStr()


