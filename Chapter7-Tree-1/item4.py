class Node():
   def __init__(self, data, left=None, right=None):
      self.data = data
      self.left = None if left is None else left
      self.right = None if right is None else right

   def __str__(self):
      return str(self.data)

class BST():
   def __init__(self, root=None):
      self.root = None if root is None else root

   def insert(self, data):
      self.root = BST.__insert(self.root, data)
      return self.root

   def __insert(root, data):
      if root is None:
         return Node(data)
      else:
         if data < root.data:
               root.left = BST.__insert(root.left, data)
         else:
               root.right = BST.__insert(root.right, data)
      return root

   def find_path(self, root, treasure, escape):
      state = {'treasure_found': False, 'escape_found': False}
      BST.__find_path(root, treasure, escape, "", state)
      if not state['escape_found']:
         print(">>> Mission Failed <<<")

   def __find_path(root, treasure, escape, path, state):
      if root is None:
         return False

      current_path = path + str(root.data)

      if root.data == treasure:
         print("Found Treasure !!!")
         state['treasure_found'] = True

      if root.data == escape and state['treasure_found']:
         state['escape_found'] = True
         print("Found Escape !!!")
         print(f"✅ {current_path}")
         print(">>> Mission Complete <<<")
         return True
      else:
         print(f"❌ {current_path}")

      path_for_children = current_path + ' -> '

      if BST.__find_path(root.left, treasure, escape, path_for_children, state):
         return True
      if BST.__find_path(root.right, treasure, escape, path_for_children, state):
         return True

      return False

   def printTree(self, node, level=0):
      if node is not None:
         self.printTree(node.right, level + 1)
         print('     ' * level, node)
         self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split("/")
path_input, treasure_input, escape_input = inp[0], inp[1], inp[2]
treasure = int(treasure_input)
escape = int(escape_input)

path = [int(i) for i in path_input.split()]
for i in path:
   root = T.insert(i)
T.printTree(T.root)
print("-------------------------------------------------")
T.find_path(T.root, treasure, escape)