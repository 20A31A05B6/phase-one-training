#day 6
from translate import translator

obj=translator(from_lang="english",to_lang="hindi")
new_name=obj.translate("ajay")
print(new_name)
##polymorphism__overloading
def m1(a,b):
    print(a+b)
def m1(a,b,c):
    print(a*b*c)
print(m1(10,20))
print(m1(10,20,30))
#overriding_same method with diff clss
#overloading_same method with diff parameters
#abstract....anotyation starts with "@"
from abc import ABC

class Area(ABC):
    @abstract method
    def calculate_area(self):
        pass
class square(ABC):
    def calculate_area(self):
        print("in square class")
class rectanle(ABC):
    pass
ob=square()
ob.calculate_area()


    
    
