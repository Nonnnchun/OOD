def print_a_to_smt(a, ch):
   if a > ch:
      print()
      return
   else:
      print(chr(a), end="")
      return print_a_to_smt(a + 1, ch)

def recursive_up(char_ord, a_ord):
   if char_ord < a_ord:
      return
   else:
      recursive_up(char_ord - 1, a_ord)
      return print_a_to_smt(a_ord, char_ord)

def recursive_down(char_ord, a_ord):
   if char_ord < a_ord:
      return
   else:
      print_a_to_smt(a_ord, char_ord)
      return recursive_down(char_ord - 1, a_ord)


character = input("Enter input: ").upper()
recursive_up(ord(character), ord('A'))
recursive_down(ord(character) - 1, ord('A'))