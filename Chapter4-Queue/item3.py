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

def hot_potato(player, stop):
   if len(player) == 1:
      print("")
      print(f"The winner is: {player[0]}!")
   else:
      queue = Queue()
      queue.list = player
      if stop == 0:
         print(f"{queue.list[0]} is the first player holding the potato")
         eliminate = queue.list[0]
         queue.dequeue()
         print(f"Eliminated: {eliminate}. Remaining players: {queue.list}")
         return queue.list
      else:
         print(f"{queue.list[0]} is the first player holding the potato")
         queue.enqueue(queue.peek())
         queue.dequeue()
         for _ in range(0,stop-1):
            print(f"  Potato passed to: {queue.list[0]}")
            queue.enqueue(queue.peek())
            queue.dequeue()
         print(f"  Potato passed to: {queue.list[0]}")
         eliminate = queue.list[0]
         queue.dequeue()
         print(f"Eliminated: {eliminate}. Remaining players: {queue.list}")
         return queue.list


print("*****Hot Potato Game*****")
player, time_to_stop = input("Enter Input: ").split("/")
player_list = player.split(",")


for i in range(0,len(player_list)):
   hot_potato(player_list, int(time_to_stop))