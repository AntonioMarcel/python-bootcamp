class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
counter.__secretCount = 100000
counter.count()