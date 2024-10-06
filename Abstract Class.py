from abc import ABC, abstractmethod

class AbsClass(ABC):
    
    def print(self, x):
        print("Passed Value:", x)
        
    def task(self):
        print("We are Inside AbsClass Task")
        
        
class test_class(AbsClass):
    def task(self):
        print("We are Inside Test_Class Task")
        

test_obj = test_class()
test_obj.task()
test_obj.print(100)
        
        