greet = "Hello There"
bob = greet.lower()
print(bob)
print(greet)

x = print("HELLO".lower())

str = "banana"
pos = str.find("na")
print(pos)
upr = str.upper()
print(upr)

str = " hello bob"
rep = str.replace("bob", "jane")
print(rep)

repp = str.replace("o" , "x")
print(repp)

greet = "      hello     world     "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())


str = "Please fill this form"
print(str.startswith("Please"))
print(str.startswith("p"))
print(str.endswith("form"))

data = "tabiawani123@gmail   .com"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ",atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

