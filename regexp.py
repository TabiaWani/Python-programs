# import re
# fhand = open('loops.py')
# for line in fhand:
#     line = line.rstrip()
#     if re.search("from", line):
#         print(line)
        
        
# import re
# fhand = open('loops.py')
# for line in fhand:
#     line = line.rstrip()
#     if re.search("^from", line):  # ^from:- start searching the line starts with from
#         print(line)
        
        
# import re
# x = "my 2 fav digits are 12 and 14"
# y= re.findall('[0-9]+',x)
# print(y)
# y = re.findall('[AEIOU]+',x)
# print(y)
# y = re.findall('[aeiou]+',x)
# print(y)

# import re     #greedy
# x = "From: Using the: character"
# y = re.findall('^F.+:',x)
# print(y)

# import re    #not greedy
# x = "From: Using the: character"
# y = re.findall('^F.+?:',x)
# print(y)

# import re
# x = "tabia wani @gn ail.com23ddggnn"
# y = re.findall('\s+@\s+',x)
# print(y)

import re
x = "tabiawani@gmail.  com"
y = re.findall('@(.*)', x)
# y = re.findall('@([^]*)',x)
print(y)


import re
x = "tabiawani@gmail.  com"
# y = re.findall('@(.*)', x)
y = re.findall('^From.@([^ ]*)',x)
print(y)

import re
x = "i got $10.00 dollars"
y = re.findall('\$[0-9.]+',x)
print(y)

import re
x = "i got $10.00 dollars"
y = re.findall('\$[0-9.]+?',x)
print(y)

