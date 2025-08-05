class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None

   def append(self, data):
      new_node = Node(data)
      if not self.head:
         self.head = new_node
         return
      
      tail = self.head
      while tail.next:
         tail = tail.next
      tail.next = new_node

   def print_list(self):
      current = self.head
      while current:
         print(current.data, end=" → " if current.next else "\n")
         current = current.next