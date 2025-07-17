class Stack :
   def __init__(self):
      self.stack = []
      self.out = ""

   def push(self, token):
      return self.stack.append(token)

   def is_empty(self):
      return len(self.stack) == 0

   def pop(self):
      if not self.is_empty():
         return self.stack.pop()
      return None

   def peek(self):
      if not self.is_empty():
         return self.stack[-1]
      return None

   def __str__(self):
      if not self.is_empty():
         for i in self.stack:
            self.out += str(i)
         return f"{self.out}"
      return None

def dec2bin(decnum):
   s = Stack()
   temp = Stack()
   while 0 < decnum :
      if decnum % 2 != 0 :
         temp.push(1)
         decnum = decnum // 2
      else:
         temp.push(0)
         decnum = decnum // 2

   while not temp.is_empty():
      s.push(temp.pop())

   if s.is_empty():
      s.push(0)
   return s

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))