class Node:
   def __init__(self, value ,next=None):
      self.value = value
      if next is None:
         self.next = None
      else : self.next = next
   
   def __str__(self):
      return str(self.value)

class LinkedList:
   def __init__(self):
      self.head = None
      self.outBook = []

   def __str__(self):
      if self.isEmpty():
         return "Empty"
      cur, s = self.head, str(self.head.value) + " "
      while cur.next != None:
         s += str(cur.next.value).strip() + " "
         cur = cur.next
      return s

   def isEmpty(self):
      return self.head == None

   def append(self, item):
      p = Node(item)
      if self.head == None:
         self.head = p
      else :
         t = self.head
         while t.next != None:t = t.next
         t.next = p

   def addHead(self, item):
      new_node = Node(item)
      if self.head is None:
         self.head = new_node
      else:
         new_node.next = self.head
         self.head = new_node
   
   def index(self, item):
      current_node = self.head
      position = 0
      while current_node is not None:
         if current_node.value == item: return position
         position += 1
         current_node = current_node.next
      return -1

   def size(self):
      size = 0
      current_node = self.head
      while current_node:
         size += 1
         current_node = current_node.next
      return size

   def pop(self, pos):
      if self.head is None:
         return "Out of Range"
      if pos == 0:
         self.head = self.head.next
         return "Success"
      current_node = self.head
      position = 0
      while current_node is not None and current_node.next is not None and position + 1 != pos:
         position += 1
         current_node = current_node.next

      if current_node.next is not None:
         current_node.next = current_node.next.next
         return "Success"
      else:
         return "Out of Range"
   
   def moveToFront(self,item):
      idx = self.index(item)
      if idx == -1 : 
         if item not in self.outBook: 
               self.outBook.append(item) 
               return -1
         else:
               self.addHead(item)
               return -2
      else : 
         self.pop(idx)
         self.addHead(item)
         return idx

print("This is your BOOK!!!")
inp = input("Enter input: ").split("/")
L = LinkedList()
cost = 0
for i in inp[0].split(): L.append(i)
for i in inp[1].split():
   idx = L.moveToFront(i)
   if idx == -1: 
      cost += L.size()+1
      print(f"Search {i} -> not found -> {L}")
   elif idx == -2: 
      cost += 1
      print(f"Search {i} -> add new book ->  {L}")
   else : 
      cost += idx+1
      print(f"Search {i} -> found at {idx+1} move to front ->  {L}")
print()
print("Final books:",L)
print("Total cost:",cost)