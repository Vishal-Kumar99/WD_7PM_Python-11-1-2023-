def my_findall1(sample,text):
    return [sample for j in [text[i:len(sample)+i] for i in range(len(text))] if j==sample]