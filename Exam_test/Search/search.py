lst = [1,2,0,5,6,3]
n = 5
print("-"*50)
print("search",n,"in",lst)
print("-"*50)

"""Searching Unorder"""
def searchUnorder(lst,key):
   i = 0
   while i<len(lst) :
      if key == lst[i]:
         return i
      i+=1
   return -1
print("searchUnorder:",searchUnorder(lst,n))

def searchUnorderMoreefficient(lst,key):
   for i in range(len(lst)):
      if key == lst[i]:
         return i
   return -1
print("searchUnorderMoreefficient:",searchUnorderMoreefficient(lst,n))

# Sentinel Search : add key at tail || BigO=n
def sentinelSearch(lst, key):
   rec = lst.copy()
   n = len(rec)
   rec.append(key)
   i = 0  

   while rec[i] != key:  
      i += 1
   if i < n:
      return i
   else:
      return -1
print("sentinelSearch:",sentinelSearch(lst,n))

def sentinelSearchInPlace(lst, key):
   if not lst: 
      return -1
   
   n = len(lst)
   last_element = lst[-1]
   lst[-1] = key
   i = 0

   while lst[i] != key:
      i += 1
   lst[-1] = last_element

   if i < n - 1 or last_element == key:
      return i
   else:
      return -1
print("sentinelSearchInPlace:",sentinelSearchInPlace(lst,n))

#Move to Front Heuristic || 
#Transposition || swaps to front 1 idx
class Node:
   def __init__(self, value, next=None):
      self.value = value
      self.next = next
   
   def __str__(self):
      return str(self.value)

class LinkedList:
   def __init__(self):
      self.head = None
      self.outBook = [] 

   def __str__(self):
      if self.isEmpty():
         return "Empty"
      
      result = []
      current = self.head
      while current is not None:
         result.append(str(current.value))
         current = current.next
      return " ".join(result)

   def isEmpty(self):
      return self.head is None

   def append(self, item):
      new_node = Node(item)
      if self.head is None:
         self.head = new_node
      else:
         current = self.head
         while current.next is not None:
               current = current.next
         current.next = new_node

   def addHead(self, item):
      new_node = Node(item)
      new_node.next = self.head
      self.head = new_node

   def Transposition(self, item):
      if self.head is None:
         return -1
      
      if self.head.value == item:
         return 0
      
      if self.head.next is not None and self.head.next.value == item:
         # and self.head.next.value == item:
         second = self.head.next
         self.head.next = second.next
         second.next = self.head
         self.head = second
         return 1
      
      prev_prev = self.head
      prev = self.head.next
      current = prev.next if prev else None
      position = 2
      
      while current is not None:
         if current.value == item:
               prev_prev.next = current
               prev.next = current.next
               current.next = prev
               return position
         prev_prev = prev
         prev = current
         current = current.next
         position += 1

      if item not in self.outBook:
         self.outBook.append(item)
         return -1
      else:
         self.addHead(item)
         return -2
         
   def MoveToFront(self, item):
      if self.head is None:
         return -1
      
      if self.head.value == item:
         return 0
      
      current = self.head
      previous = None
      position = 0
      
      while current is not None:
         if current.value == item:
               previous.next = current.next
               current.next = self.head
               self.head = current
               return True, position
         
         previous = current
         current = current.next
         position += 1

      if item not in self.outBook:
         self.outBook.append(item)
         return -1
      else:
         self.addHead(item)
         return -2
         
L1 = LinkedList()
for i in lst: L1.append(i)
L1.MoveToFront(n)
print("moveToFront:",L1)

L2 = LinkedList()
for i in lst: L2.append(i)
L2.Transposition(n)
print("Transposition:",L2)

"""Searching order"""
def bubble_sort(lst): 
   for last in range(len(lst)-1,0,-1): #from last index to 0
      swaped = False  
      for i in range(last):
         if lst[i] > lst[i+1] :
               lst[i],lst[i+1] = lst[i+1],lst[i]
               swaped  = True
      if not swaped : break
   return lst
lst_sort = bubble_sort(lst)
print("-"*50)
print("list sort :",lst_sort)
print("-"*50)

#Sequential Search (Linear Search) : ไล่หาตรงๆเลอ || O(n) 
def sequentialSearch(arr, key):
   for i in range(len(arr)):
      if arr[i] == key:
         return i
   return -1
print("sequentialSearch:",sequentialSearch(lst_sort,n))

#binarySearch || O(logn)
def binarySearch(lst,key):
   low = 0
   high = len(lst) - 1
   if key<lst[0]: return -1
   if key>lst[-1]:return 999
   while low <= high:
      mid = (high + low) // 2 
      if key > lst[mid]:    
         low = mid + 1
      elif key < lst[mid]:
         high = mid - 1
      else:
         return mid
   
   lower_idx, upper_idx = low, high
   lower_val, upper_val = lst[lower_idx], lst[upper_idx]
   decimal = (key - lower_val) / (upper_val - lower_val)
   idx = (upper_idx - lower_idx) * decimal + lower_idx
   return idx
