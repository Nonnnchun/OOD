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

   def find_parent(self, value):
      return BST.__find_parent(self.root, value, [])

   def __find_parent(root, value, found = []):
      if root is not None and root.data == value:
         found.append(root)
      else:
         if root is not None:
            BST.__find_parent(root.left, value, found)
            BST.__find_parent(root.right, value, found)
      return found

   # Preorder
   def find_child(self, node):
      return BST.__find_child(node, [])

   def __find_child(node, ans = []):
      if node is not None:
         ans.append(node.data)
         BST.__find_child(node.left, ans)
         BST.__find_child(node.right, ans)
      return ans

   def printTree(self, node, level = 0, out = []):
      if node != None:
         self.printTree(node.right, level + 1, out)
         print('     '* level, node)
         self.printTree(node.left, level + 1, out)

inp = input("Enter the BST values and search value: ").split(",")
r = [int(i) for i in inp[0].split()]
val = int(inp[1])

T = BST()
for i in r:
   root = T.insert(i)
print(f"Input: root = {r}, val = {val}")
parent = T.find_parent(val)
if len(parent) != 0:
   print(f"Output: {T.find_child(parent[0])}")
else:
   print(f"Output: []")