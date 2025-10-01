def is_num(word):
   return word in '0123456789'

def is_sort(data):
   for i in range(1,len(data)):
      if data[i][0] < data[i-1][0]:
         return False
   return True

def bubbler_sort(data):
   while not is_sort(data):
      for i in range(1,len(data)):
         if data[i-1][0] > data[i][0]:
            data[i], data[i-1] = data[i-1], data[i]
   return data


inp = input("Enter Input : ").split()
ans = []
dict = {
}

for i in inp:
   for j in range(len(i)):
      if not is_num(i[j]):
         dict[i[j]] = i

dict_item = list(dict.items())
dict_sort = bubbler_sort(dict_item)
for i in dict_sort:
   print(i[1], end = ' ')