# tuple constructor tuple()
#tuple literal is ()
#tuple immutable
#tuple is set of sequence of elements.it contain each and every datatype
# tuple is hashable
# tuple is faster then list 
#tuple support indexing
#tuple support slicing

a=tuple()
print(a)   #()

b=()
print(b)  #()

c=(1,"krishna",1.0,[1,2,3],(1,2,3))
print(c)

print(c[2])
print(c[1:4])

d=(1,2,3,4)

e=[1,2,3,4]

print(d.count(2))    # 1
print(d.index(3))    # 2


a=(1)
print(a)

b=(1,)
print(b)

d=1,2,3,4,5
print(d)

# packing and unpacking

k,l,m,n,o=(1,2,3,4,5)
print(k)
print(l)
print(m)
print(n)
print(o)

k,l,m,n,o=1,2,3,4,5
print(k)
print(l)
print(m)
print(n)
print(o)

k,l="krishna",11

print(type(k),k,"k")

k="krishna",11

print(type(k),k,"k")

