def is_sort(list):
   for i in range(0, len(list)-1):
      if list[i] > list[i+1]:
         return False
   return True

# def bubble(list):
#    last_index = len(list) - 1
#    swaped = True
#    while (last_index >= 1 and swaped):
#       swaped = False
#       i = 0
#       while (i < last_index):
#          if (list[i] > list[i+1]):
#             list[i], list[i+1] = list[i+1], list[i]
#             swaped = True
#          i+=1
#       last_index -= 1

def bubble(list):
   for last in range(len(list)-1,0,-1):
      swaped = False
      for i in range(last):
         if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            swaped = True
      if not swaped:
         break
   return list

l1 = [32,26,2,15,264,-183,10,0,20,-142,-1]
print(f"Is sorted? : {is_sort(l1)} -> {l1}")
l1 = bubble(l1)
print(f"bubble sort: complete")
print(f"Is sorted? : {is_sort(l1)} -> {l1}")

print("------------------------------------------------------------------------")

# def selection(list):
#    last = len(list) - 1
#    while (last >= 1):
#       biggest = list[0]
#       biggest_index = 0
#       i = 1
#       while (i <= last):
#          if list[i] > biggest:
#             biggest = list[i]
#             biggest_index = i
#          i += 1
#       list[biggest_index], list[last] = list[last], list[biggest_index]
#       last -= 1
#    return list

def selection(list):
   for last in range(len(list)-1,0,-1):
      biggest = list[0]
      biggest_index = 0
      for i in range(1, last + 1):
         if list[i] > biggest:
            biggest = list[i]
            biggest_index = i
      list[last], list[biggest_index] = list[biggest_index], list[last]
   return list

l2 = [32,26,2,15,264,-183,10,0,20,-142,-1]
print(f"Is sorted? : {is_sort(l2)} -> {l2}")
l2 = selection(l2)
print(f"selection sort: complete")
print(f"Is sorted? : {is_sort(l2)} -> {l2}")

print("------------------------------------------------------------------------")

# def insertion(list):
#    i = 1
#    while (i < len(list)):
#       insertEle = list[i]
#       ip = i
#       while (ip > 0 and list[ip-1] > insertEle):
#          list[ip] = list[ip-1]
#          ip -= 1
#       list[ip] = insertEle
#       i += 1
#    return list

def insertion(list):
   for i in range(1, len(list)):
      iEle = list[i]
      for j in range(i,-1,-1):
         if j > 0 and list[j-1] > iEle:
            list[j] = list[j-1]
         else:
            list[j] = iEle
            break
   return list

l3 = [32,26,2,15,264,-183,10,0,20,-142,-1]
print(f"Is sorted? : {is_sort(l3)} -> {l3}")
l3 = insertion(l3)
print(f"insertion sort: complete")
print(f"Is sorted? : {is_sort(l3)} -> {l3}")

print("------------------------------------------------------------------------")

def shell(list, dIncrements):
   for inc in dIncrements:
      for i in range(inc,len(list)):
         iEle = list[i]
         for j in range(i, -1, -inc):
            if list[j-inc] > iEle and j >= inc:
               list[j] = list[j-inc]
            else:
               list[j] = iEle
               break
   return list

l4 = [32,26,2,15,264,-183,10,0,20,-142,-1]
dIncrements = [5,3,1]
print(f"Is sorted? : {is_sort(l4)} -> {l4}")
l4 = shell(l4, dIncrements)
print(f"shell sort: complete")
print(f"Is sorted? : {is_sort(l4)} -> {l4}")

print("------------------------------------------------------------------------")

# from math import log2
# from math import floor
# def print90(h, i, max_i):
#    if i < max_i:
#       indent = floor(log2(i+1))
#       print90(h, (i*2)+2, max_i)
#       print('    ' * indent, h[i])
#       print90(h, (i*2)+1, max_i)

# def insertMinHeap(h, i):
#    print('insert', h[i], 'at index', i, end = ' ')
#    print(h)
#    insertEle = h[i]
#    fi = (i-1)//2 #
#    while i > 0 and insertEle < h[fi] :
#       h[i] = h[fi]
#       i = fi
#       fi = (i-1)//2
#    h[i] = insertEle
#    return h

