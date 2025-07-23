class Queue:
   def __init__(self, init_list = []):
      self.list = init_list

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

def reverse_queue(list):
   queue = Queue()
   for card in list:
      queue.enqueue(card)

   item = queue.dequeue()
   temp = []
   while len(queue.list) > 0:
      temp.append(queue.dequeue())
   queue.enqueue(item)

   while temp:
      queue.enqueue(temp.pop())

   queue.enqueue(queue.peek())
   queue.dequeue()
   return queue

def shuffle_card(card, shuffler_cmd, times):
   queue = Queue()
   if shuffle_card == '':
      pass
   pass


card_deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
reverse_deck = reverse_queue(card_deck)

token = input("Enter Commands: ").split(", ")

for i in token:
   shuffler, number = i.split(" ")
   shuffle_card(card_deck, shuffler, number)