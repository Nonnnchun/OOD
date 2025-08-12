def renew_message(old_message, index=0):
   #base case:
   if index == len(old_message):
      return ""
   #recursive case:
   else:
      allowed_chars = "abcdefghijklmnopqrstuvwxyz1234567890"
      current_char = old_message[index]
      if current_char in allowed_chars:
         return current_char + renew_message(old_message, index + 1)
      else:
         return renew_message(old_message, index + 1)

def check_even(message, half):
   #base case
   if len(message) == 0:
      return True
   #recursive case:
   else:
      left = message[:half]
      right = message[half:]
      return left == right[::-1]

def check_odd(message, half):
   #base case:
   if len(message) <= 1:
      return True
   #recursive case:
   else:
      left = message[:half]
      right = message[half+1:]
      return left == right[::-1]

def is_palindrom(message):
   half = len(message) // 2
   if len(message) % 2 == 0:
      return check_even(message, half)
   else:
      return check_odd(message, half)


print("**Palindrome pretty version!**")
m = input("Enter message : ").replace(" ", "").lower()
m = renew_message(m)
if is_palindrom(m):
   print("True")
else:
   print("False")