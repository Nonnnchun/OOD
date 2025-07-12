#BMI Calculate
high,weight = input("Enter your High and Weight : ").split(" ")
high = float(high)
weight = float(weight)
BMI = weight/(high*high)
if BMI < 18.50:
   print("Less Weight")
elif 18.5 <= BMI <23:
   print("Normal Weight")
elif 23 <= BMI  < 25:
   print("More than Normal Weight")
elif 25 <= BMI  < 30:
   print("Getting Fat")
elif BMI  >= 30:
   print("Fat")
else:
   print("Error")