#NOTE - Class Node --> (Data in list)
class Node():
   def __init__(self, data, next = None):
      self.data = data
      if next is None:
         self.next = None
      else:
         self.next = next

#NOTE - Class LinkedList --> (List)
class LinkedList():
   def __init__(self, head = None, tail = None):
      if head is None:
         self.head = self.tail = None
         self.size = 0
      else:
         self.head = head
         t = self.head
         self.size = 1
         while t.next != None:
            t = t.next
            self.size += 1
         self.tail = t

#NOTE - Method
# REVIEW - append(data) --> append to tail
# append()
   def append(self, data):
      p = Node(data)
      if self.head is None:
         self.head = p
      else:
         t = self.head
         while t.next != None:
            t = t.next
         t.next = p
      self.size += 1

# REVIEW - remove_at_tail() --> remove tail
# pop()
   def remove_at_tail(self):
      if self.head is None: return
      if self.head.next is None:
         p = self.head
         self.head = None
      else:
         t = self.head
         while t.next.next != None:
            t = t.next
         p = t.next
         t.next = t.next.next
         self.size -= 1
      return p.data

# REVIEW - insert_at_head(data) --> append to head
   def insert_at_head(self, data):
      p = Node(data)
      if self.head is None:
         self.head = p
      else:
         p.next = self.head
         self.head = p
         self.size += 1
      print(f"\nInsert at head : {p.data}")

# REVIEW - remove_at_head() --> remove head
   def remove_at_head(self):
      if self.head is None: return
      if self.head.next is None:
         p = self.head
         self.head = None
      else:
         p = self.head
         self.head = self.head.next
      self.size -= 1
      return p.data

# REVIEW - insert_after(index, data) --> insert after index
   def insert_after(self, index, data):
      p = Node(data)
      if self.head is None:
         self.head = p
      else:
         q = self.head
         count = 0
         while q != None:
            if count == index:
               p.next = q.next
               q.next = p
               self.size += 1
               print(f"\nInsert after index {index} : {p.data}")
               return
            q = q.next
            count += 1

# REVIEW - remove_after(index) --> remove after index
   def remove_after(self, index):
      if self.head is None: return
      if self.head.next is None:
         q = self.head
         self.head = None
      else:
         q = self.head
         count = 0
         while q != None and q.next != None:
            if count == index:
               q.next = q.next.next
               self.size -= 1
               return
            q = q.next
            count +=1
      return q.data

# REVIEW - remove(element) --> remove element
   def remove(self, element):
      if self.head is None: return
      if self.head.next is None:
         if self.head.data == element:
            self.head = None
            self.size -= 1
      else:
         t = self.head
         while t != None:
            if self.head.data == element:
               self.head = self.head.next
            elif t.next != None and t.next.data == element:
               t.next = t.next.next
            else:
               t = t.next

# REVIEW - index(element) --> index of that element
   def index(self, element):
      index_of_element = LinkedList()
      count = 0
      p = self.head
      if self.head is None: return
      else:
         while p != None:
            if p.data == element:
               index_of_element.append(count)
               count += 1
               p = p.next
            else:
               count += 1
               p = p.next
         return index_of_element

# REVIEW - clear() --> clear linkedlist
   def clear(self):
      self.head = None

# REVIEW - copy() --> copy linkedlist
   def copy(self):
      copy = LinkedList()
      p = self.head
      while p != None:
         copy.append(p.data)
         p = p.next
      return copy

# REVIEW - count(element) --> count number of times the element appears
   def count(self, element):
      t =self.head
      count = 0
      if self.head is None: return
      else:
         while t != None:
            if t.data == element:
               count += 1
               t = t.next
            else:
               t = t.next
         return count

# REVIEW - extend(linkedlist) --> append linkedlist to linkedlist
   def extend(self, list): #List : [A, B, C]
      extend_list = LinkedList()
      for i in list:
         extend_list.append(i)
      t = extend_list.head
      while t != None:
         self.append(t.data)
         t = t.next

# REVIEW - sort() --> sorting linkedlist
   def sort_but_bubble(self):
      prev = None
      current = self.head
      next_node = current.next

      while next_node != None:
         if current.data > next_node.data:
            if prev != None:
               prev.next = next_node
            else:
               self.head = next_node
            current.next = next_node.next
            next_node.next = current

            prev = next_node
            next_node = current.next
         else:
               prev = current
               current = next_node
               next_node = next_node.next

   def find_tail(self):
      t = self.head
      while t.next != None:
         t = t.next
      return t

# REVIEW - reverse() --> reverse linkedlist
   def reverse(self):
      prev = None
      current = self.head
      while current != None:
         next_node = current.next
         current.next = prev
         prev = current
         current = next_node
      self.tail = self.head
      self.head = prev

# REVIEW - print() --> print linkedlist simple
   def print1(self):
      t = self.head
      while t != None:
         print(t.data, end = '->')
         t = t.next
      print("None")

# REVIEW - print() --> print linkerlist with string append
   def print2(self):
      out = ''
      t = self.head
      while t != None:
         out += str(t.data) + '->'
         t = t.next
      print(out[:-2])

# REVIEW - print() --> print linkerlist with magic method (list)
   def __str__(self):
      ans = []
      t = self.head
      while t != None:
         ans.append(str(t.data))
         t = t.next
      return '->'.join(ans)

linked_list = LinkedList()
# linked_list.append("A")
# linked_list.append("B")
# linked_list.append("C")
# print("Print format 1 -> ", end = '')
# linked_list.print1()
# print("Print format 2 -> ", end = '')
# linked_list.print2()

# a = linked_list.remove_at_tail()
# print(f"\nRemove tail : {a}")
# print(f"List : {linked_list}")

# linked_list.insert_at_head("Z")
# print(f"List : {linked_list}")

# b = linked_list.remove_at_head()
# print(f"\nRemove head : {b}")
# print(f"List : {linked_list}")

# index = 0
# c = linked_list.remove_after(0)
# print(f"\nRemove after index {index} : {c}")
# print(f"List : {linked_list}")

# linked_list.insert_after(0,"C")
# print(f"List : {linked_list}")

# a = linked_list.copy()
# print(f"\nCopy list: {a}")

# linked_list.clear()
# print(f"\nLinked list clear")
# print(f"List : {linked_list}")

# print("------------------------------------------------------")
# linked_list.append("A")
# linked_list.append("B")
# linked_list.append("A")
# linked_list.append("C")
# linked_list.append("A")
# print(f"List : {linked_list}")

# d = "A"
# g = linked_list.count(d)
# print(f"Times of {d} appaers are : {g}")

# linked_list.reverse()
# print(f"\nReverse list : {linked_list}")

# linked_list.remove(d)
# print(f"\nRemove All : {d}")
# print(f"List : {linked_list}")

# e = "B"
# print(f"\nIndex of {e} is : ", end = '')
# f = linked_list.index(e)
# print(f)
# print(f"List : {linked_list}")

# token = input("\nEnter Input : ").split(" ")
# linked_list.extend(token)
# print(f"List : {linked_list}")

# linked_list.clear()
# print(f"\nLinked list clear")
# print(f"List : {linked_list}")

print("------------------------------------------------------")
linked_list.append(1)
linked_list.append(3)
linked_list.append(2)
linked_list.append(5)
linked_list.append(4)
print(f"List : {linked_list}")

linked_list.sort_but_bubble()
print(f"List : {linked_list}")