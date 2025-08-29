class Node():
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = None if left is None else left
      self.right = None if right is None else right

   def __str__(self):
      return str(self.data)

class BST():
   def __init__(self, root = None):
      self.root = None if root is None else root

   def insert(self, data):
      self.root = BST.__insert(self.root, data)

   def __insert(root, data):
      if root is None: return Node(data)
      else:
         if data < root.data:
            root.left = BST.__insert(root.left, data)
         else:
            root.right = BST.__insert(root.right, data)
      return root

   def printTree(self, node, level = 0):
      if node != None:
         self.printTree(node.right, level + 1)
         print('     '* level, node)
         self.printTree(node.left, level + 1)

   def reverseTree(self, node, level = 0):
      if node != None:
         self.reverseTree(node.left, level + 1)
         print('     '* level, node)
         self.reverseTree(node.right, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
   root = T.insert(i)

print("Before:")
T.printTree(T.root)
print("After:")
T.reverseTree(T.root)