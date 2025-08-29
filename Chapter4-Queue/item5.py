class Queue:
   def __init__(self):
      self.list = []

   def enqueue(self, value):
      # Find the organization number (the first digit of the number)
      org_id = int(str(value)[0])

      # Check if there is already a queue for this organization
      found = False
      for org_queue in self.list:
         if int(str(org_queue[0])[0]) == org_id:
               org_queue.append(value)  # Add the user to this organization's queue
               found = True
               break

      # If there is no queue for this organization, create a new one
      if not found:
         self.list.append([value])

      return f"Enqueued: {value}"

   def is_empty(self):
      return len(self.list) == 0

   def dequeue(self):
      if not self.is_empty():
         # Take the first number in the first organization queue
         org_queue = self.list[0]
         dequeued_value = org_queue.pop(0)
         
         # If this organization's queue is empty, remove it from the main queue
         if not org_queue:
            self.list.pop(0)
         
         return f"Dequeued: {dequeued_value}"
      return None  # If dequeue is not possible, return None

   def peek(self):
      if not self.is_empty():
         return self.list[0][0]  # See who is at the front of the first organization's queue
      return "Empty"

   @property
   def size(self):
      return sum(len(org_queue) for org_queue in self.list)

   def __str__(self):
      return f"Queue state: {str(self.list)}"


print(" ***Queue of Queue of Queue of ...*** ")
token = input("Enter Input : ").split(",")
queue = Queue()

for i in token:
   if len(i) > 2:  # Enqueue command
      cmd, people_to_queue = i.split(" ")
      if cmd == 'en':
         print(queue.enqueue(int(people_to_queue)))
         print(queue)

   else:  # Dequeue command
      cmd = i
      result = queue.dequeue()
      if result:
         print(result)
         print(queue)  # Show the queue state after dequeue
      elif queue.is_empty():
         # Show Queue state: [] when the main queue is empty
         print("Queue is empty")