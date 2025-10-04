def is_sort(data):
   for i in range(1,len(data)):
      if data[i] < data[i-1]:
         return "No"
   return "Yes"

inp = [int(i) for i in input("Enter Input : ").split()]
print(is_sort(inp))