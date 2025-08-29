class StackCalculator():
   def __init__(self):
      self.stack = []
      self.format_out = ''

   def push(self, token):
      self.stack.append(token)

   def pop(self):
      if not self.is_empty():
         return self.stack.pop()
      return None

   def is_empty(self):
      return len(self.stack) == 0

   def peek(self):
      if not self.is_empty():
         return self.stack[-1]
      return None

   def __str__(self):
      if not self.is_empty():
         return f"{self.stack[-1]}"
      return ""

def is_operator(ch):
   return not ch.isalnum()

def is_num(num):
   return num.isnumeric()

print("* Stack Calculator *")
arg = input("Enter arguments : ").split(" ")
stack = StackCalculator()

for char in arg :
   if is_operator(char):
      if is_num(stack.peek()):
         a = int(stack.pop())
         b = int(stack.pop())
         if char == '+':
            stack.push(str(a+b))
         elif char == '-':
            stack.push(str(a-b))
         elif char == '*':
            stack.push(str(a*b))
         elif char == '/':
            stack.push(str(int(a/b)))
         else:
            print("Invalid operator")
      else:
         a = stack.pop()
         b = stack.pop()
         stack.push(a+char+b)
   else:
      if not is_num(char):
         if char == "DUP":
            stack.push(stack.peek())
         elif char == "POP":
            stack.pop()
            if stack.is_empty():
               stack.push(0)
         elif char == "PSH":
            pass
         else:
            print(f"Invalid instruction: {char}")
            break
      else:
         stack.push(char)

print(stack)