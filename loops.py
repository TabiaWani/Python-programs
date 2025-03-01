
while True:
    line=input(">")
    if line[0]== "#":
        continue
    if line == 'done':
        break
    print(line)
print("there")


for i in (5,4,3,2,1):
    print(i)
print("yayyyyyyyy")


for i in range(5):
    print(i)
print("hurrrah")
        
        
friends = ["samreen","fiza","soliha"]
for friend in friends:
    print( "Happy Days",friend)
print("done")

largest = -1
print("before", largest)
for the_num in [23, 45, 6, 78, 22]:
    if the_num > largest:
        largest = the_num
    print("largest num is",largest)
    
print("done")


number = 100
print("greatest so far:",number)
for num in [12,23,1,45,6]:
    if num < number:
        number = num
    print("smallest so far is:", number)
print("done")

count = 0
print("before", count)
for iterations in [2,3,4,5,6,7]:
    count=count+1
    print(count,iterations)
print("after", count)

sum = 0
print("before sum is:", sum)
for total_sum in [20,10,30,40,60]:
    sum = sum + total_sum
    print(sum,total_sum)
print("total sum is:", sum)

count = 0
sum = 0
print("before", count,sum)
for value in [20,21,34,56,78]:
    count=count+1
    sum=sum+value
    print(sum,count,value)
print("after", sum,count, sum/count)
    
found = False
print("before", found)
for value in [20,30,45,30,12,3]:
    if value==3:
        found= True
    print(found, value)
print("after", found)


smallest = None
print("before")
for value in [10,20,3,4,5,60]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("after", smallest)