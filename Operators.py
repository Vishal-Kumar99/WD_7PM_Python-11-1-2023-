# Operators --> Operators are symbol use to perform mathematical
# opeartion on operands

# Operends --> The values on which operation done by operators;
#  ex=  2+4 where 2,4 are operands and "+" is a operator.

# Operators are or 7 types:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic Operators--> +,-,/,*,**,//,%

a=10
b=3

c=a+b #13
print(c)

d=a-b
print(d) #7

e=a*b
print(e)  #30

f=a/b
print(f)   #3.33333333333333

g=a//b
print(20//2)

h=a%b
print(h)

i=a**3
print(i)

# Assignment operators
k=10
k=k+10
k+=10   
print(k)

l=20
l=l*10
l*=10
print(l)

m=20
m=m/2
m/=2
print(m)

n=30
n=n**2
n**=2
print(n)

n//=2;   # n=n//2


# Comparison operators

# ==,<=,>=,>,<,!=

print(10==10)
print(10<10)
print(10>10)
print(10<=10)
print(10>=10)
print(10!=10)   # "!=" not equal

print(10=="10")

#Python Logical Operators

# and, or, not
 
print(2==2 and 3==3)   #True
print(2!=2 and 3==3 and 4==4)   #False
print(2!=2 and 3!=3)   #False
print("this is manipulated.",not(2==2 or 3==3)) #True
print(2!=2 or 3==3)  #True
print(2==2 or 3!=3)   #True
print(2<=2 and 3>=3)  #True

# not

print("This is True: ",not True)

# Identity operators: is , is not

a="python"
print(id(a))
b="Python"
print(id(b))

print(a is b )  #"python" is "Python"
print("python" is "Python")  #False

b=[1,2,3,4]
c=[1,2,3,4]
print(b is c)

a="krishna"
print(id(a))
b="krishna"
print(id(b))
print(a is b)

b=[1,2,3,4]
c=b
print(id(b))
print(id(c))
print(b is c)

a=(1,2,3,4)
b=(1,2,3,4)
print(id(a))
print(id(b))
print(a is not b)   #False

# Membership operators : in, not in
a="Python is funny language"
b="Python"
print(b in a)
print(a[0:6],id(a[0:6]))
print(id(b))
print(ord("P"))
print(bin(ord("P")),bin(ord("y")),bin(ord("t")),bin(ord("h")),bin(ord("o")),bin(ord("n")),sep="")
print(str(bin(ord("P")))[2:],str(bin(ord("y")))[2:],str(bin(ord("t")))[2:],str(bin(ord("h")))[2:],str(bin(ord("o")))[2:],str(bin(ord("n")))[2:],sep="")

print(b not in a)  #False

# Bitwise operators
# ~,&,|,<<,>>,^

print(~12)

print()



