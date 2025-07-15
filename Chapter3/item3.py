class Stack():
   def __init__(self):
      self.stack = []
      self.format_out = ''
   
   def push(self, token):
      self.stack.append(token)
   
   def is_empty(self):
      return len(self.stack) == 0
   
   def peek(self):
      if not self.is_empty():
         return self.stack[-1]
      return None
   
   def pop(self):
      if not self.is_empty():
         return self.stack.pop()
      return None
   
   def __str__(self):
      for i in self.stack:
         self.format_out += i
      return f"Postfix : {self.format_out}"

def infix_to_postfix(str):
   precedence = {
      '^': 3,
      '*': 2,
      '/': 2,
      '+': 1,
      '-': 1,
      '(': 0
   }
   return precedence[str]

def is_operand(ch):
   return ch.isalnum()

string = input("Enter Infix : ")
stack = Stack()
output = Stack()

for char in string:
   if is_operand(char):
      output.push(char)
   elif char == '(':
      stack.push(char)
   elif char == ')':
      while stack.peek() != '(' and not stack.is_empty():
         output.push(stack.pop()) # pop everythings in (...)
      stack.pop() # pop '('
   else:
      precedence = infix_to_postfix(char)
      while (not stack.is_empty()) and (infix_to_postfix(char) <= infix_to_postfix(stack.peek())) :
         output.push(stack.pop())
      stack.push(char)

while not stack.is_empty():
   output.push(stack.pop())

print(output)