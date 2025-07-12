class Stack():
   pass

stack = Stack()
a = input("Enter Input : ").split(",")
print(a)
for i in range(0,len(a)):
   if len(a[i]) > 1 :
      function, value = a[i].split()
      if function == 'A':
         pass
      elif function == 'P':
         pass
      else:
         if function == 'LD' :
            pass
         elif function == 'MD' :
            pass
         else:
            pass
      print(function)
      print(value)
      # stack.add_into_stack(add_function = x[0],value = x[1])
   else:
      print(a[i])
      # stack.pop_stack(add_function = a[i])
      pass