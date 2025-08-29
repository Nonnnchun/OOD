class Queue():
   def __init__(self, count):
      self.queue = []
      self.out = ''
      self.count = count

   def size(self):
      return f"{len(self.queue)}"

   def is_empty(self):
      return len(self.queue) == 0

   def enqueue(self, value):
      return self.queue.append(value)

   def peek(self):
      if not self.is_empty():
         return self.queue[0]
      return "Empty"

   def dequeue(self):
      if not self.is_empty():
         self.dequeue_list.append(self.peek())
         return self.queue.pop(0)
      return "Empty"

   def __str__(self):
      for i in self.queue:
         self.out += i+", "
      self.out = self.out[:-2]
      return f"Group {self.count} : {self.out}"

def make_group(count, people, group):
   temp = []
   reject = []
   queue = Queue(count+1)
   for i in people:
      if len(queue.queue) < group:
         if i == "Pink" and "Green" in queue.queue and "Blue" not in queue.queue:
            reject.append(i)
         elif i == "Green" and "Pink" in queue.queue and "Blue" not in queue.queue:
            reject.append(i)
         elif i == "Yellow" and "Blue" in queue.queue and "Red" not in queue.queue:
            reject.append(i)
         elif i == "Blue" and "Yellow" in queue.queue and "Red" not in queue.queue:
            reject.append(i)
         else:
            queue.enqueue(i)
      else:
         temp.append(i)
   
   if len(queue.queue) < group:
      for i in queue.queue:
         reject.append(i)
      queue.queue = []

   people = temp
   if len(queue.queue) == 0:
      pass
   else:
      print(queue)
   return people,reject

def rejected_format(rejected_people):
   # format rejected people
   out = ''
   for i in str(rejected_people):
      if i in "[]'' ":
         pass
      else:
         out += i

   x = out.split(",")
   temp = []
   rejected_people = []
   for i in x:
      if len(i) < 1:
         temp.append(i)
      else:
         rejected_people.append(i)

   # rejected output after complete formatting
   if len(a) == 0 :
      if len(rejected_people) == 0:
         print(f"Rejected : None")
      else:
         out = ''
         for i in rejected_people:
            out += i+", "
         out = out[:-2]
         print(f"Rejected : {out}")
   else:
      out = ''
      for i in a:
         out += i+", "
      out = out[:-2]
      print(f"Rejected : {out}")

print("***Make a group***")
token = input("Enter input : ").split(", ")

# people per one group
group_of = int(token[0])

# list of people that i have
list_people = token[1].split(" ")
a = list_people

# number of group that can make group
number_of_group = round(len(list_people) // group_of)

# making group and find people, who rejected
rejected = []
for i in range(0,number_of_group):
   a,reject = make_group(i, a, group_of)
   rejected.append(reject)

rejected_format(rejected)