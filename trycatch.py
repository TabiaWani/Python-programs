# x = "hello"
# try:
#     y = int(x)
# except:
#     y = -1
# print("first", y)    

# x = '123'
# try:
#     y = int(x)
# except:
#     y = -1
# print("second", y)

x = input("enter a number")
try:
    y = int(x)
except:
    y = -1
    
if y > 0:
    print("nice work")
else:
    print("not a number")
    
    
    
