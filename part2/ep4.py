# Set

"""
- คล้าย List กับ Tuple
- ความแตกต่างคือ Set จะมีสมาชิกซ้ำกันไม่ได้
- แต่มีชนิดที่แตกต่างกันได้
- ลำดับไม่แน่นอน
- แก้ไขข้อมูลสมาชิกไม่ได้เนื่องจากไม่มี index ระบุตำแหน่ง

[] List
() Tuple
{} Set
"""

fruit = {10, "มะม่วง", True, "มะขาม"}
fish  = set(["ปลาหมอ", "ปลาดุก"]) # สร้างแบบ constructor
print(fruit)

lis = ["ปลาทู", "ปลาตะเพียน"]
fish = set[lis] #แปลงจาก list เป็น set
print(fish) 

#การเพิ่มข้อมูลสมาชิก
fruit.add("ทุเรียน")
fruit.add("สัปปะรด")
fruit.update(lis) # เพิ่มทีละหลายๆตัว

print(fruit)

# การใช้ loop
for item in fruit :
    print ("ข้อมูล = ", item)


len(fruit) # การนับจำนวน

# การเช็คข้อมูล
if ("มะเฟือง" in fruit) :
    print ("มีใน Set")

# หรือสามารถเช็คแบบนี้ก็ได้
print ("มะเพือง" in fruit ) # true or false


# การลบข้อมูล
fruit.remove("ทุเรียน") # ทำการลบข้อมูลเมื่อพบค้นหาและเจอข้อมูลที่ต้องการให้ลบ และแสดงข้อความ error เมื่อค้นหาและไม่เจอข้อมูลที่ต้องการลบ
fruit.discard("มะนาว") # ทำการลบข้อมูลเมื่อพบค้นหาและเจอข้อมูลที่ต้องการให้ลบ และไม่มีการแสดงข้อความ error เมื่อค้นหาและไม่เจอข้อมูลที่ต้องการลบ
fruit.clear() # ลบสมาชิกทั้งหมดทิ้ง
del fruit # ลบทิ้งทั้งตัวแปรและข้อมูลใน Set
print (fruit)