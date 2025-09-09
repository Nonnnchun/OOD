class AVLTree:
   class AVLNode:
      def __init__(self, data, left=None, right=None):
         self.data = data
         self.left = None if left is None else left
         self.right = None if right is None else right
         self.height = self.setHeight()

      def __str__(self):
         return str(self.data)

      def setHeight(self):
         a = self.getHeight(self.left)
         b = self.getHeight(self.right)
         self.height = 1 + max(a, b)
         return self.height

      def getHeight(self, node):
         return -1 if node is None else node.height

      def balanceValue(self):
         return self.getHeight(self.right) - self.getHeight(self.left)

   def __init__(self, root=None):
      self.root = None if root is None else root

   def add(self, data):
      self.root = self._add(self.root, data)

   def _add(self, root, data):
      if root is None:
         return self.AVLNode(data)
      else:
         if int(data) < int(root.data):
               root.left = self._add(root.left, data)
         else:
               root.right = self._add(root.right, data)
      root = self.rebalance(root)
      return root

   def rotateLeftChild(self, root):
      new_root = root.right
      root.right = new_root.left
      new_root.left = root
      root.setHeight()
      new_root.setHeight()
      return new_root

   def rotateRightChild(self, root):
      new_root = root.left
      root.left = new_root.right
      new_root.right = root
      root.setHeight()
      new_root.setHeight()
      return new_root

   def rebalance(self, x):
      if x is None:
         return x
      x.setHeight()
      balance = x.balanceValue()

      if balance < -1:
         if x.left.balanceValue() > 0:
               x.left = self.rotateLeftChild(x.left)
         x = self.rotateRightChild(x)
      elif balance > 1:
         if x.right.balanceValue() < 0:
               x.right = self.rotateRightChild(x.right)
         x = self.rotateLeftChild(x)
      x.setHeight()
      return x

   def printTree(self):
      AVLTree._printTree(self.root)

   def _printTree(node, level=0):
      if node is not None:
         AVLTree._printTree(node.right, level + 1)
         indent = '    ' * level
         print(f"{indent}{node}")
         AVLTree._printTree(node.left, level + 1)

def check_same_tree(node1, node2):
   if node1 is None or node2 is None:
      return node1 is node2
   return (node1.data == node2.data and
         check_same_tree(node1.left, node2.left) and
         check_same_tree(node1.right, node2.right))

Tree1 = AVLTree()
Tree2 = AVLTree()

Tree1_inp, Tree2_inp = (input("Enter Tree1/Tree2 : ")).split("/")

Tree1_inp = Tree1_inp.split()
Tree2_inp = Tree2_inp.split()

for data in Tree1_inp:
   Tree1.add(data)

for data in Tree2_inp:
   Tree2.add(data)

print("Tree 1")
Tree1.printTree()
print()

print("Tree 2")
Tree2.printTree()
print()

if check_same_tree(Tree1.root, Tree2.root):
   print("Same Tree")
else:
   print("Different Tree")