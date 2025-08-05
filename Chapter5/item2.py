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
      if not self.head or not self.head.next:
         return

      while not self.sort():
         prev = None
         current = self.head
         next_one = current.next

         while next_one:
            if current.data > next_one.data:
               if prev:
                  prev.next = next_one
               else:
                  self.head = next_one
               current.next = next_one.next
               next_one.next = current

               print("")
               print(f"Swapping {current.data} and {next_one.data}")
               self.print_swap_list()

               prev = next_one
               next_one = current.next
            else:
               prev = current
               current = next_one
               next_one = next_one.next

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