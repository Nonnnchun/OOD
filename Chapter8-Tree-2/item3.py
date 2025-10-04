class AVLTree:
   class AVLNode:
      def __init__(self, data, left = None, right = None):
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

   def __init__(self, root = None):
      self.root = None if root is None else root

   def insert(self, data):
      self.root = self.__insert(self.root, data)

   def __insert(self, root, data):
      if root is None: 
         return self.AVLNode(data)
      else:
         if int(data) < int(root.data):
            root.left = self.__insert(root.left, data)
         else:
            root.right = self.__insert(root.right, data)
      root = self.rebalance(root)
      return root

   def rotateLeft(self, root):
      new_root = root.right
      root.right = new_root.left
      new_root.left = root
      root.setHeight()
      new_root.setHeight()
      return new_root

   def rotateRight(self, root):
      new_root = root.left
      root.left = new_root.right
      new_root.right = root
      root.setHeight()
      new_root.setHeight()
      return new_root

   def rebalance(self, x):
      if x is None: return x
      x.setHeight()
      balance = x.balanceValue()

      if balance < -1:
         if x.left.balanceValue() > 0:
            x.left = self.rotateLeft(x.left)
         x = self.rotateRight(x)
      elif balance > 1:
         if x.right.balanceValue() < -1:
            x.right = self.rotateRight(x.right)
         x = self.rotateLeft(x)
      x.setHeight()
      return x

   def postOrder(self):
      return AVLTree.__postOrder(self.root, [])

   def __postOrder(root, result = []):
      if root is None: return root
      else:
         AVLTree.__postOrder(root.left, result)
         AVLTree.__postOrder(root.right, result)
         result.append(int(root.data))
      return result

   def printTree(self):
      AVLTree.__printTree(self.root)
      print()

   def __printTree(node, level = 0):
      if node is not None :
         AVLTree.__printTree(node.right, level + 1)
         print('     ' * level, node)
         AVLTree.__printTree(node.left, level + 1)

def findMaxPath(postList, height):
   maxSum = 0
   out = ''
   for i in range(0, height + 1):
      maxSum += postList[i]
      out = out + str(postList[i]) + ' + '
   return maxSum, out

tree = AVLTree()
inp = input("Enter tree nodes: ").split()
for i in inp:
   tree.insert(i)

tree.printTree()
res = tree.postOrder()
high = tree.AVLNode(tree.root).getHeight(tree.root)

res = res[::-1]
maximum, formatOut = findMaxPath(res, high)
print(f"Path with maximum sum: {formatOut[:-3]} = {str(maximum)}")