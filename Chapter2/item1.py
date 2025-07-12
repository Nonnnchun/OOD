def Rshift(number, shift):
   temp = number
   binary_num = []

   # Handle positive numbers
   if number >= 0:
      if number == 0:
         binary_num.append(0)
      while number > 0:
         binary_num.insert(0, number % 2)
         number = number // 2

      # If the binary number is less than the shift length, pad with leading zeros
      while len(binary_num) < shift:
         binary_num.insert(0,0)

   # Handle negative numbers (2's complement)
   else:
      number = abs(number)
      while number > 0:
         binary_num.insert(0, number % 2)
         number = number // 2

      # 1) Invert the bits (flip 0s to 1s and 1s to 0s)
      # binary_num = [1 - bit for bit in binary_num]
      for i in range(len(binary_num)):
         binary_num[i] = 1 - binary_num[i]

      # 2) Add 1 to the result
      binary_num[-1] = 1 - binary_num[i]

      # add bit in negatively
      if temp <= -3 :
         binary_num.insert(0, 1)

      # If the binary number is less than the shift length, pad with leading zeros
      while len(binary_num) < shift:
         binary_num.insert(0,1)

   #shift bit
   for i in range(0,shift):
      binary_num.pop(-1)

   value_after_shift = 0
   #cal to decimal
   if temp >= 0 :
      if temp == 0 :
         value_after_shift = 0
      else:
         binary_num.reverse()
         for i in range(0,len(binary_num)):
            value_after_shift += pow(2*binary_num[i],i)
   else:
      binary_num.reverse()
      for i in range(0,len(binary_num)):
         if binary_num[0] == 0 :
            binary_num.pop(0)
            binary_num.append(0)
         value_after_shift += pow(2*binary_num[i],i)
      value_after_shift = value_after_shift * (-1)

      if value_after_shift == 0 :
         value_after_shift = -1
   return value_after_shift

num,shiftcount = input("Enter number and shiftcount : ").split()
print(Rshift(int(num),int(shiftcount)))