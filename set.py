# 8. Set      -> set  --> {1,2,3,4}  --> duplicacy not allowed
# set constructor is set()
# set does not have any literal
# set is not a set of sequence of elements.
# set doesnot support indexing and slicing.
# set does not allowed duplicate values.
# set is mutable and mutable means unhashable
# set only allowed hashable datatype(immutable datatype)


a=set()
print(a)  # set() beacuse set doesnot have literal

b={}
print(b)
print(type(b))

c={1}
print(c)
print(type(c))

d={2,1,4,5,6,7,7,7,7,6,6,6,6}
print(d)        #{1, 2, 4, 5, 6, 7}

# a=10
# print("a",a,id(a),type(a))

# b=10
# print("b",b,id(b),type(b))


# c=[1,2,3,4]
# d=[1,2,3,4]
# print("c",c,id(c),type(c))
# print("d",d,id(d),type(d))
# c=d
# print("c",c,id(c),type(c))
# print("d",d,id(d),type(d))

l={1}
print(l)   #immutable --> integer

m={"krishna"}
print(m)     #immutable --> string 

n={1.0}    
print(n)     #immutable --> float

# o={[1,2,3]}
# print(o)     #mutable --> list

p={(1,2,3)}
print(p)       #immutable --> tuple

# q={{1,2,3}}  
# print(q)

print(dir(set()))

r={1,2,3,4,(1,2)}
print(r)