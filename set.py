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

# methods of set

a=set()
print(a.add(1))
print(a)

a.add(1)
print(a)

a.add(1.0)  #this is exception 1 and 1.0 are same 2 and 2.0 and soon are same.
print(a)

a.add("krishna")
print(a)
# a.add({1,2,3,4,5})   #set is unhashable or mutable which is not allowed inside a set
#to read documentation of any method use ctrl+shift+space bar

a.add((1,2,3,4))
print(a)

# a.add([1,2,3,4])  #list is unhashable or mutable which is not allowed inside a set

print(a)

b=a
print("b",b)

print("b",b,id(b),type(b))
print("a",a, id(a),type(a))

#copy()
c=a.copy()
print("c",c,id(c),type(c))

c.clear()
print(c)     #set()

a={1,2,3}
b={1,4,5}
print(a.difference(b))   #{2,3}
print(a)    #{1,2,3}

print("it is a parmanent change",a.difference_update(b))  #None
print("a :",a)     #{2,3}

print(a.discard(2))
print(a)

a.discard(10000)
print(a)

c={1,2,3}
d={2,3,4}
print(c.intersection(d))  #{2,3}
print(c)   #{1,2,3}

print(c.intersection_update(d))  #None
print(c)      #{2,3}

e={1,2,3}
f={4,5,6}
print(e.isdisjoint(f))

krishna={4,5,6}
sunil={1,2,3,4,5,6}
print(krishna.issubset(sunil))

print(krishna.issuperset(sunil))

krishna.pop()

print("krishna",krishna)

#Note: array store value but other collection like list tuple set store id of the values

#Note: pop() method in set will remove last id which will read by interpreter from hashing table.

a={1,2,3,4,6}
print(a.pop())
print(a)
b={2,3,4,6}
print(b.remove(3))
print(b)

k={1,2,3}
l={2,3,4}
print(k.symmetric_difference(l))   #{1,4}

print(k.symmetric_difference_update(l))   #None
print(k)  #{1,4}

x={1,2,3,4}
y={3,4,5,6}
z={11,21,31,41}
print(x.union(y,z))

print(z.update({101,201,301,401,501}))
print(z)

print(z.update([102,202,302,402,502]))
print(z)

print(z.update(10000000000))
print(z)


