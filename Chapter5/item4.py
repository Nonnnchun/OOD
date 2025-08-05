class Node():
   def __init__(self, data, next=None):
      self.data = data
      self.next = next

class LinkedList():
   def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0

   def append(self, data):
      new_node = Node(data)
      if self.head is None:
         self.head = self.tail = new_node
      else:
         self.tail.next = new_node
         self.tail = new_node
      self.size += 1

   def remove_by_name(self, name):
      current = self.head
      prev = None
      while current:
         if current.data == name:
               if prev is None:
                  self.head = current.next
               else:
                  prev.next = current.next
               if current == self.tail:
                  self.tail = prev
               self.size -= 1
               return True
         prev = current
         current = current.next
      return False

   def list_names(self):
      current = self.head
      names = []
      while current:
         names.append(current.data)
         current = current.next
      return names

   def is_empty(self):
      return self.size == 0

class AntColony():
   def __init__(self, w, a):
      self.ant_list = LinkedList()
      self.worker_count = 0
      self.army_count = 0
      self.anger = 0
      self.create_initial_ants(w, a)

   def create_initial_ants(self, w, a):
      for i in range(1, w + 1):
         self.worker_count += 1
         self.ant_list.append(f'W{self.worker_count}')
      for i in range(1, a + 1):
         self.army_count += 1
         self.ant_list.append(f'A{self.army_count}')

   def show_ants(self):
      names = self.ant_list.list_names()
      # List all worker ants
      worker_ants = [n for n in names if n.startswith('W')]
      soldier_ants = [n for n in names if n.startswith('A')]

      print("-> Remaining worker ants:", ' '.join(worker_ants) if worker_ants else 'Empty')
      print("-> Remaining soldier ants:", ' '.join(soldier_ants) if soldier_ants else 'Empty')

   def add_workers(self, count):
      # Reset worker numbering
      self.worker_count = 0
      for i in range(count):
         self.worker_count += 1
         self.ant_list.append(f'W{self.worker_count}')

   def add_soldiers(self, count):
      # Reset soldier numbering
      self.army_count = 0
      for i in range(count):
         self.army_count += 1
         self.ant_list.append(f'A{self.army_count}')

   def carry_food(self, amount):
      if amount == None:
         return "Food carrying mission : Empty"
      print("Food carrying mission :", end=' ')
      current = self.ant_list.head
      used = []
      total = 0
      # Use workers first
      while current and total < amount:
         if current.data.startswith('W'):
               used.append(current.data)
               total += 2
         current = current.next

      # Then use soldiers
      current = self.ant_list.head
      while current and total < amount:
         if current.data.startswith('A') and current.data not in used:
               used.append(current.data)
               total += 5
         current = current.next

      if total >= amount:
         print(' '.join(used))
         for name in used:
               self.ant_list.remove_by_name(name)
      else:
         print(' '.join(used) if used else 'Empty')
         print("The food load is incomplete!")
         print("Queen is angry! ! !")
         self.ant_list.head = None
         self.anger += 1
         if self.anger >= 3:
               print("**The queen is furious! The ant colony has been destroyed**")
               exit()

   def fight_enemy(self, hp):
      print("Attack mission :", end=' ')
      current = self.ant_list.head
      used = []
      total = 0
      # Use soldiers first
      while current and total < hp:
         if current.data.startswith('A'):
               used.append(current.data)
               total += 10
         current = current.next

      # Then use workers
      current = self.ant_list.head
      while current and total < hp:
         if current.data.startswith('W') and current.data not in used:
               used.append(current.data)
               total += 5
         current = current.next

      if total >= hp:
         print(' '.join(used))
         for name in used:
               self.ant_list.remove_by_name(name)
      else:
         print(' '.join(used) if used else 'Empty')
         print("Ant nest has fallen!")
         exit()


print("***This colony is our home***")
raw_input = input("Enter input : ")

init, commands = raw_input.strip().split('/')
w, a = map(int, init.strip().split())
colony = AntColony(w, a)

print("Current Ant List:", ' '.join(colony.ant_list.list_names()) or 'Empty')
print("")

for command in commands.strip().split(','):
   if command.startswith('C'):
      x = int(command[2:])
      colony.carry_food(x)
   elif command.startswith('F'):
      x = int(command[2:])
      colony.fight_enemy(x)
   elif command.startswith('W'):
      y = int(command[2:])
      colony.add_workers(y)
   elif command.startswith('A'):
      y = int(command[2:])
      colony.add_soldiers(y)
   elif command == 'S':
      colony.show_ants()