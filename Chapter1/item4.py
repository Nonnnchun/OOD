#Fun with Drawing

# for i in range(number_of_pyramid*2 - 1, 0,-1):

print("*** Fun with Drawing ***")
number_of_pyramid = int(input("Enter input : "))

#Upper pyramid
for i in range(1, number_of_pyramid*2-1):
   #    #Outer pyramid
   for j in range (1,(number_of_pyramid*4)-3):
      if j <= i:
         if j % 2 == 1:
            print("#",end = "")
         else:
            print(".",end = "")
      elif j >= number_of_pyramid*4-1-i:
         if j % 2 == 1:
            print("#",end = "")
         else:
            print(".",end = "")

      #Draw # in pyramid ...,9 ,5 ,1
      else:
         if j <= number_of_pyramid*4-3 and i % 2 == 0:
            print(".",end = "")
         else:
            print("#",end = "")
   print("#")  # สิ้นสุดด้วย #



#Lower pyramid
for i in range(1, number_of_pyramid*2):
   for j in range (1,(number_of_pyramid*4)-3):

      #Outer pyramid
      if j <= number_of_pyramid*2 -1-i:
         if j % 2 == 1:
            print("#",end = "")
         else:
            print(".",end = "")
      elif j >= number_of_pyramid*2-1+i:
         if j % 2 == 1:
            print("#",end = "")
         else:
            print(".",end = "")

      #Draw # in pyramid 1, 5, 9, ...
      else:
         if j <= number_of_pyramid*4-3 and i % 2 == 0:
            print(".",end = "")
         else:
            print("#",end = "")
   print("#")  # สิ้นสุดด้วย #