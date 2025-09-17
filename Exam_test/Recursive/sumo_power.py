"""
Chapter : 6 - item : 4 - เลขพลังซูโม่ (Sumo Power Numbers)

****** ห้ามใช้ For, While loop หรือการแปลงเป็นสตริงแล้ววนลูป *******

ในโรงเรียนสอนซูโม่แห่งหนึ่ง อาจารย์ใหญ่เชื่อว่า "พลังที่แท้จริง" ของตัวเลขไม่ได้อยู่ที่ขนาดของมัน แต่อยู่ที่ผลรวมของเลขโดดแต่ละตัว! เช่น เลข 35 จะมีพลังเท่ากับ 3 + 5 = 8 ส่วนเลข 123 จะมีพลังเท่ากับ 1 + 2 + 3 = 6

จงเขียนฟังก์ชัน sum_of_digits โดยใช้ Recursion เท่านั้น เพื่อคำนวณหา "พลังซูโม่" ของตัวเลขที่ป้อนเข้ามา

คำใบ้: พลังของเลข 123 คือ 3 บวกกับพลังของเลข 12
"""
def sum_power(power_str):
   if power_str == "":
      return 0

   if power_str[0] ==  "-":
      return int(power_str[:2]) + sum_power(power_str[2:])
   else:
      return int(power_str[0]) + sum_power(power_str[1:])

power = input()
print(f"Sum of digits is {sum_power(power)}")