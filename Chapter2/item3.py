def mod_position(arr_string, modposition):
   temp_list = []
   answer_list = []

   #Trans string to list
   for i in range(0,len(arr_string)):
      temp_list.append(arr_string[i])

   #Set first index of list equal to 1
   for i in range(0,len(arr_string)):
      real_position = 1+i
      #If real_position % modposition == 0 append to answer list, else skip that position
      if real_position % modposition == 0 :
         answer_list.append(temp_list[real_position-1])

   return answer_list

print("*** Mod Position ***")
string,mod = input("Enter Input : ").split(",")
print(mod_position(str(string),int(mod)))