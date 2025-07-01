#!/usr/bin/python
# define parent class
class Parent:        
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ("Calling parent method")

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

# define child class
class Child(Parent): 
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ("Calling child method")

p = Parent()
c = Child()

p.parentAttr = 500
print(Parent.parentAttr)

p.setAttr(500)
c.setAttr(600)
print(p.parentAttr)
