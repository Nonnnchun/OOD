class HashTable:
   def __init__(self,size,max_collision,Threshold):
      self.size = size
      self.max_collision = max_collision
      self.table = [None]*size
      self.Threshold = Threshold
      self.count = 0 

   def insert(self, key, rehashing=False):
      key = int(key)
      
      if key < 0: 
         return 

      if not rehashing:
         load_factor = (self.count + 1) / self.size * 100
         if load_factor > self.Threshold:
               print("****** Data over threshold - Rehash !!! ******")
               self.rehash()
               self.insert(key)
               return

      for i in range(self.max_collision):
         idx = (key + i * i) % self.size
         if self.table[idx] is None:
               self.table[idx] = key
               self.count += 1
               return
         else:
               print(f"collision number {i+1} at {idx}")

      print("****** Max collision - Rehash !!! ******")
      self.rehash()
      self.insert(key)

   def rehash(self):
      old_table = [x for x in self.table if x is not None]
      new_size = self.next_prime(self.size * 2)
      self.size = new_size
      self.table = [None] * new_size
      self.count = 0
      for item in reversed(old_table):
         self.insert(item, rehashing=True)

   def next_prime(self, n):
      def is_prime(x):
         if x < 2:
               return False
         if x == 2:
               return True
         if x % 2 == 0:
               return False
         for i in range(3, int(x**0.5) + 1, 2):
               if x % i == 0:
                  return False
         return True

      p = n + 1
      while not is_prime(p):
         p += 1
      return p
   
   def is_full(self):
      return all(self.table)

   def show(self):
      for i, item in enumerate(self.table):
         print(f"#{i+1}\t{item}")
      print("----------------------------------------")
      

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