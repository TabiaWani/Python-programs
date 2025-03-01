def animal():
    print("dog")
    print("cat")
    
animal()
print("blue whale")
animal()


x = 2
y = 3
z = 4
max_value = max(x , y , z)
print(max_value)


def greet(lang):
    if lang == 'es':
        print("spanish")
    elif lang == 'fr':
        print("bonjour")
    else:
        print("other")
        
greet('en')
greet('fr')
greet('es')        


def greet(lang):
    if lang == 'es':
        return 'spanish'
    elif lang == 'fr':
        return 'bonjour'
    else:
        return 'other'
    
print(greet('en'), 'Micheal')
print(greet('es'),'Racheal')
print(greet('fr'), 'jack')


def addtwo(x,y):
    added=x+y
    return added

a=addtwo(3, 5)
print(a)