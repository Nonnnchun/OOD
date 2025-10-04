# ------------------------- default: sort by price -------------------------

def quickSort(l, key=lambda x: x[1]):
   qSort(l, 0, len(l)-1, key)


# --------------------------------------------------------------------------

def qSort(l, left, right, key):
   if left < right:
      p = partition(l, left, right, key)
      qSort(l, left, p - 1, key)
      qSort(l, p + 1, right, key)

def partition(l, left, right, key):
   if left == right - 1:  # only 2 elements
      if key(l[left]) > key(l[right]):
         l[left], l[right] = l[right], l[left]  # swap
      return left

   pivot = l[left]  # first element pivot
   i, j = left + 1, right
   while i < j:
      while i < right and key(l[i]) <= key(pivot):
         i += 1
      while j > left and key(l[j]) >= key(pivot):
         j -= 1
      if i < j:
         l[i], l[j] = l[j], l[i]  # swap
   if left != j:
      l[left], l[j] = l[j], l[left]
   return j

def sort_item(data):
   print("----------------------------------------")
   print("Sort by price :")
   tmp = data[:]
   quickSort(tmp, key=lambda x: x[1])
   print_items(tmp)
   
   print("----------------------------------------")
   print("Sort by price and alphabet :")
   tmp = data[:]
   quickSort(tmp, key=lambda x: (x[1], x[0]))
   print_items(tmp)



def print_items(data):
   for i, (name, price) in enumerate(data):
      print(f"{i+1:>2}. {name:<12}{price:>4}")


inp = (input("Enter Input : ")).split(",")
data = [(name, int(price)) for item in inp for name, price in [item.split()]]
sort_item(data)