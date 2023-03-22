#import second
#print(second.a)
#print(second.b)
#second.add()

#from second import a,b,add
#print(a)
#print(b)
#add()

#from second import *
#print(a)
#print(b)
#add()

#How to import package
#import Package.third
#print(Package.third.c)
#print(Package.third.d)
#Package.third.sub()

#import Package.third as a
#print(a.c)
#print(a.d)
#a.sub()

#from Package import third

#print(third.c)
#print(third.d)
#third.sub()

#from Package import third as k
#print(k.c)
#print(k.d)
#k.sub()

from Package.third import *
print(c)
print(d)
sub()
