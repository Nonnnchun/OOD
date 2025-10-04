def binarySearch(lst, key):
   low = 0
   high = len(lst) - 1
   if key<lst[0]: return -1
   if key>lst[-1]:return 999
   while low <= high:
      mid = (high + low) // 2 
      if key > lst[mid]:    
         low = mid + 1
      elif key < lst[mid]:
         high = mid - 1
      else:
         return float(mid)
   
   lower_idx, upper_idx = low, high
   lower_val, upper_val = lst[lower_idx], lst[upper_idx]
   decimal = (key - lower_val) / (upper_val - lower_val)
   idx = (upper_idx - lower_idx) * decimal + lower_idx
   return idx

def is_sorting(lst):
   pre = 0
   for i in lst:
      if pre<=i:
         pre = i
      else : 
         return False
   return True

def percentile(idx, n):
   if idx == 999 : idx = n-1
   per = (idx + 1) * 100/ n 
   return per if per != 0 and per != 100 else int(per)

inp = input("Enter Input : ").split("/")
lst = list(map(float, inp[0].split()))
key = float(inp[1])
if is_sorting(lst): 
   idx = binarySearch(lst, key)

print()
print(f"index      :   {idx}")
print(f"percentile :   {percentile(idx, len(lst))}")