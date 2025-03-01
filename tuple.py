tup = ("bob","cop","lop")
print(tup)
print(len(tup))
print(max(tup))
for iter in tup:
    print(iter)

(x,y)=(100,70)
print(y)


d = dict()
d["tab"]=5
d["bob"]=7
d["cop"]=9
for (k,v) in d.items():
    print(k,v)
    
tups=d.items()
print(tups)

print((9,7,8) > (9,78,98))


d = {'a':4,'b':7,'c':8}
t = sorted(d.items())
print(t)

for (k,v) in sorted(d.items()):
    print(k,v)
    
s = {'n':8, 'h':0, 'o':9}
t= sorted(s.items())
print(t)
for (k,v) in sorted(s.items()):
    print(k,v)
    
c = {'b':3,'c':6,'u':9}
tmp = list()
for (k,v) in c.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp , reverse=True)
print(tmp)




# fhand=open("loops.py")
# count = dict()
# for line in fhand:
#     words=line.split()
#     for word in words:
#         count[word]=count.get(word,0)+1

# lst = list()
# for key, val in count.items():
#     newtup = (val, key)
#     lst.append(newtup)
    
# lst=(sorted(lst, reverse=True))
# for val, key in list[:2]:
#   print(key,val)
  
  
c = {'b':60,'c':6,'d':78}
print (sorted ( [ (v,k) for k,v in c.items() ] ) )