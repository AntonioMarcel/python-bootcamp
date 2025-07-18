## 1st example
# class Division:
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def divide(self):
#       return self.n/self.d
# class Modulus:
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def mod_divide(self):
#       return self.n%self.d
      
# class DivMod(Division,Modulus):
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def div_and_mod(self):
#       divval=Division.divide(self)
#       modval=Modulus.mod_divide(self)
#       return (divval, modval)
   
# x=DivMod(10,3)

# print ("division:",x.divide())
# print ("mod_division:",x.mod_divide())
# print ("divmod:",x.div_and_mod())

## 2nd example
# class Division:
#     def __init__(self, a, b):
#         self.n = a
#         self.d = b

#     def divide(self):
#         return self.n / self.d

# class Modulus:
#     def __init__(self, a, b):
#         self.n = a
#         self.d = b

#     def mod_divide(self):
#         return self.n % self.d

# class DivMod(Division, Modulus):
#     def __init__(self, a, b):
#         Division.__init__(self, a, b)
#         Modulus.__init__(self, a, b)

#     def div_and_mod(self):
#         divval = self.divide()
#         modval = self.mod_divide()
#         return divval, modval

# Test
# x = DivMod(10, 3)
# print(x.d)
# print("Division:", x.divide())         # 10 / 3 = 3.333...
# print("Mod Division:", x.mod_divide()) # 10 % 3 = 1
# print("Divmod:", x.div_and_mod())      # (3.333..., 1)

# 3rd example
# class Parent:
#     def __init__(self, a, b):
#         self.n = a
#         self.d = b
#         print("Division init")
#         super().__init__()  # Call next in MRO

#     def divide(self):
#         return self.n / self.d

#     def mod_divide(self):
#         return self.n % self.d

# class MiddleChild:
#     def __init__(self, a, b):
#         print("MiddleChild init")
#         super().__init__(a, b)  # Cooperative call to keep the chain


# class Child(MiddleChild, Parent):
#     def __init__(self, a, b):
#         print("DivMod init")
#         super().__init__(a, b)  # Start the MRO chain

# x = Child(10, 3)
# x.divide()
# x.mod_divide()
# print(Child.__mro__)

