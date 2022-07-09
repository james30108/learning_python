# List (Array)

number = [] # create List
all = [10, "ทดสอบ", True, 3.14] # ตัวอย่าง List

all = list([10, "ทดสอบ", True, 3.14]) # การประกาศแบบ constructor คือ การประกาศแบบบอกชนิดข้อมูลลงไปด้วย

print (all)
print (type(all))

# การเข้าถึงข้อมูลของ List
print (all[0])
print (all[1])
print (all[1:3])
print (all[2:])

# การแก้ไขข้อมูล
number = [1,2,3,4,5]

print ("ก่อนแก้ไข => ", number)
number[2]   = 9
number[-1]  = "James"
print ("หลังแก้ไข => ", number)

# การแสดงผลด้วย Loop
for x in number :
    print ("สมาชิก = ", x)

# การตรวจสอบข้อมูล
fruit = ["มะละกอ", "กลว้ย", "ส้ม"]
if "มะยม" in fruit :
    print ("เป็น")
else :
    print ("ไม่เป็น")

# การนับจำนวน
print (len(number))

# len ทำงานร่วมกับ for
for i in range(len(fruit)) :
    print (fruit[i])

for item in fruit :
    print (item)

# การเพิ่มข้อมูลมาต่อท้ายใน list
fruit.append("มะปราง")

# การเพิ่มข้อมูลโดยใช้คำสั่ง insert
fruit.insert(1, "ทุเรียน") # ใส่หมายเลข index ที่กำหนดในใส่ลงไปเสมอ

# การลบข้อมูลออกขาก List
"""
fruit.remove ("มะปราง") # ลบสมาชิกที่ตรงกับข้อมูลที่ระบุ
fruit.pop() # ลบสมาชิกตัวสุดท้ายออกไป
fruit.clear() # ลบเฉพาะสมาชิกทั้งหมด
del fruit[1] # ลบข้อมูลจากตำแหน่ง index ที่ต้องการ
del fruit # ลบทั้งหมด หรือลบตัวแปรนั้นๆทิ้งไปเลย
"""



# การคัดลอกข้อมูล
fruit = ["มะละกอ", "กลว้ย", "ส้ม"]
x = []
x = fruit.copy() # คัดลอกข้อมูล


# การรวมข้อมูลระหว่าง List
all = number + fruit # ใช้การ + ได้เลย
number.extend(fruit) # ทำการเพิ่มข้อมูลเข้าสู่ List number โดยไม่ต้องสร้างตัวแปรใหม่เพิ่มขึ้นมา

# การค้นหาข้อมูล
number = [1,2,2,3,3,3,4,5]
x = number.count(3) # ค้นหาหมายเลข 5 ใน number
print(x)
