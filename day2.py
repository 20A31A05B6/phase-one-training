#day2
#tuple
t=(10,20,30,40,50,60,20)
res=t.index(40)
print(res)
#ven diagram
s1={1,2,3,4,5}
s2={3,4,6,7,8}
s3=s1.intersection(s2)
print(s3)
s4=s1.union(s2)
print(s4)
s5=s1.difference(s2)
print(s5)
#if else
if 10<20:
    print("if block")
else:
    print("else block")
#even or odd
a=99
if a%2==0:
    print("given number is even")
else:
    print("given number is odd")
#prime number checking
r=5
if r%2==0:
    print("given number is prime")
else:
    print("given number is not prime")
 #elif statements
 #syntax for elif
'''if condition 1:
     code1
elif condition 2:
    code2
elif condition 3:
    code3
else condition 4:
    code4 '''
    #elif example week
day=int(input("enter a day between one to seven:"))
if day==1:
    print("it is Monday")
elif day==2:
    print("it is tuesday")
elif day==3:
    print("it is wednesday")
elif day==4:
    print("it is thursday")
elif day==5:
    print("it is friday")
elif day==6:
    print("it is saturday")
elif day==7:
    print("it is sunday")
else:
    print("enter a valid num")
#weried number
n=int(input("enter a number:"))
if n>0 and n<20:
    if(n%2==0):
     print("it is weird number")
    else:
        print("it is normal number")
elif n>=20 and n<30:
    print("normal number")
else:
    if n>30 and n%2==0:
        print("it is normal number")
    else:
        print("it is weird number")
print(list(range(1,10)))
#for loop
print(list(range(1,10)))
for i in range(1,10):
    print(i, end=',')
##
lst=[1,2,3,4,5]
for i in lst:
    print(i*i)
