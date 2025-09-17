class BST():
   class Node():
      def __init__(self, data, left = None, right = None):
         self.data = data
         self.left = None if left is None else left
         self.right = None if right is None else right

      def __str__(self):
         return str(self.data)

   def __init__(self, root = None):
      self.root = None if root is None else root

   def insert(self, data):
      self.root = BST.__insert(self.root, data)

   def __insert(root, data):
      if root is None:
         return BST.Node(data)
      else:
         if data < root.data:
            root.left = BST.__insert(root.left, data)
         else:
            root.right = BST.__insert(root.right, data)
      return root

   def preOrder(self):
      return BST.__preOrder(self.root)

   def __preOrder(root):
      if root is not None:
         print(root, end = ' ')
         BST.__preOrder(root.left)
         BST.__preOrder(root.right)

   def inOrder(self):
      return BST.__inOrder(self.root)

   def __inOrder(root):
      if root is not None:
         BST.__inOrder(root.left)
         print(root, end = ' ')
         BST.__inOrder(root.right)

   def postOrder(self):
      return BST.__postOrder(self.root)

   def __postOrder(root):
      if root is not None:
         BST.__postOrder(root.left)
         BST.__postOrder(root.right)
         print(root, end = ' ')

   def levelOrder(self):
      result = []
      queue = []
      queue.append(self.root)
      while queue:
         current = queue.pop(0)
         result.append(current.data)
         if current.left is not None:
            queue.append(current.left)
         if current.right is not None:
            queue.append(current.right)
      return result

   def dfs(self):
      result = []
      stack = []
      stack.append(self.root)
      while stack:
         current = stack.pop()
         result.append(current.data)
         if current.left is not None:
            stack.append(current.left)
         if current.right is not None:
            stack.append(current.right)
      return result

   def find_min(node):
      while node.left:
         node = node.left
      return node

   def delete_node(self, value):
      self.root = BST.__delete_node(self.root, value)

   def __delete_node(node, value):
      if node is None:
         return None
      if value < node.data:
         node.left = BST.__delete_node(node.left, value)
      elif value > node.data:
         node.right = BST.__delete_node(node.right, value)
      else:
         if not node.left:
            return node.right
         elif not node.right:
            return node.left
         else:
            temp = BST.find_min(node.right)
            node.data = temp.data
            node.right = BST.__delete_node(node.right, temp.data)
      return node

   def printTree(self, node, level = 0, out = []):
      if node != None:
         self.printTree(node.right, level + 1, out)
         print('     '* level, node)
         self.printTree(node.left, level + 1, out)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
   root = T.insert(i)
T.printTree(T.root)
print("Preorder : ",end = '')
T.preOrder()
print()

print("Inorder : ",end = '')
T.inOrder()
print()

print("Postorder : ",end = '')
T.postOrder()
print()

print("Levelorder : ",end = '')
print(T.levelOrder())

print("Dfs : ",end = '')
print(T.dfs())
print()

T.delete_node(3)
T.printTree(T.root)