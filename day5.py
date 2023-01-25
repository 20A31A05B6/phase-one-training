'''#day5
#inheritance
#example
class A:
    name="Mukesh"
    age=36
class B(A):
    age=10
obj=B() 
#obj.name="ramesh" or example taking from same obj
print(obj.age)
print(obj.name)
#example2_single and multilevel inheritance
class Hospital1:
    sr_doctor="rakesh"
    work="eye_specialist"
class Hospital2(Hospital1):
    sr_doctor="dp"
    work="heart_specialist"
class Hospital3(Hospital1):
    work="medicinespecialist"
obj=Hospital3()
print(obj.work)
print(obj.sr_doctor)
#heriarchical inheritance'''
class insta:
    login="ajay1"
    sign_up=""
    forgot_pas="asd123"
    def func1(self):
        self.login
        self.sign_up
        self.forgot_pas
class account1(insta):
    username="ajay"
    password="122345"
    def fun2(self):
      print(self.username)
      print(self.password)

obj1=account1()
print(obj1.username)
print(obj1.forgot_pas)
obj1.fun2()

class account2(insta):
    username="prasad"
    password="1245875"
    def fun3(self):
      print(self.username)
      print(self.password)
obj2=account2()
obj2.fun3()
#####
#multiple inheritance example
'''class heroine1:
    heroine1_name=""
    def heroine1(self):
        print(self.heroine1_name)
class heroine2:
    heroine2_name=""
    def heroine2(self):
        print(self.heroine2_name)
class hero(heroine1,heroine2):
    def main_role(self):
        print("heroine1:",self.heroine1_name)
        print("heroine2:",self.heroine2_name)
s1=hero()
s1.heroine1_name="shruti"
s1.heroine2_name="rose"
s1.main_role()
####
from random imort,randint

a=randint(1,10)
id=random()*1000
print(id)'''

choice=['rock','paper','scissor']
p_score=0
c_score=0
limit=3
while p_score!=limit and c_score!=limit:
    print(f"choose among the following:",choice)
    my_ch=input("player choice:").lower()
    if my_ch not in choice:
       print("Invalid input")
        continue
    sys_ch=choice[int(randint(0,2))]
    print(f")
   

    
    
    
    

    



