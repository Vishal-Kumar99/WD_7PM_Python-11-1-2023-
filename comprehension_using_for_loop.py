#mutable collection(which contain multiple elemtents seperated with comman(,))
#list comprehension 
#dictionary comprehension
#set comprehension

# [0,1,2,3,4,5,6,7,8,9]

# a=[]
# for i in range(10):
#     a.append(i)
# print(a)

b=[i for i in range(10)]
print(b)

# set comprehension
c=set([i for i in range(10)])
print(c)

d={i for i in range(10)}
print(d)

# dictionary comprehension

e={1:"krishna",2:"Mohan",3:"Shyam",4:"Mohit"}

# f=[1,2,3,4]
# g=["krishna","Mohan","Shyam","Mohit"]

# h={}
# for i,j in zip(f,g):
#     # print(i,":",j)
#     h.update({i:j})
# print(h)


# h={}
# for i,j in zip([1,2,3,4],["krishna","Mohan","Shyam","Mohit"]):
#     # print(i,":",j)
#     h.update({i:j})
# print(h)

k={i:j for i,j in zip([1,2,3,4],["krishna","Mohan","Shyam","Mohit"])}
print(k)


# [i if i%2!=0 for i in [0,1,2,3,4,5,6,7,8,9]]

# a=[]
# c=[]
# for i in range(10):
#     if i%2!=0:
#         a.append(i)
#     else:
#         c.append(i)
# print(a)    
# print(c)

# b=[i for i in range(10) if (i%2!=0)]
# print(b)



# 1,krishna,kumar
# 2,Rohan,Agrawal
# 3,Sohan,Malhotra
# 4,Ranveer,Kapoor

a=[1,2,3,4]
b=["krishna","Rohan","Sohan","Ranveer"]
c=["kumar","Agrawal","Malhotra","Kapoor"]
for i,j,k in zip(a,b,c):
    # print(i,j,k, sep=",")
    # print(f"{i},{j},{k}")
    print("{},{},{}".format(i,j,k))