
from abc import ABCMeta, abstractmethod
from _pyio import __metaclass__

class People(object):
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def displayDetail(self):
        pass
    
    
class Teacher(People):
    
    def __init__(self, name):
        self.name = name
        
    def displayDetail(self):
        print "name: %s" % (self.name)
        

t = Teacher("aaa")
t.displayDetail()
