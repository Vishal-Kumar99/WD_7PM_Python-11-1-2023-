#list constructor is list()
#list literal is []
#list is a set of sequence of element(s) 
#list is mutable
# list support slicing 
# list support indexing 
# In python list assume like array but it is not an array.
#list support concatination.

a=list()
print(a)

b=[]
print(a)

#indexing
c=[1,"krishna",10.0,complex(),4+2j]
print(c)

print(c[1])
print(c[3])

#slicing
print(c[1:4])   #['krishna', 10.0, 0j]
print(c[::])    #[1, 'krishna', 10.0, 0j, (4+2j)]
print(c[:])     #[1, 'krishna', 10.0, 0j, (4+2j)]
print(c[0:])    #[1, 'krishna', 10.0, 0j, (4+2j)]
print(c[::1])   #[1, 'krishna', 10.0, 0j, (4+2j)]

print(c[::-1])  #[(4+2j), 0j, 10.0, 'krishna', 1]

d=[1,2,3,40]
e=[5,6,7,8]
print(d+e)#[1,2,3,40,5,6,7,8]   # for concatination both operand must be of same datatype
print("krishna"+"kumar")        #concatination supported by list and string both
# print(d-e)  this is an error

# print(d*e)  this is an error

# print(d/e)  this is an error 

print("1"+"krishna")

#methods:

f=list()   #[]
print(f, type(f),id(f))

f.append(1)
print(f)
# f.append(1,2,3,4,5)   #TypeError: list.append() takes exactly one argument (5 given)
f.append([1,2,3,4,5])
print(f)

f.clear()    
print(f)     #[]   means empty list

f.extend([1,2,3,4,5])   # string and list both are iterable beacuse it support indexing 
print(f)
f.extend("krishna")
print(f)

print(f.index("k"))
f.extend("kkkkkkk")
print(f)      #[1, 2, 3, 4, 5, 'k', 'r', 'i', 's', 'h', 'n', 'a', 'k', 'k', 'k', 'k', 'k', 'k', 'k']

print(f.index('k'))

f.append(1000000000)
print("f",f)

z=f
print("z",z)

z.append(999999)
print("z",z)
print("f",f)

print("z",id(z))
print("f",id(f))

l=[1,2,3]
print("l",l,id(l))
m=l.copy()
print("m",m,id(m))
m.append(100000)
print("m",m)
print("l",l)



a=[1,2,3,4]
b=[5,6,7,8]

# method of list

c=[1,2,3,4,5]
print(c.count(4))   #count() method count the occurence of similar type of element in a list 

c.extend([4,4,4,4])   # [1,2,3,4,5,4,4,4,4]
print(c)
print(c.count(4))      #count of 4 inside a list c is 5

c.append(1000)
print(c)
c.append([1,2,3,4,5])  #[1,2,3,4,5,[1,2,3,4,5]]
print(c)

c.extend([5,5,6,3,2,4]) #[1,2,3,4,5,[1,2,3,4,5],5,5,6,3,2,4]
print(c)

c.insert(3,3000000)   #insert(index_value,value) #[1, 2, 3, 3000000, 4, 5, 4, 4, 4, 4, 1000, [1, 2, 3, 4, 5], 5, 5, 6, 3, 2, 4]
print(c)

c.pop()    # if we will not mentioned any value inside pop(value) then it will remove the last element of list 
print(c)  

c.pop(6)  # pop(index) :if pop mentioned contain any value inside () then it will remove that element from the list
print(c)

# c.pop(1000)   #IndexError: pop index out of range
# print(c)

print(c.index(2))   # 1 

print(len(c))

print(c[15])

# indexing start from 0
# counting start from 1 when use len()
# maximum index of list = len(c)-1

d=[1,2,3]
d.extend("krishna")  
print(d)             #[1,2,3,'k','r','i','s','h','n','a']

print(len("krishna"))

e=[1,"1",1.0,[1]]
print(e.remove(1))     #None
print(e)         #["1",1.0,[1]]

v=[3,4,2,4,5,6,7]
v.sort()
print(v)  #[2, 3, 4, 4, 5, 6, 7] bydefault sort it in ascending order 

v.sort(reverse=True)
print(v)   #[7,6,5,4,4,3,2]



