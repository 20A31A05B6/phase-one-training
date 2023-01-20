print(bin(64))
print(1 and 64)
#membership operator
l=[1,2,3,4,5,6,7]
print(1 in l)
print(5 not in l)
#identity operator
a=10
#terminary opertor
#list
lst=[1,2,3,4,5,6,7]
lst.append("hello")
lst.append([10,12])
print(lst)
lst.pop(1)
print(lst)
print(lst.remove(5))
print(lst.insert(4,18))
print(lst)
a=[10,29,30,45]
b=[10,20,30,66]
a.extend(b)
print(a)
c=a.count(10) #count is same for list,tuple,set
print(c)
a.reverse()
print(a)
q=[1,5,4]
w=sorted(q)
print("w=",w)
#typecasting
a=int('1')
b=3
c=a+b
print(c)
a='mr.dp '
b=str(60)
c=' years old'
g=a+b+c
print(g)
#map
a="12345"
b=list(a)
print(b)
c=list(map(int,b))
print(c)




