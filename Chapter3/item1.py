class Stack():
   def __init__(self):
      self.size = 0
      self.stack = []

   def size_of_stack(self):
      return f"{self.size}"

   def add_into_stack(self, add_function, value):
      if add_function == 'A':
         self.stack.append(value)
         self.size += 1
      print(f"Add = {value} and Size = {self.size}")

   def pop_stack(self, add_function):
      if add_function == 'P':
         if not self.stack:
            print("-1")
         else:
            print(f"Pop = {self.stack[-1]} and Index = {self.size - 1}")
            self.stack.pop()
            self.size -= 1

   def __str__(self):
      output = ''
      for i in self.stack:
         output += ' '
         output += i
      if len(output) == 0 :
         return "Value in Stack = Empty"
      else:
         return f"Value in Stack ={output}"

stack = Stack()
a = input("Enter Input : ").split(",")
for i in range(0,len(a)):
   if len(a[i]) > 1 :
      x = a[i].split()
      stack.add_into_stack(add_function = x[0],value = x[1])
   else:
      stack.pop_stack(add_function = a[i])


print(stack)