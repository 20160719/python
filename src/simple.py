
score = 80
if score >= 90:
    print "youxiu"
elif score > 80 and score <=90:
    print "lianghao"
elif score > 60 and score <=80:
    print "yiban"
else:
    print "chongkao"    
    
name = "bbb"
if name == "aaa":
    print name
else:
    print "bucunzai"
    
a = 3
b = 2
c = a**b
print "c:",c
c += a
print "c",c

numbers = [1, 2, 3, 4, 5, 6]
even = []
old = []
while len(numbers):
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        old.append(number)

for e in even:
    print "e:", e

for o in old:
    print "o:", o

for index in range(len(old)):
    print "old:", old[index]

print len(old)

arr = range(3);
for a in arr:
    print "a:",a


    
