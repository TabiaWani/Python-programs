str= "hello beautiful world"
abc = str.split()
print(abc)
print(str)
print(len(abc))
print(str[1])
print(abc[1])
for w in abc:
    print(w)
    
    
str = " a line full of           spaces"
abc = str.split()
print(abc)

strr = "first;second;third"
thing = strr.split()
print(thing)
print(len(thing))
thing=strr.split(';')
print(thing)
print(len(thing))