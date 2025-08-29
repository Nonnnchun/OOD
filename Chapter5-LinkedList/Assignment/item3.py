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
      p = Node(data)
      if self.head == None:
         self.head = p
      else:
         t = self.head
         while t.next != None:
            t = t.next
         t.next = p
         self.tail = t.next
      self.size += 1

   def contains(self, data):
      t = self.head
      while t:
         if t.data == data:
            return True
         t = t.next
      return False

def create_branch(branch_in):
   commits = branch_in.strip().split("->")
   commits = [c.strip() for c in commits]

   branch = LinkedList()
   for i in commits:
      branch.append(i)
   return branch

def is_same_repo(branches):
   if branches.head is None:
      return "Empty"

   current = branches.head
   first_tail = get_tail_data(current.data)

   current = current.next
   while current:
      tail = get_tail_data(current.data)
      if tail != first_tail:
         return False
      current = current.next
   return True

def get_tail_data(branch):
   t = branch.head
   while t and t.next:
      t = t.next
   return t.data if t else None

def count_merge_commit(branches):
   commits = LinkedList()
   nexts_list = LinkedList()

   t = branches.head
   while t:
      branch = t.data
      node = branch.head
      while node and node.next:
         commit = node.data
         next_commit = node.next.data

         if not commits.contains(commit):
            commits.append(commit)
            sub = LinkedList()
            sub.append(next_commit)
            nexts_list.append(sub)
         else:
            c = commits.head
            n = nexts_list.head
            while c:
               if c.data == commit:
                  if not n.data.contains(next_commit):
                     n.data.append(next_commit)
                  break
               c = c.next
               n = n.next
         node = node.next
      t = t.next

   count = 0
   n = nexts_list.head
   while n:
      if n.data.size > 1:
         count += 1
      n = n.next

   return count


raw_branches = input("Git History: ").strip().split("|")
branches = LinkedList()
for branch in raw_branches:
   br = create_branch(branch)
   branches.append(br)

if is_same_repo(branches):
   print("Are these branches in the same repository? True")
   print(f"{count_merge_commit(branches)} Merge(s)")
else:
   print("Are these branches in the same repository? False")