print("binarySearch",binarySearch(lst_sort,n))

class Node:
   def __init__(self,data):
      self.data = data
      self.left = None
      self.right = None
   
   def __str__(self):
      return str(self.data)

class BST:
   def __init__(self):
      self.root = None

   def insert(self,data):
      def _insert(root,data):
         if root == None : return Node(data)
         if root.data < data : root.right = _insert(root.right,data)
         else : root.left  = _insert(root.left,data)
         return root
      self.root = _insert(self.root,data)
      return self.root
   
   def binarySearch(self,key):
      p = self.root
      while p :
         if key < p.data:
               p = p.left
         elif key > p.data:
               p = p.right
         else :
               return p
      return
   
   def printTree(self, node=None, level = 0):
      if node != None:
         self.printTree(node.right, level + 1)
         print('     ' * level, node)
         self.printTree(node.left, level + 1)
T = BST()
for i in lst : T.insert(i)
print("binarySearchTree",T.binarySearch(n))

class HashTable:
   def __init__(self, size, max_collision, threshold):
      self.size = size
      self.max_collision = max_collision
      self.table = [None] * size
      self.threshold = threshold
      self.count = 0
      self.total_collisions = 0  # Track total collisions for statistics

   def ascii_sum(self, key):
      return sum(ord(c) for c in str(key))

   def hash_function(self, key):
      # return self.ascii_sum(key) % self.size
      return int(key) % self.size

   def insert(self, key, rehashing=False):
      if not rehashing:    # Check load factor before insertion (unless rehashing)
         load_factor = (self.count + 1) / self.size * 100
         if load_factor > self.threshold:
               print("****** Data over threshold - Rehash !!! ******")
               self.rehash()
               return self.insert(key)  # Try again after rehashing
      # Quadratic probing: h(key) + i² mod size
      collision_count = 0
      for i in range(self.max_collision):
         idx = (self.hash_function(key) + i * i) % self.size
         
         if self.table[idx] is None:
               self.table[idx] = key
               self.count += 1
               return True
         else:
               collision_count += 1
               print(f"Collision number {collision_count} at index {idx} (occupied by {self.table[idx]})")
      
      # Max collisions reached
      print("****** Max collision - Rehash !!! ******")
      self.rehash()
      return self.insert(key)  # Try again after rehashing

   def search(self, key):
      """Search for a key using quadratic probing"""
      key = int(key)
      comparisons = 0
      for i in range(self.max_collision):
         idx = (self.hash_function(key) + i * i) % self.size
         comparisons += 1
         if self.table[idx] is None: return False, idx, comparisons
         elif self.table[idx] == key: return True, idx, comparisons   # Key found
      return False, -1, comparisons  # Not found after max probes

   def delete(self, key):
      found, idx, _ = self.search(key)
      if found:
         self.table[idx] = None
         self.count -= 1
         print(f"Key {key} deleted from index {idx}")
         return True
      else:
         print(f"Key {key} not found for deletion")
         return False

   def rehash(self):
      print(f"Rehashing from size {self.size} to ", end="")
      old_table = [x for x in self.table if x is not None]
      new_size = self.next_prime(self.size * 2)
      self.size = new_size
      self.table = [None] * new_size
      self.count = 0
      self.total_collisions = 0
      for item in reversed(old_table):
         self.insert(item, rehashing=True)

   def next_prime(self, n):
      def is_prime(x):
         if x < 2: return False
         if x == 2: return True
         if x % 2 == 0: return False
         for i in range(3, int(x**0.5) + 1, 2):
               if x % i == 0: return False
         return True
      p = n
      while not is_prime(p):
         p += 1
      return p
   
   def is_full(self):
      return all(item is not None for item in self.table)
   
   def load_factor(self):
      return (self.count / self.size) * 100

   def show(self):
      print(f"Hash Table (Size: {self.size}, Count: {self.count}, Load Factor: {self.load_factor():.1f}%)")
      for i, item in enumerate(self.table):
         print(f"#{i+1:2d}\t{str(item)}")
      print("-" * 40)

print(" ***** Rehashing *****")
inp = input("Enter Input : ")

left, right = inp.split("/")
size, max_collision ,Threshold= map(int, left.split())
pairs = right.split(" ")

ht = HashTable(size, max_collision,Threshold)
print("Initial Table :")
ht.show()

for p in pairs:
   if ht.is_full():
      print("This table is full !!!!!!")
      break
   else:
      print("Add :",p)
      ht.insert(p)
   ht.show()