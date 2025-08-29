class funString():
   def __init__(self,string = ""):
      self.string = string

   def __str__(self):
      return f"This is funString class, and this your word : {self.string}"

   def size(self) :
      return f"{len(self.string)}"

   def changeSize(self):
      return f"{self.string.swapcase()}"

   def reverse(self):
      return f"{self.string[::-1]}"

   def deleteSame(self):
      new_string = ""
      for char in self.string:
         if char not in new_string:
               new_string += char
      self.string = new_string

      return f"{self.string}"


str1,str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)

if str2 == "1" : print(res.size())
elif str2 == "2": print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())