def my_findall(sample,text):
    return [sample for j in [text[i:len(sample)+i] for i in range(len(text))] if j==sample]

def my_search(a,b):

    cont=[b[i:len(a)+i] for i in range(len(b))]
    k=0
    for i in cont:
        if a==i:
            print(k)
            break
        k+=1

def my_split():
    cont=[]
    pattern=" "
    text="this is krishna"
    str1=""
    k=0
    for i in text:
        if i==pattern:
            cont.append(str1)
            str1=""
            continue
        str1+=i
        k+=1
    else:
        cont.append(str1.strip())
    return cont