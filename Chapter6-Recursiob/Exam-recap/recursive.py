def print_recursive(a, char):
   if a > char:
      print()
      return
   else:
      print(chr(a), end = "")
      return print_recursive(a + 1, char)

def recursive_up(char_ord, a_ord):
   if char_ord < a_ord:
      return
   else:
      recursive_up(char_ord - 1, a_ord)
      return print_recursive(a_ord, char_ord)

def recursive_down(char_ord, a_ord):
   if char_ord < a_ord:
      return
   else:
      print_recursive(a_ord, char_ord)
      return recursive_down(char_ord - 1, a_ord)

def string_len(string):
   if string == '':
      return 0
   else:
      return 1 + len(string[1:])

def fac(n):
   if n == 0 or n ==1 :
      return 1
   else:
      return n * fac(n-1)

def sum_list1(power_list):
   if len(power_list) == 0:
      return 0
   else:
      return power_list[0] + sum_list1(power_list[1:])

def sum_list2(power_list, fromI, toI):
   if fromI > toI:
      return 0
   elif fromI == toI:
      return power_list[toI]
   else:
      return power_list[fromI] + sum_list2(power_list, fromI + 1, toI)

def fibo(n):
   if n == 0 or n == 1:
      return n
   else:
      return fibo(n-2) + fibo(n-1)

l = [1,1,2,3,4,5,6,7,8,9,9]
print(f"Sum of list is : {sum_list1(l)}")
print("----------------------------------------")

print(f"Sum of list is : {sum_list2(l,1,len(l)-2)}")
print("----------------------------------------")

character = "d".upper()
print(f"Output of character : {character}")
recursive_up(ord(character), ord('A'))
recursive_down(ord(character) - 1, ord('A'))
print("----------------------------------------")

print(f"Lenght of string is : {string_len("Hello bro!")}")
print("----------------------------------------")

print(f"Factorial result is : {fac(7)}")
print("----------------------------------------")

print(f"Fibonacci result is : {fibo(8)}")
print("----------------------------------------")