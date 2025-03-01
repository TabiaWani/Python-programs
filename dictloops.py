
# count = dict()
# print('enter a line')
# line = input("")
# words=line.split()
# print("words:", words)
# print("counting")
# for word in words:
#     count[word]=count.get(word,0)+1
# print(count)


# count = {"sam":1,"nan":9,"bob":5}
# for key in count:
#     print(key,count[key])
    
    
# jjj = {"bob":6,"bon":8,"nun":9}
# print(list(jjj))
# print(jjj.keys())
# print(jjj.values())
# print(jjj.items())


# kkk = {"bobb":1, "conn":5, "loll":7}
# for aaa,bbb in kkk.items():
#     print(aaa,bbb)
    

name = input("enter the file name")
handle = open(name)
count = dict()
for line in handle:
    words=line.split()
    for word in words:
        count[word]=count.get[word,0]+1

bigcount=None
bigword=None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)