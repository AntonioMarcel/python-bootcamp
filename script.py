class Desktop:
   def __init__(self):
      self.__max_price = 25000

   def sell(self):
      return f"Selling Price: {self.__max_price}"

   def set_max_price(self, price):
      if price > self.__max_price:
         self.__max_price = price

# Object
desktopObj = Desktop()
print(desktopObj.sell()) 

# modifying the price directly
desktopObj.__max_price = 25000
print(desktopObj.__max_price)
print(desktopObj._Desktop__max_price)
print(desktopObj.sell()) 

# modifying the price using setter function
desktopObj.set_max_price(35000)
print(desktopObj.sell())       
print(desktopObj.__max_price)
print(desktopObj._Desktop__max_price)