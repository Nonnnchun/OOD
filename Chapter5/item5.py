class Node():
   def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList():
   def __init__(self, head=None):
      self.head = head

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
         print(current.data, end = " → " if current.next else "\n")
         current = current.next

   def size_of(self):
      count = 0
      t = self.head
      while t:
         count += 1
         t = t.next
      return count

   def reverse_k_nodes(self, head, k):
      prev = None
      current = head
      count = 0
      tail = head

      # Reverse k nodes
      while current and count < k:
         nxt = current.next
         current.next = prev
         prev = current
         current = nxt
         count += 1

      return prev, tail, current
      # returns new_head, new_tail, next_segment

   def swap_army(self, k):
      if k <= 0 or not self.head or not self.head.next:
         return

      dummy = Node(0)
      dummy.next = self.head
      prev_tail = dummy
      current = self.head
      reverse = True

      while current:
         # Check size
         temp = current
         count = 0
         while temp and count < k:
               temp = temp.next
               count += 1

         if count == 0:
               break

         if reverse:
               # Reverse (even if < k)
               new_head, new_tail, next_segment = self.reverse_k_nodes(current, k)
               prev_tail.next = new_head
               new_tail.next = next_segment
               prev_tail = new_tail
               current = next_segment
         else:
               # Skip this
               for _ in range(k):
                  if not current:
                     break
                  prev_tail = current
                  current = current.next

         reverse = not reverse

      self.head = dummy.next


print(" *** Ant Army ***")
ant, k = input("Input : ").split(",")
ant = ant.strip().split()
k = int(k.strip())

# Create ant linked list
ant_army = LinkedList()
for a in ant:
   ant_army.append(a)

print("Before : ", end='')
ant_army.print_list()

ant_army.swap_army(k)

print("After : ", end='')
ant_army.print_list()