
#git init
#git remote add origin {link to remote repo}
#git add .
#git commit -m "initial commit"
#git push origin master



#l[start:end:step size]  #slice
l=[1,2,3,4,5,6,7,8,9]
print(l)
print(l[0:6])
print(l[0:10:2])
print(l[1:])
print(l[::2])
print(l[::-1]) #reversing the list
print(l[-5]) #negative indexing......giving elelment from the last end in index
#fibonaaci series
#string methods
s="hello world"
print(s)
print(s.capitalize())
a=s.split()
print(a)
print('-'.join(a))
#print(title())
s1="ajay"
s2="HII"
s3="hELLo"
print(s1.upper())
print(s2.lower())
s4=s3.swapcase()
print(s4)
#######################
num=3.14
print("the square of {} is {:.6f}".format(num,num*num))
#############program :expection handing ..tryand expect
a=int(input('enter a:'))
b=int(input('enter b:'))
try:
    print(a/b)
except:
    print("cannot be 0")
    print("after the error")
######
a=int(input("enter a number:"))
 #### example
try:
     arr=list(map(int, input().split('')))
     print(arr)
except:
        print("enter integer input")
#####
print(eval("1+3/5*8"))

