def gcd(a,b):
   #base case
   if b == 0:
      if a < 0:
         return a*(-1)
      else:
         return a

   #recursive case
   else:
      return gcd(b,a%b)

num1,num2 = input("Enter Input : ").split(" ")
num1 = int(num1)
num2 = int(num2)

if num1 == 0 and num2 == 0 :
   print("Error! must be not all zero.")
else:
   if num1 > num2:
      print(f"The gcd of {num1} and {num2} is : {gcd(num1,num2)}")
   else:
      print(f"The gcd of {num2} and {num1} is : {gcd(num1,num2)}")