class AVLTree:
   def __init__(self):
      self.root = None

   def insertMovie(self, movie):  
      self.root = self._insert(self.root, movie)

   def _insert(self, node, movie):
      if not node:
         return Node(Movie(movie[0], movie[1]))

      # --- BST Insertion ---
      # If new movie's rating is less, go left. Otherwise (>=), go right.
      if float(movie[1]) < node.data.rating:
         node.left = self._insert(node.left, movie)
      else:
         node.right = self._insert(node.right, movie)

      # --- Update height and balance ---
      node.setHeight()
      return self.balance(node)

   # Function to find a movie object by its name (full scan)
   def _findMovie(self, node, movieName):
      if node is None:
         return None
      if node.data.title == movieName:
         return node.data

      found_in_left = self._findMovie(node.left, movieName)
      if found_in_left:
         return found_in_left
      return self._findMovie(node.right, movieName)

   def removeMovie(self, movieName):
      movie_to_delete = self._findMovie(self.root, movieName)
      if movie_to_delete:
         self.root = self._remove(self.root, movie_to_delete)

   def _remove(self, node, movie_to_delete):
      if not node:
         return node

      rating_to_delete = movie_to_delete.rating
      title_to_delete = movie_to_delete.title

      if rating_to_delete < node.data.rating:
         node.left = self._remove(node.left, movie_to_delete)
      elif rating_to_delete > node.data.rating:
         node.right = self._remove(node.right, movie_to_delete)
      else: # Ratings are equal, check title
         if title_to_delete != node.data.title:
               node.right = self._remove(node.right, movie_to_delete)
         else: # This is the node to delete
               if node.left is None:
                  return node.right
               elif node.right is None:
                  return node.left

               # Node with two children: get inorder successor
               temp = self.getMin(node.right)
               node.data = temp.data
               # Delete the inorder successor from the right subtree
               node.right = self._remove(node.right, temp.data)

      # Update height and balance
      node.setHeight()
      return self.balance(node)

   def top(self, number):
      return self._top(self.root, number, [])

   def _top(self, node, number, top_list):
      if node is None or len(top_list) >= number:
         return top_list

      # Reverse in-order traversal (Right, Root, Left)
      self._top(node.right, number, top_list)

      if len(top_list) < number:
         top_list.append(node.data)

      self._top(node.left, number, top_list)

      return top_list

   def getRatingRange(self, start, end):
      result = []
      self._getRatingRange(self.root, start, end, result)
      return sorted(result, key=lambda x: x.rating)

   def _getRatingRange(self, node, start, end, range_list):
      if node is None:
         return range_list
         
      # ไปทางซ้ายถ้ายังมีโอกาสเจอค่าใน range
      if node.data.rating >= start:
         self._getRatingRange(node.left, start, end, range_list)

      # ถ้าอยู่ในช่วงก็เก็บ
      if start <= node.data.rating <= end:
         range_list.append(node.data)

      # ไปทางขวาถ้ายังมีโอกาสเจอค่าใน range
      if node.data.rating <= end:
         self._getRatingRange(node.right, start, end, range_list)

      return range_list

   def balance(self, node):
      BF = node.balanceFactor()

      # Right heavy case
      if BF > 1:
         # Right-Left case
         if node.right and node.right.balanceFactor() < 0:
               node.right = node.right.rotateRight()
         return node.rotateLeft()

      # Left heavy case
      if BF < -1:
         # Left-Right case
         if node.left and node.left.balanceFactor() > 0:
               node.left = node.left.rotateLeft()
         return node.rotateRight()

      return node

   def getMin(self, node): #Get minimum rating node
      current = node
      while current.left:
         current = current.left
      return current

   def printTree(self, node, level=0):
      if node is not None:
         self.printTree(node.right, level + 1)
         print('     ' * level, node)
         self.printTree(node.left, level + 1)

   def isAVL(self):
      return self._isAVL(self.root)

   def _isAVL(self, node):
      if not node:
         return True
      if abs(node.balanceFactor()) > 1:
         return False
      expected_height = 1 + max(node.left.height if node.left else -1, node.right.height if node.right else -1)
      if node.height != expected_height:
         return False
      return self._isAVL(node.left) and self._isAVL(node.right)
   
   def isBST(self):
      return self._isBST(self.root)

   def _isBST(self, node, min=float('-inf'), max=float('inf')):
      if not node:
         return True
      if not (min <= node.data.rating <= max):
         return False
      return (self._isBST(node.left, min, node.data.rating) and
               self._isBST(node.right, node.data.rating, max))

class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      self.height = 0

   def __str__(self):
      return f'{self.data}'
   
   def balanceFactor(self):    #Get balance factor
      if not self:
         return -1
      left_height = self.left.height if self.left else -1
      right_height = self.right.height if self.right else -1
      return right_height - left_height
   
   def setHeight(self):        #Set height base on child node
      a = self.left.height if self.left else -1  
      b = self.right.height if self.right else -1
      self.height = 1 + max(a,b)

   def rotateRight(self):      #Rotate right (clockwise)
      new_root = self.left
      self.left = new_root.right
      new_root.right = self
      self.setHeight()
      new_root.setHeight()
      return new_root
   
   def rotateLeft(self):       #Rotate left (counter-clockwise)
      new_root = self.right
      self.right = new_root.left
      new_root.left = self
      self.setHeight()
      new_root.setHeight()
      return new_root
      
class Movie:
   def __init__(self, title, rating):
      self.title = title
      self.rating = float(rating)

   def __str__(self):
      return f'{self.title}({self.rating})'

rottenPotato = AVLTree()
movies = [
   ("Megalodon", 5.0),
   ("Inception", 9.1),
   ("The_Dark_Knight", 8.9),
   ("Interstellar", 9.4),
   ("Tenet", 7.2),
   ("Memento", 7.9),
   ("Dunkirk", 7.7),
   ("The_Prestige", 8.3),
   ("Avatar", 7.8),
   ("Titanic", 8.1),
   ("Gladiator", 8.6),
   ("The_Matrix", 9.3),
   ("John_Wick", 7.5),
   ("Parasite", 9.0),
   ("Whiplash", 8.5),
   ("La_La_Land", 8.0),
   ("The_Godfather", 9.2),
   ("Pulp_Fiction", 8.4),
   ("Fight_Club", 8.7),
   ("Forrest_Gump", 8.8)
]

for movie in movies:
   rottenPotato.insertMovie(movie)

inp = input("The Requests From User: ").split(", ")
for request in inp:
   req = request.split(" ")
   if req[0] == "I":
      rottenPotato.insertMovie([req[1], float(req[2])])
   elif req[0] == "D":
      rottenPotato.removeMovie(req[1])
   elif req[0] == "T":
      print(f"Top {req[1]}")
      print([str(movie) for movie in rottenPotato.top(int(req[1]))])
      print()
   elif req[0] == "R":
      print(f'Rating range from {req[1]} to {req[2]}')
      print([str(movie) for movie in rottenPotato.getRatingRange(float(req[1]), float(req[2]))])
      print()
print(f'Is this AVL Tree? {rottenPotato.isAVL() and rottenPotato.isBST()}')