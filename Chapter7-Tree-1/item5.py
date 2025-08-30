def is_operator(ch):
   return ch in "+-*/"

class Node():
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = None if left is None else left
      self.right = None if right is None else right

   def __str__(self):
      return str(self.data)

class Stack():
   def __init__(self):
      self.stack = []

   def is_Empty(self):
      return len(self.stack) == 0

   def pop_stack(self):
      if not self.is_Empty():
         return self.stack.pop()
      return None

   def push(self, value):
      self.stack.append(value)

class BST():
   def __init__(self, root = None):
      self.root = None if root is None else root

   def printTree(self):
      self.__printTree(self.root, 0)

   def __printTree(self, node, level = 0):
      if node is not None:
         self.__printTree(node.right, level + 1)
         print('     ' * level, node)
         self.__printTree(node.left, level + 1)

   def inorder(self):
      return self.__inorder(self.root)

   def __inorder(self, node):
      if node is None:
         return None
      if is_operator(node.data):
         return "(" + self.__inorder(node.left) + str(node.data) + self.__inorder(node.right) + ")"
      else:
         return str(node.data)

   def preorder(self):
      return self.__preorder(self.root)
   
   def __preorder(self, node):
      if node is None:
         return ""
      return str(node.data) + self.__preorder(node.left) + self.__preorder(node.right)


stack = Stack()
inp = input("Enter Postfix : ")

for char in inp:
   if not is_operator(char):
      stack.push(Node(char))
   else:
      right_node = stack.pop_stack()
      left_node = stack.pop_stack()
      operator_node = Node(char, left = left_node, right = right_node)
      stack.push(operator_node)

T = BST(stack.pop_stack())
print("Tree :")
T.printTree() 
print("--------------------------------------------------")
print("Infix : " + T.inorder())
print("Prefix : " + T.preorder())