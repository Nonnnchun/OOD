def is_sort(data):
   for i in range(1,len(data)):
      if data[i] < data[i-1]:
         return False
   return True

def bubbler_sort(data):
   total = 0
   while not is_sort(data):
      for i in range(1,len(data)):
         if data[i-1] > data[i]:
            data[i], data[i-1] = data[i-1], data[i]
            total += 1
            print(f"Swap {total}: {' '.join(map(str, data))}")
   return data, total

def insertion_sort(data):
   total = 0
   while not is_sort(data):
      for i in range(1, len(data)):
         temp = data[i]
         j = i - 1
         while j >= 0 and data[j] > temp:
               data[j + 1] = data[j]
               j -= 1
               total += 1
               print(f"Swap {total}: {' '.join(map(str, data))}")
         data[j + 1] = temp
   return data, total

def selection_sort(data):
   total = 0
   for i in range(len(data)):
      index_min = i
      for j in range(i + 1, len(data)):
         if data[j] < data[index_min]:
               index_min = j
      if index_min != i:
         data[i], data[index_min] = data[index_min], data[i]
         total += 1
         print(f"Swap {total}: {' '.join(map(str, data))}")
   return data, total

print("*** Counted Sort ***")
inp = input("N, numbers, sort_choice: ").split(",")
nums = [int(i) for i in inp[1].split()]
method = inp[2]

if method == '1':
   sort, swaps = bubbler_sort(nums)
elif method == '2':
   sort, swaps = insertion_sort(nums)
elif method == '3':
   sort, swaps = selection_sort(nums)
else:
   print("Invalid method")

print(f"Final sorted array: {' '.join(map(str, sort))}")
print(f"Total swaps: {swaps}")