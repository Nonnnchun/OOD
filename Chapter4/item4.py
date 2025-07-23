class Queue:
   def __init__(self):
      self.list = []

   def enqueue(self, value):
      self.list.append(value)

   def is_empty(self):
      return len(self.list) == 0

   def dequeue(self):
      if not self.is_empty():
         return self.list.pop(0)
      return "Empty"

   def peek(self):
      if not self.is_empty():
         return self.list[0]
      return "Empty"

   @property
   def size(self):
      return len(self.list)

   def __str__(self):
      return str(self.list)

class Stack():
   def __init__(self):
      self.stack = []

   def push(self, token):
      self.stack.append(token)

   def is_empty(self):
      return len(self.stack) == 0

   def peek(self):
      if not self.is_empty():
         return self.stack[-1]
      return None

   def pop(self):
      if not self.is_empty():
         return self.stack.pop()
      return None

   @property
   def size(self):
      return len(self.stack)

   def __str__(self):
      return str(self.stack)

def reverse(list):
   queue = Queue()
   queue.list = list
   to_reverse = Stack()

   for _ in range(len(list)):
      to_reverse.push(queue.dequeue())

   for _ in range(to_reverse.size):
      queue.enqueue(to_reverse.pop())
   return queue.list

def reverse_overhand(queue_in, n):
   if n == 0 or n > len(queue_in):
      print("\n-------------------- Invalid Number ------------------")
      return queue_in
   else:
      queue = Queue()
      queue.list = queue_in

      to_reverse = Stack()

      for _ in range(n):
         to_reverse.push(queue.dequeue())

      for _ in range(to_reverse.size):
         queue.enqueue(to_reverse.pop())
      return queue.list

def decreasing_hindu(queue_in, n):
   if n == 0 or n > len(queue_in):
      print("\n-------------------- Invalid Number ------------------")
      return queue_in
   else:
      queue = Queue()
      temp_queue = Queue()
      queue.list = queue_in
      temp_stack = Stack()

      queue.list = reverse(queue.list)  # รีเวิร์ส queue ก่อน
      temp_queue.list = []

      for i in range(0,n):  # ทำการดำเนินการตามจำนวนที่ให้
         for _ in range(0,n-i):
            if not queue.is_empty():
               temp_stack.push(queue.dequeue())
         temp_stack.stack = reverse(temp_stack.stack)  # รีเวิร์ส stack

         for card in temp_stack.stack:
            temp_queue.enqueue(card)
         temp_stack.stack = []

      # ย้าย temp_queue ไป queue และรีเวิร์ส queue ก่อน
      queue.list = reverse(queue.list)
      temp_stack.stack = temp_queue.list
      temp_queue.list = queue.list
      queue.list = temp_stack.stack

      # ย้ายค่าที่เหลือใน temp_queue มาใส่ queue
      while not temp_queue.is_empty():
         queue.enqueue(temp_queue.dequeue())
      return queue.list


def riffle(queue_in, times):
   if times == 0 :
      print("\n-------------------- Invalid Number ------------------")
      return queue_in
   else:
      queue = Queue()
      queue2 = Queue()
      temp_queue = Queue()
      temp_stack = Stack()
      
      for i in range(0,((len(queue_in)+1)//2)):
         temp_queue.enqueue(queue_in[i])
      for i in range(((len(queue_in)+1)//2),len(queue_in)):
         queue2.enqueue(queue_in[i])

      while not temp_queue.is_empty():
         queue.enqueue(temp_queue.dequeue())
         queue.enqueue(queue2.dequeue())
      temp_stack.stack = queue.list
      temp_stack.pop()
      queue.list = temp_stack.stack

   return queue.list

card_deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
token = input("Enter Commands: ")
token = [item.strip() for item in token.split(",")]

print("")
print("-------------------- Original Deck -------------------")
print("| " + " | ".join(card_deck) + " |")

for i in token:
   try:
      shuffler, number = i.split(" ")
      number = int(number)
      queue = Queue()  # Create a queue instance for the deck
      if shuffler == 'O'and number != 0 and number < len(card_deck):
         print("\n--------------- Reverse Overhand Shuffle -------------")
         queue.list = reverse_overhand(card_deck, number)  # Shuffle the queue
         print("| " + " | ".join(queue.list) + " |")
         card_deck = queue.list
      elif shuffler == 'H'and number != 0 and number < len(card_deck):
         print("\n-------------- Decreasing Hindu Shuffle --------------")
         queue.list = decreasing_hindu(card_deck, number)  # Shuffle the queue
         print("| " + " | ".join(queue.list) + " |")
         card_deck = queue.list
      elif shuffler == 'R'and number != 0 and number < len(card_deck):
         print("\n------------------- Riffle Shuffle -------------------")
         for i in range(0,number):
            queue.list = riffle(card_deck, number)  # Shuffle the queue
            card_deck = queue.list
            print("| " + " | ".join(queue.list) + " |")
      else:
         print("\n-------------------- Invalid Number ------------------")
         card_deck = card_deck

   except:
      print("")