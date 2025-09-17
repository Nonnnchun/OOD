class AVLTree():
   class AVLNode():
      def __init__(self, data, left = None, right = None):
         self.data = data
         self.left = None if left is None else left
         self.right = None if right is None else right
         self.height = self.setHeight() # NOTE ------------------> AVLTree

      def __str__(self):
         return str(self.data)

      def setHeight(self): # NOTE ------------------> AVLTree
         a = self.getHeight(self.left)
         b = self.getHeight(self.right)
         self.height = 1 + max(a, b)
         return self.height

      def getHeight(self, node): # NOTE ------------------> AVLTree
         return -1 if node is None else node.height

      def balanceValue(self): # NOTE ------------------> AVLTree
         return self.getHeight(self.right) - self.getHeight(self.left)

   def __init__(self, root = None):
      self.root = None if root is None else root

   def insert(self, data): # NOTE ------------------> AVLTree -> self
      self.root = self.__insert(self.root, data) 

   def __insert(self, root, data):
      if root is None:# NOTE ------------------> AVLTree -> self
         return self.AVLNode(data)
      else:
         if data < root.data:
            root.left = self.__insert(root.left, data)
         else:
            root.right = self.__insert(root.right, data)
      root = self.rebalance(root) # NOTE ------------------> AVLTree
      return root

   def rotateLeftChild(self, root): # NOTE ------------------> AVLTree
      new_root = root.right
      root.right = new_root.left
      new_root.left = root
      root.setHeight()
      new_root.setHeight()
      return new_root

   def rotateRightChild(self, root): # NOTE ------------------> AVLTree
      new_root = root.left
      root.left = new_root.right
      new_root.right = root
      root.setHeight()
      new_root.setHeight()
      return new_root

   def rebalance(self, node): # NOTE ------------------> AVLTree
      if node is None:
         return node

      node.setHeight()
      balance = node.balanceValue()

      if balance < -1: # NOTE => L
         if node.left.balanceValue() > 0: # NOTE => R
            node.left = self.rotateLeftChild(node.left)
         node = self.rotateRightChild(node) # NOTE => L

      elif balance > 1:# NOTE => R
         if node.right.balanceValue() < 0:# NOTE => L
            node.right = self.rotateRightChild(node.right)
         node = self.rotateLeftChild(node)# NOTE => R
      node.setHeight()
      return node

   def delete_node(self, value):# NOTE ------------------> AVLTree -> self
      self.root = self.__delete_node(self.root, value)

   def __delete_node(self, node, value):
      if node is None:
         return None
      if value < node.data:
         node.left = self.__delete_node(node.left, value)
      elif value > node.data:
         node.right = self.__delete_node(node.right, value)
      else:
         if not node.left:
            return node.right
         elif not node.right:
            return node.left
         else:
            temp = self.find_min(node.right)
            node.data = temp.data
            node.right = self.__delete_node(node.right, temp.data)
      # NOTE ------------------> AVLTree
      node.setHeight()
      return self.rebalance(node)