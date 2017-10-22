

class Person(object):
    
    perCount = 0

    def __init__(self, name, sex, birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday
        Person.perCount += 1
        
    def getPersonInfo(self):
        print "name: %s, sex: %s, birthday: %s" %(self.name, self.sex, self.birthday)
 
    def getPerCount(self):
        print "perCount: ", self.perCount
    
person = Person("aaa", "f", "1991-09-23")       
person.getPersonInfo()
person.getPerCount()


person.money = 2000
print person.money
del person.money
print hasattr(person, "age")
print getattr(person, "name")
setattr(person, "sex", "m")
person.getPersonInfo()






