#day4
#keyword argument function
def f(a,b,c):
    pass
f(c=10,b=90,a=180)
#variable
def f(*tyu):
    pass

f(1,2,3,54,"hello")
#repeation operator
l=[1,2,3]*5
print(l)
#packages
#from mypython file import add_n_numbers
a=10
b=20
c=30
d=40
#########
#ops python examplee
class Student:
    student_name="no name"
    def __init__(self,name):
        self.student_name=name
        
s1=Student("mukesh")
s2=Student("Ramesh")
s3=Student("Sukesh")
print(s2.student_name)
####problem
class Student:
    student_name="no name"
    def __init__(self,name):
        self.student_name=name
    def_update_name(self,new_name):
        self.student_name= new_name
s1=Student("mukesh")
s2=Student("Ramesh")
s3=Student("Sukesh")
print(s2.student_name)
    

