"""Chapter : 5 - item : 3 - โลกกลับด้าน (Upside Down World)

กาลครั้งหนึ่งนานมาแล้ว ในดินแดนที่ทุกอย่างกลับตาลปัตร เด็กชายชื่อ "กลับ" รู้สึกเบื่อหน่ายกับลำดับของตัวเลขที่เขาเห็นทุกวัน เขาจึงอยากได้โปรแกรมวิเศษที่สามารถรับรายการตัวเลขของเขา (ในรูปแบบ Linked List) แล้วแสดงผลลัพธ์แบบกลับด้าน จากหลังไปหน้าได้ ภารกิจของคุณคือช่วย "กลับ" สร้างโปรแกรมนี้ให้สำเร็จ!

ตัวอย่างเช่น ถ้าหาก Input เป็น 1 2 3 4 5 โปรแกรมจะต้องแสดงผลลัพธ์เป็น 5 4 3 2 1
"""
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def append(self, data):
      if not self.head:
         self.head = Node(data)
      else:
         current = self.head
         while current.next:
               current = current.next
         current.next = Node(data)

   def __str__(self):
      if not self.head:
         return "Empty"
      nodes = []
      current = self.head
      while current:
         nodes.append(str(current.data))
         current = current.next
      return " -> ".join(nodes)

   def reverse(self):
      prev = None
      current = self.head
      while current != None:
         next_node = current.next
         current.next = prev
         prev = current
         current = next_node
      self.tail = self.head
      self.head = prev

   def find_tail(self):
      t = self.head
      while t.next != None:
         t = t.next
      self.tail = t

# รับ Input
inp = input("Enter Input : ").split()
ll = LinkedList()
for i in inp:
   ll.append(i)

print(f"Original list : {ll}")
ll.reverse()
print(f"Reversed list : {ll}")