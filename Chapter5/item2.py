class LinkedList():
   class Node():
      def __init__(self, data, next = None):
         self.data = data
         if next == None:
            self.next = None
         else:
            self.next = next

   def __init__(self, head = None):
      self.head = head
      if self.head == None:
         self.tail = None
         self.size = 0
      else:
         self.head = head
         t = self.head
         self.size = 1
         while t.next != None:
            t = t.next
            self.size += 1
         self.tail = t

   def append(self, data):
      p = LinkedList.Node(data)
      if self.head == None:
         self.head = p
      else:
         t = self.head
         while t.next != None:
            t = t.next
         t.next = p
      self.size += 1

   def sort(self):
      t = self.head
      while t.next != None:
         if t.data > t.next.data:
            return False
         else:
            t = t.next
      return True

   def print_swap_list(self):
      t = self.head
      print("List: ", end = '')
      while t.next != None:
         print(t.data, end = "->")
         t = t.next
      print(t.data)

   def bubble_sort(self):
      reset = self.head
      while not self.sort():
         t = self.head
         current  = self.head
         next_one = self.head.next
         while next_one != None:
            if current.data > next_one.data:
               t = next_one.data
               next_one.data = current.data
               current.data = t
               print("")
               print(f"Swapping {next_one.data} and {current.data}")
               self.print_swap_list()
            else:
               current = current.next
               next_one = next_one.next
         current = reset



   def __str__(self):
      ans = []
      node = self.head
      while node:
         ans.append(str(node.data))
         node = node.next
      return '->'.join(ans)

print("*****Bubble Sort Linked List*****")
token = input("Enter Input: ").split(",")
linked = LinkedList()
for i in token:
   i = int(i)
   linked.append(i)

print("Input List: ", end = '')
print(linked)
print("_______________________________________")

linked.bubble_sort()

print("_______________________________________")
print("Sorted List: ", end = '')
print(linked)