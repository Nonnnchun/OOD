def pair_five(list_of_number):
   answer_list = []
   set_of_number = []
   for first_char in range(1, len(list_of_number)+1):
      try:
         for second_char in range(1+first_char, len(list_of_number)+1):
            try:
               set_of_number = []
               for third_char in range(1+second_char, len(list_of_number)+1):
                  try:
                     set_of_number = []
                     if (list_of_number[first_char-1] + list_of_number[second_char-1] + list_of_number[third_char-1]) == 5 :
                        set_of_number.append(list_of_number[first_char-1])
                        set_of_number.append(list_of_number[second_char-1])
                        set_of_number.append(list_of_number[third_char-1])
                        if len(set_of_number) <= 3:
                           set_of_number.sort()
                        if set_of_number != set_of_number :
                           pass
                        else:
                           answer_list.append(set_of_number)
                     else:
                        pass
                  except:
                     break
            except:
               break
      except:
         break

   for check in range(0,len(answer_list)):
      try:
         for index in range(0,len(answer_list)):
            try:
               if answer_list[index] == answer_list[index+1]:
                  answer_list.pop(index+1)
            except:
               pass
      except:
         break

   return f"{answer_list}"


num = input("Enter Your List : ").split(" ")
num = [int(i) for i in num]
if len(num) < 3:
   print("Array Input Length Must More Than 2")
else:
   print(pair_five(num))