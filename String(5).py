#Important point about string 
# 1> String constructor is str()
# 2> String literal is string '', "", """""",''''''
# 3> String is a set of sequence of elements
# 4> String is immutable 
# 5> String support indexing
# 6> String support slicing 



# 1> String constructor is str()

a=str()
print(a)


b=""
print(b)

c=''         
print(c)
print(type(c),"c")


# 2> String literal is string '', "", """""",''''''

d=''
print("d",type(d),d)

e=""
print("e",type(e),e)

f=""""""
print("f",type(f),f)

g=''''''
print("g",type(g),g)

k="Rohan"
print(k)
print("k",type(k),k)

# 3> String is a set of sequence of character

l="KRISHNA"
print(l)

print(l[-4])
print(l[3])