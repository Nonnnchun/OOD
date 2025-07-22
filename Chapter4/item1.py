class Queue():
   def __init__(self):
      self.queue = []
      self.dequeue_list = []
      self.bin = []
      self.out = ''

   def size(self):
      return f"{len(self.queue)}"

   def is_empty(self):
      return len(self.queue) == 0

   def enqueue(self, value):
      return self.queue.append(value)

   def peek(self):
      if not self.is_empty():
         return self.queue[0]
      return None

   def dequeue(self):
      if not self.is_empty():
         self.bin.append(self.peek())
         self.dequeue_list.append(self.peek())
         return self.queue.pop(0)
      return "Empty"
   

   def inqueue(self):
      if not self.is_empty():
         a = ''
         for i in self.queue:
            a += i+", "
         a = a[:-2]
         return a
      return "Empty"

   def __str__(self):
      self.out = ''
      if not self.is_empty():
         if len(self.bin) != 0:
            for i in self.bin:
               self.out += i+", "
            self.out = self.out[:-2]
            self.out += ' : '
            for i in self.queue:
               self.out += i+", "
            self.out = self.out[:-2]
            return f"{self.out}"
         else:
            self.out += 'Empty'
            self.out += ' : '
            for i in self.queue:
               self.out += i+", "
            self.out = self.out[:-2]
            return f"{self.out}"
      else:
         if len(self.dequeue_list) != 0 :
            for i in range(0,len(self.dequeue_list)):
               self.out += self.dequeue_list[i]
               self.out += ", "
            self.out = self.out[:-2]
            self.out += ' : '
            if len(self.queue) != 0:
               for i in self.queue:
                  self.out += i+", "
            else:
               self.out += "Empty"
            return f"{self.out}"
         else:
            if len(self.queue) == 0 and len(self.dequeue_list) == 0:
               return "Empty : Empty"
            else:
               return "Empty"

token = input("Enter Input : ").split(",")
queue = Queue()
for i in token:
   if len(i) > 1:
      command, value = i.split(" ")
      if command == 'E':
         queue.enqueue(value)
         print(queue.inqueue())
      else:
         print("Error command")
         break
   else:
      if len(queue.inqueue()) >= 0 and queue.inqueue() != 'Empty':
         print(queue.dequeue()+" <- ",end = '')
      print(queue.inqueue())

print(queue)