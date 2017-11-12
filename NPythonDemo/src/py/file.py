
seq = ["\n","eee\n","fff\n","ggg"]

f = open("a.txt", "a+")
print "file name: ", f.name
#f.writelines(seq)
#f.flush()
#f.close()

f = open("a.txt", "a+")
print f.readline()
#for line in f.readlines():
#    line = line.strip()
#    print "line: %s" % (line)
#pos = f.tell()
#print "pos %s" %(pos)
f.seek(5, 0)

for index in range(5):
    line = f.next()
    print "%d - %s" %(index, line)
f.close()

try:
    f = open("a.txt", "a+")
    for line in f.readlines():
        line = line.strip()
        print "line: %s" % (line)
except IOError:
    print "Error"
else:
    print "file read success"



