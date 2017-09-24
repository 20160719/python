

class Person(object):

    count = 0
    
    def __init__(self, name, sex, age):
        print "Person..."
        self.name = name
        self.sex = sex
        self.age = age
        Person.count += 1
    
    def displayCount(self):
        print "person count:", Person.count
    
    def displayDetail(self):
        print "name: %s, sex: %s, age: %d" % (self.name, self.sex, self.age)
        
class Student(Person):
    
    def __init__(self, name, sex, age, classId):
        Person.__init__(self, name, sex, age)
        self.classId = classId
        print "Studend..."
    def displayDetail(self):
        print "name: %s, sex: %s, age: %d, classId: %s" % (self.name, self.sex, self.age, self.classId)
    
p1 = Person("aaa", "m", 20)
p1.displayCount()
p1.displayDetail()

setattr(p1, "height", 170)

#print Person.__dict__

p2 = Person("bbb", "f", 20)
p2.displayCount()
p2.displayDetail()

del p1, p2

s1 = Student("sss", "m", 20, "1001")
s1.displayDetail()




