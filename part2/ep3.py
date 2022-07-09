# Tuple
"""
- คุณสมับติคล้ายกับ List 
- ต่างกับ List ตรงที่ข้อมูลสมาชิกไม่สามารถเปลี่ยนแปลงได้
- เช่นเก้บ ID, รหัสที่เซ็ตเป็นค่าคงที่ต่าง ๆ

[] คือ List
() คือ Tuple
"""

# วิธีสร้าง Tuple
tup  = (1, 2, 3, 4, "James", True, 3.52)
tup2 = tuple((1,2,6,"Jmes")) # สร้างแบบ constructor
tup3 = ("james")
tup4 = ("james",)
print (tup)
print (type(tup))
print (tup[1]) # แสดง tuple ตามตำแหน่ง
print (type(tup3)) # Output => String
print (type(tup4)) # Output => Tuple


# การเปลี่ยนค่าข้อมูล Tuple
lis     = list(tup) # เป็นการแปลง tuple ให้เป็น list เพื่อให้ข้อมูลสามารถแก้ไขได้
lis[0]  = "กรุงเทพ"
tup     = tuple(lis) # แปลง list กลับไปเป็น tuple

# การใช้ for ตรวจสอบข้อมูล
for item in tup :
    print ("สมาชิก = ", item)

# การตรวจสอบข้อมูล
if "ทุเรียน" in tup :
    print ("เป็นสมาชิก")
else :
    print ("ไม่เป็นสมาชิก")

print (len(tup)) # การนับสมาชิก

# ใช้ len กับ loop for
for item in range(len(tup)) :
    print (tup[item])

# การเพิ่มข้อมูล
name = ("James", "Joe")
new  = "Nut"
new2 = ("Tom", "Ex")
name = name + (new,) + new2 # ทำการต่อข้อมูล
print (name)

# การทำงานร่วมกับ List
# การแปลง List เป็น Tuple และนำมา Join กับ Tuple
city = ["กรุงเทพ", "ชลบุรี", "อุบล"]
tup = tup + tuple(city) 

# ลบข้อมูล
"""
del tup # ลบทั้งตัวแปร
"""


# ลบเฉพาะตัวแปร
lis = list(tup) # แปลงข้อมูลเป็น List ก่อนทำการลบข้อมูล
lis.pop() # ลบข้อมูลตัวสุดท้าย
lis.remove("กรุงเทพ") # ลบข้อมูลตามที่ระบุไว้เท่านั้น
tup = tuple(lis) # แปลงข้อมุลกลับไปเป็น tuple

print (tup)

tup.count("กรุงเทพ") # ค้นหาและนับสมาชิกที่ระบุ
tup.index("กรุงเทพ") # เช็คว่าเจอข้อมูลที่ระบุใน index หรือตำแหน่งที่เท่าไหร่

# การเรียงข้อมูล 
tup  = (1, 2, 3, 4,)
lis = list(tup) # แปลงข้อมูลเป็น List
lis.sort() # เรียงข้อมูลน้อยไปมาก
lis.reverse() # เรียงข้อมูลมากไปน้อย
tup = tuple(lis) # แปลงข้อมุลกลับไปเป็น tuple

# การสลับ 
x = (5, 6)
y = (8 ,9)
x, y = y, x # ขั้นตอนการสลับค่า

# การทำ tuple ให้เป็น String
charecter = ("j","a","m","e","s")
name = "".join(charecter) # การรวมตัวอักษร

# การเรียงสมาชิกจากหลังไปหน้า
x = tuple(reversed(charecter))
print (x)