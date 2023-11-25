string = "aaa"
length = len(string)
array =[]
for i in range(0,length):
    if string[i] == string[i+1] and string[i] == string[i+2]:
        array.append(i)
        for j in range (i,length):
            if string[i]!=string[j]:
                array.append(j-1)
print(array)
                