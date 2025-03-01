fruits = ["apple", "mango", "banana"]
for fruit in fruits:
    print(fruit)
    
friends = ["zeenat", "tabia", "fiza"]
for friend in friends:
    print("happy us", friend)
print(len(friends))

num = [1,2,3,4]
print(num)
num[2]=5
print(num)
print(len(num))

str = ["tataa","cuuuu","byyy","hiii"]
print(str)
str[2]="nooo"
print(str)

# fruit = "banana"  #will generate error because strings are immutable
# fruit[2]="o"
# print(fruit)

for i in range(3):
    print( i)

friends = ['tab','sam','sol']
print(len(friends))
print(range(len(friend)))

friends = ['tab','sam','sol']
for friend in friends:
    print("happy new year", friend)
    
for i in range(len(friends)):
    friend=friends[i]
    print("happy new year", friend)
    
    
inp = list()
print(type(inp))

inp.append("hi")
inp.append(2)
inp.append("bye")
inp.append("no")
print(inp)

num = [2, 5 , 6, 7 ,9]
print(9 in num)
print(20 not in num)
print(6 in num)

list = ["tania","sania","mania"]
list.sort()
print(list)
print(list[1])

listt = [45,78,99,00,55,77,44]
print(listt[2:5])
print(listt[:])
print(len(listt))
print(max(listt))
print(min(listt))
print(sum(listt))
print(sum(listt)/len(listt))


# total = 0
# count = 0
# while True:
#     inp = input("enter a number:")
#     if inp == "done":
#         break
#     value=float(inp)
#     total=total+value
#     count=count+1
# average = total/count
# print("average:", average)
    
numlist = list()
while True:
    inp = input("enter a number:")
    if inp == "done":
        break
    value=float(inp)
    numlist.append(value)
average= sum(numlist)/len(numlist)
print("average:", average)