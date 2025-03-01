

# purse = dict()
# purse["money"]= 12
# purse["cards"]= 3
# purse["tissues"]= 34
# print(purse)
# print(purse["cards"])
# purse["money"]=purse["money"]+1
# print(purse)
# print(purse["cards"])

# purse["money"]=2344
# print(purse)

# ooo = {}
# print(ooo)

# count = dict()
# names=["jasm","inuu","tinuu","sinuu","sinuu"]
# for name in names:
#     if name not in count:
#         count[name] = 1
#     else:
#         count[name]=count[name]+1
# print(count)


count=dict()
places = ["sgr","sgr","sgr","del"]
for place in places:
    if place not in count:
        count[place]=1
    else:
        count[place]=count[place]+1
print(count)


count = dict()
names = ["tabb","tabz","tabi","tabb"]
for name in names:
    count[name]=count.get(name,0)+1
print(count)
        
    