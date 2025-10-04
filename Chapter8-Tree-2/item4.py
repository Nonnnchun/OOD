class BST:
   class Node:
      def __init__(self, data, left=None, right=None):
         self.data = data
         self.left = None if left is None else left
         self.right = None if right is None else right
         self.h = 0

      def __str__(self):
         return str(self.data)

      def update_height(self):
         a = self.getHeight(self.left)
         b = self.getHeight(self.right)
         self.h = 1 + max(a, b)
         return self.h

      def getHeight(self, node):
         return -1 if node is None else node.h

      def balance_factor(self):
         return self.getHeight(self.right) - self.getHeight(self.left)

   def __init__(self, root=None):
      self.root = None if root is None else root

   def insert(self, data):
      self.root = self.__insert(self.root, data)

   def __insert(self, root, data):
      if root is None:
         return self.Node(data)
      else:
         if int(data) < int(root.data):
               root.left = self.__insert(root.left, data)
         else:
               root.right = self.__insert(root.right, data)
      root.update_height()
      return root

   def _get_format(root, ans=""):
      if root:
         temp = ""
         if root.right:
               temp += BST._get_format(root.right, ans + "     ")
         temp += f"{ans}{root.data}\n"
         if root.left:
               temp += BST._get_format(root.left, ans + "     ")
         return temp
      return ""

   def __str__(self):
      return BST._get_format(self.root)

################################
'''
⠀⠀⢘⣾⣾⣿⣾⣽⣯⣼⣿⣿⣴⣽⣿⣽⣭⣿⣿⣿⣿⣿⣧
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣰⣯⣾⣿⣿⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠛⠛⠋⠁⣠⡼⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠤⣶⣾⣿⣿⣿⣦⡈⠉⠉⠉⠙⠻⣿⣿⣿⣿⣿⠿⠁⠀
⠀⠀⠀⠀⠈⠟⠻⢛⣿⣿⣿⣷⣶⣦⣄⠀⠸⣿⣿⣿⠗⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠀⠄⣿⡿⠋⣉⠈⠙⢿⣿⣦⣿⠏⡠⠂⠀⠀⠀
⠀⠀⠀⠀⢰⡌⠀⢠⠏⠇⢸⡇⠐⠀⡄⣿⣿⣃⠈⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣻⣿⢫⢻⡆⡀⠁⠀⢈⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣻⣷⣾⣿⣿⣷⢾⣽⢭⣍⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⡿⠈⣹⣾⣿⡞⠐⠁⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⠨⣟⣿⢟⣯⣶⣿⣆⣘⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡆⠀⠐⠶⠮⡹⣸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

def isAVL(node: BST.Node):
   if node is None:
      return True
   bf = node.balance_factor()
   if abs(bf) > 1:
      return False
   return isAVL(node.left) and isAVL(node.right)

tree = BST()
print("**********IsAVL**********")
for i in list(map(int, input("Enter numbers to insert in the tree: ").split())):
   tree.insert(i)
print("Tree:")
print(tree)
print("Is AVL???:", isAVL(tree.root))