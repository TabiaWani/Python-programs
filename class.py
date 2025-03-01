# class partyanimal:
#     x = 0
#     def party(self):
#         self.x=self.x+1
#         print("so far", self.x)
# an = partyanimal()
# an.party()
# an.party()        
# an.party()        

# print("type" , type(an))
# print("dir means capabilities", dir(an))        




# class PartyAnimal:
#     x = 0

#     def __init__(self):
#         print("I am constructed")

#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)

#     def __del__(self):
#         print("I am destructed", self.x)


# an = PartyAnimal()  # Create an instance of the class
# an.party()
# an.party()
# an = 42  # Replace the object reference with an integer
# print("an contains", an)

    
# class partyanimal:
#     x = 0
#     name = " "
#     def __init__(self,z):
#         self.name=z
#         print(self.name , "constructed")
    
#     def party(self):
#         self.x=self.x + 1
#         print(self.name, "party count", self.x)
        
# s = partyanimal("bunny")
# s.party()
# j = partyanimal("sunny")
# j.party()
# s.party()
        
        
class partyanimal:
    x = 0
    name = " "
    def __init__(self,z):
        self.name=z
        print(self.name, "constructed")
    def party(self):
        self.x=self.x + 1
        print(self.name,"party count", self.x)
        
class footballfan(partyanimal):
    y = 0
    def touchdown(self):
        self.y=self.y + 7
        self.party()
        print(self.name, "y", self.y)
    
s = partyanimal("bunny")
s.party()
j=footballfan("jammy")
j.party()
j.touchdown()
        
        
      
        
        
    
        