# fhand = open("first.py")
# print(fhand)

# fhand = open("try.py")
# print(fhand)   #not_found bcx file doesnt exist


# str = "hello\nworld"   # \n refers to start a new line
# print(str)
# print(len(str))

# fhand = open("loops.py")
# count = 0
# for line in fhand:
#   
# 
#  count = count + 1
# print("line count is:", count)

# fhand = open("loops.py")
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# fhand = open("loops.py")
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith("from:"):
#         print(line)

fhand = open("loops.py")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("from"):
        continue
    print(line)
    
# fhand = input("enter the file name:")
# fhand = open(fhand)
# count = 0
# for line in fhand:
#     if line.startswith("from"):
#         count=count+1
# print("count is:", count)

fname = input("enter file name:")
try:
    fhand=open(fname)
except:
    print("file does not open")
    quit()
    
count=0
for line in fhand:
    if line.startswith("from"):
        count=count+1
print(count)
    