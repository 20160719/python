
print "welcome to python"

def add(x, y) :
    return x + y

def multi(x):
    return x ** 2

def f(x):
    return x % 2 == 0

lam = lambda x: x ** 3

list = [1, 3, 5, 7, 9, 12]

print "x + y = ", add(3, 5)

for r in range(5):
    print "r1: ", r
    
for r in range(0, 5):
    print "r2: ", r
    
for r in range(0, 5, 5):
    print "r3: ", r
    
for i in list :
    print "i: ", i
    
print "max: ", max(list)

print "min: ", min(list)
    
print "map: ", map(multi, list)

print "lambda: ", map(lam, list)

print "filter: ", filter(f, list)

print "reduce: ", reduce(add, list)

it = iter(list)

while True:
    try:
        x = next(it)
        print "x: ", x
    except StopIteration:
        break    
    






