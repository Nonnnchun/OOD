class Data:
   def __init__(self, key, value):
      self.key = key
      self.value = value

   def __str__(self):
      return "({0}, {1})".format(self.key, self.value)

class HashTable:
   def __init__(self,size,max_collision):
      self.size = size
      self.max_collision = max_collision
      self.table = [None]*size
      self.full_message_shown = False

   def ascii_sum(self, key):
      return sum(ord(c) for c in key)

   def insert(self, key, value):
      data = Data(key, value)
      h = self.ascii_sum(key) % self.size

      for i in range(self.max_collision):
         idx = (h + i * i) % self.size
         if self.table[idx] is None:
               self.table[idx] = data
               return
         else :
               print(f"collision number {i+1} at {idx}")
         
      print(f"Max of collisionChain")

   def search(self, key):
      idx = self._hash(key)
      for pair in self.table[idx]:
         if pair[0] == key:
               return pair[1]
      return None
   
   def is_full(self):
      return all(self.table)

   def show(self):
      for i, item in enumerate(self.table):
         print(f"#{i+1}\t{item if item else 'None'}")
      print("-"*27)
      

print(" ***** Fun with hashing *****")
raw = input("Enter Input : ")

left, right = raw.split("/")
size, max_collision = map(int, left.split())
pairs = right.split(",")

ht = HashTable(size, max_collision)

for p in pairs:
   k, v = p.split()
   if ht.is_full():
      print("This table is full !!!!!!")
      break
   else:
      ht.insert(k, v)
   ht.show()