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