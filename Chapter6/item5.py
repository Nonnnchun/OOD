def fib(n):
   if n < 0:
      return 0
   if n == 0 or n == 1:
      return n
   return fib(n-1) + fib(n-2)

def find_total(p, w):
   if p == 1:
      return w
   f = fib(p -1)
   new_weight = w * 2 - f
   a = int(new_weight / 2) + 1
   b = int(new_weight / 2) + 1

   if (a + b + f) // 2 != w:
        b += w - (a+b+f) // 2
   if a == 0 or b == 0:
      return -1
   return find_total(p - 1, a) + find_total(p - 1, b)

inp = input("Purity and Weight needed: ").split()
purity, weight = int(inp[0]), int(inp[1])

print(f"Total weight of used minerals with Purity 1 : {find_total(purity, weight)}")