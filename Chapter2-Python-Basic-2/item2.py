def weirdSubtract(num,k):
   #Turn int to str --> str index
   num = str(num)
   list_of_num_for_cal = []

   #str can't change anythings but list is not --> str to list
   for i in num:
      list_of_num_for_cal.append(i)

   #If index = -1 of list == 0 then pop, else turn to int and -= 1 then covert to list again
   #Loop k time
   for i in range(1,k+1):
      try:
         temp = ''
         if list_of_num_for_cal[-1] == '0':
            list_of_num_for_cal.pop(-1)
         else:
            temp += list_of_num_for_cal[-1]
            temp = int(temp)
            temp -= 1
            temp = str(temp)
            list_of_num_for_cal.pop(-1)
            list_of_num_for_cal.append(temp)
      except:
         return 0

   weird_num = ''
   for i in range(0,len(list_of_num_for_cal)):
      weird_num += list_of_num_for_cal[i]
   weird_num = int(weird_num)

   return weird_num

n,s = input("Enter num and sub : ").split()
print(weirdSubtract(int(n),int(s)))