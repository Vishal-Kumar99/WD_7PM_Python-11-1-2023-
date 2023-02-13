#dictionary constructor is dict()
# dictionary literal is {}
# dictionary is a combination of key(s) and value(s) pair.
# dictionary key must be immutable datatype(hashable datatype).
# dictionary value may or may not be immutable.
# dictionary doesnot support indexing but key treated as index value
# dictionary is also a set of sequence of items.
# items are know as combination of key and values .
# dictionary doesnot support slicing.

a=dict()     #constructor used to create a empty dictionary
print(a,type(a),id(a))
b={}        #literal to create an empty dictionary
print(b)

c={1:"krishna",2:"Rahul",3:"Mohan",4:"Sohan"}
print(c)

print(c[1]) #'krishna'

c[1]="Sohan"

print(c)   #{1: 'Sohan', 2: 'Rahul', 3: 'Mohan', 4: 'Sohan'}

c.update({1:"krishna"})
print(c)   #{1: 'krishna', 2: 'Rahul', 3: 'Mohan', 4: 'Sohan'}

#1.key must be unique
#2. key must be immutable(int,float,string,tuple)
#3. values may or may not immutable(all datatype are accepted)
c.update({5:"krishna"}) #{1: 'krishna', 2: 'Rahul', 3: 'Mohan', 4: 'Sohan',5: 'krishna'}
print(c)

d={"name":"krishna","father":"Sunil","Mother":"Suman"}
print(d)

e={1.9:"suger",2.0:"rice",4.23:"meat"}
print(e)

f={(27,78):"krishna",(20,52):"Hyder"}
print(f)

g={1:["krishna","Sunil","Suman"],
2:{"Mohan","Sohan","Sunita"},
3:{"name":"Sunita","Father":"Mr. Sharma","Mother":"Mrs. Sharma"},
4:["Tinku","Mohan","Angle"],
5:3j,
6:True}

print(g)

h=dict()
print(h)
h.update({1:"krishna",2:"Moni",3:"Rashmi",4:"Ayush",5:"Mohan"})    #update --> only except a key value pair(dictionary)
print(h)

print(h.keys())

print(h.values())

print(h.pop(1))

print(h)   #{2: 'Moni', 3: 'Rashmi', 4: 'Ayush', 5: 'Mohan'}

print(h.popitem())  #{2: 'Moni', 3: 'Rashmi', 4: 'Ayush'}
print(h)

print(h.items())   #   [(2,"Moni"),(3,"Rashmi"),(4,"Ayush")]

print(h.get(2))

print(h.get(10,"This key is not available"))
print(h.get(10))

i={}
i.setdefault(1,None)
print(i)

i[1]="krishna"
print(i)
i[1]=None
print(i)

i.update({1:"krishna"})
print(i)