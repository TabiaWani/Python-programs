str1 = " hello "
str2 = "there"
bob = str1 + str2
print(bob) 

str = '123'
x = int(str)+ 1
print(x)

str = "banana"
print(str[3])

str = "banana"
print(len(str))

fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
    
fruit = "oranges"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = "banana"
for letter in fruit:
    print(letter)
    
fruit = "banana"
index = 0


while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

word = "banana"
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
        

#slicing

s = " hello world"
print(s[0:3])
print(s[2:3])
print(s[3:7])
print(s[0:])
print(s[:5])
print(s[:])


a = "hello"
b = a + "   " + "there"
print(b)

