class Stack():
   def __init__(self):
      self.stack = []

   def add_into_stack(self, value):
      self.stack.append(value)
      print(f"Add = {value}")

   def pop_stack(self):
      if not self.stack:
         print("-1")
      else:
         print(f"Pop = {self.stack[-1]}")
         self.stack.pop()

   def delete_index(self, value):
      if not self.stack:
         print("-1")
      else:
         while self.stack:
            for _ in range(0,len(self.stack)):
               for i in self.stack:
                  if i == value:
                     print(f"Delete = {i}")
                     self.stack.remove(i)
            break

   def lessthan_del(self, lessthan_value):
      temp = []
      if not self.stack:
         print("-1")
      else:
         while self.stack:
            for i in self.stack:
               if i < lessthan_value:
                  temp.append(i)
            break
         temp.sort()
         for i in temp:
            for j in self.stack:
               if j == i:
                  print(f"Delete = {j} Because {j} is less than {lessthan_value}")
                  self.stack.remove(j)

   def morethan_del(self, morethan_value):
      if not self.stack:
         print("-1")
      else:
         while self.stack:
            
            for _ in range(0,len(self.stack)):
               for i in self.stack:
                  if i > morethan_value:
                     self.stack.remove(i)
                     print(f"Delete = {i} Because {i} is more than {morethan_value}")
            break

   def __str__(self):
      output = []
      for i in self.stack:
         output.append(int(i))
      return f"Value in Stack = {output}"

stack = Stack()
a = input("Enter Input : ").split(",")
for i in range(0,len(a)):
   if len(a[i]) > 1 :
      function, value = a[i].split()
      value = int(value)
      if function == 'A':
         stack.add_into_stack(value = value)
      else:
         if function == 'LD' :
            stack.lessthan_del(lessthan_value = value)
         elif function == 'MD' :
            stack.morethan_del(morethan_value = value)
         else:
            stack.delete_index(value = value)
   else:
      stack.pop_stack()

print(stack)