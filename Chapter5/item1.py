class Node():
   def __init__(self, data, next = None):
      self.data = data
      if next == None:
         self.next = None
      else:
         self.next = next

class LinkedList():
   def __init__(self, head = None):
      self.head = head
      self.count = 0
      if self.head == None:
         self.tail = None
         self.size = 0
      else:
         self.head = head
         t = self.head
         self.size = 1
         while t.next != None :
            t = t.next
            self.size += 1
         self.tail = t

   def append(self, data):
      p = Node(data)
      if self.head == None:
         self.head = p
      else:
         t = self.head
         while t.next != None:
            t = t.next
         t.next = p
      self.size += 1

   def add_head(self, data):
      p = Node(data)
      p.next = self.head
      self.head = p
      self.size += 1

   def remove_head(self):
      if self.head == None:return None
      if self.head.next == None:
         p = self.head
         self.head = None
      else:
         p = self.head
         self.head = self.head.next
      self.size -= 1
      return p.data

   def remove_tail(self):
      if self.head == None:return None
      if self.head.next == None:
         self.head = None
         self.size -= 1
         return
      else:
         p = self.head
         while p.next.next != None:
            p = p.next
         p.next = p.next.next
         self.size -= 1

   def insertAfter(self, index, data):
      p = Node(data)
      q = self.head
      count = 0
      while q != None:
         if count == index:
            p.next = q.next
            q.next = p
            return
         q = q.next
         count += 1

   def delete_after(self, index):
      q = self.head
      count = 0
      while q != None and  q.next != None:
         if count == index:
            p = q.next
            q.next = p.next
            p = None
            self.size -= 1
            return
         q = q.next
         count += 1
      return

   def remove_duplicates(self):
      current = self.head
      while current != None:
         prev = current
         runner = current.next

         while runner != None:
               if runner.data == current.data:
                  prev.next = runner.next
                  self.size -= 1
                  self.count += 1
               else:
                  prev = runner
               runner = runner.next
         current = current.next


   def print_list(self):
      p = self.head
      print("Linked list now is", end = " ")
      while p != None:
         print(p.data, end = ' ')
         p = p.next
      print("")

   def print_del_list(self):
      p = self.head
      print(f"there are {self.count} duplicates that been remove")
      print("Remove duplicates Linked list", end = " ")
      while p != None:
         print(p.data, end = ' ')
         p = p.next

info = input("Enter Input : ").split()
link_list = LinkedList()

for i in info:
   link_list.append(i)

link_list.print_list()

link_list.remove_duplicates()

link_list.print_del_list()