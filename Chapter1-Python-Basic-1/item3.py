#Pascal Triangle
number_of_row = int(input("Enter number of row : "))
list_for_cal = []
anwer_list = []
temp_list = []
index = 0

for i in range(1,number_of_row+1):
   if i == 1:
      anwer_list = [1]
   elif i == 2:
      anwer_list = [1,1]
      list_for_cal = [1,1]
   else:
      temp_list = []
      for j in range(1,len(list_for_cal)):
         temp_num = 0
         temp_num = list_for_cal[index] + list_for_cal[index+1]
         temp_list.insert(0,temp_num)
         index += 1
      temp_list.insert(0,1)
      temp_list.append(1)
      list_for_cal = temp_list
      anwer_list = list_for_cal
      index = 0

   for j in range(0,len(anwer_list)):
      print(anwer_list[j],end=" ")
   print("\n",end="")