# h = [13,14,16,20,21,19,68,65,26,32,31]
# for i in range(1, len(h)):
#    insertMinHeap(h, i)
#    print90(h, 0, i)
#    print(h)
#    print('------------------\n')

# print("------------------------------------------------------------------------")

# def delMin(h, last):
#    print('delMin', h[0], 'last index = ', last, end = ' ')
#    print(h)
#    insertEle = h[last]
#    h[last] = h[0] #inplace sort the root
#    hole = 0
#    ls = hole*2+1 # left son indicies
#    found = False
#    while ls < last and not found:
#       rs = ls if ls+1 >= last else ls+1
#       min = ls if h[ls] < h[rs] else rs # minson index
#       if h[min] < insertEle:
#          h[hole] = h[min] # promote small son up to hole
#          hole = min # going down the tree
#          ls = hole*2+1
#       else:
#          found = True
#    h[hole] = insertEle

# h = [13,14,16,20,21,19,68,65,26,32,31]
# for last in range(len(h)-1, -1, -1):
#    delMin(h, last)
#    print(h)
#    print90(h, 0, last)
#    print('------------------\n')

# print("------------------------------------------------------------------------")

def merge(l, left, right, rightEnd):
   start = left
   leftEnd = right-1
   result = []
   while left <= leftEnd and right <= rightEnd:
         if l[left] < l[right]:
            result.append(l[left])
            left += 1
         else:
            result.append(l[right])
            right += 1
   while left <= leftEnd: # copy remaining left half if any
      result.append(l[left])
      left += 1
   while right <= rightEnd: # copy remaining right half if any
      result.append(l[right])
      right += 1
   for ele in result: # copy result back to list l
      l[start] = ele
      start += 1
      if start > rightEnd:
         break
   return l

def mergeSort(l, left, right):
   center = (left+right)//2
   if left < right:
      mergeSort(l, left, center)
      mergeSort(l, center+1, right)
      merge(l, left, center+1, right)
   return l

l5 = [5,3,6,1,2,7,8,4]
print(f"Is sorted? : {is_sort(l5)} -> {l5}")
l5 = mergeSort(l5, 0, len(l5)-1)
print(f"merge sort: complete")
print(f"Is sorted? : {is_sort(l5)} -> {l5}")

print("------------------------------------------------------------------------")

def qSort(l, left, right):
   if left < right :
      p = partition(l, left, right)
      qSort(l, left, p - 1)
      qSort(l, p + 1, right)
   return l

def quickSort(l) :
   qSort(l, 0, len(l)-1)
   return l

# def partition(l, left, right):
#    if left == right - 1 : #only 2 elements
#       if l[left] > l[right] :
#          l[left],l[right] = l[right],l[left] #swap
#       return left
#    pivot = l[left] #first element pivot
#    i, j = left + 1, right
#    while i<j:
#       while i<right and l[i]<=pivot:
#          i += 1
#       while j>left and l[j]>=pivot:
#          j -= 1
#       if i<j:
#          l[i], l[j] = l[j], l[i] #swap
#    if left is not j:
#       l[left], l[j] = l[j], l[left]
# # swap pivot to index j
#    return j

def partition(l, left, right) :
   if left == right - 1 : #only 2 elements
      if l[left] > l[right] :
         l[left],l[right] = l[right],l[left] #swap
      return left

   c = (left + right)//2 #order #order c <= l <= r
   if l[left] < l[c] :
      l[left],l[c] = l[c],l[left]
   if l[right] < l[c] :
      l[c],l[right] = l[right],l[c]
   if l[right] < l[left] :
      l[left],l[right] = l[right],l[left]

   pivot = l[left] #first element pivot
   i, j = left + 1, right
   while i<j:
      while i<right and l[i]<=pivot:
         i += 1
      while j>left and l[j]>=pivot:
         j -= 1
      if i<j:
         l[i], l[j] = l[j], l[i] #swap
   if left is not j:
      l[left], l[j] = l[j], l[left]
# swap pivot to index j
   return j

l = [5,1,4,9,6,3,8,2,7,0]
print(f"Is sorted? : {is_sort(l)} -> {l}")
l = quickSort(l)
print(f"quick sort: complete")
print(f"Is sorted? : {is_sort(l)} -> {l}")