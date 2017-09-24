from _ctypes_test import func
import time
from __builtin__ import raw_input


def printme(name) :
    print name
printme("aaa")

def add(x, y):
    return x + y
print add(3, 5)

def multi(x):
    return x * x

list = [1, 2, 3, 4]
list.append(5)
list.append(2)

print list.count(2)

print len(list), max(list), min(list)

print map(multi, list)

print reduce(add, list)

tup1 = (1, 2, 3, 4, 5)
print tup1[0], tup1[4]
for t in tup1:
    print t

print tup1[1:5], len(tup1), 3 in tup1

dict = {"name":"aaa", "sex":"m","age":20}
dict["sex"] = "f"
print dict["name"], dict["sex"], dict["age"]
dict.clear()

print time.strftime('%y-%m-%d %H:%M:%S', time.localtime())

sum = lambda a, b : a + b

print "a + b = ", sum(3, 5)

def funx(x):
    def funy(y):
        return x * y
    return funy

print funx(4)(5)

i = 10
def p():
    i = 5
    print "i = ", i

p();
print i

str = raw_input("please input:");
print "your input:", str









