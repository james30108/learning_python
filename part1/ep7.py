# การใช้งาน String

name = "nathasophon khamdechsak" # index -> 0

print (name[0]) # แสดงตัวอักษรแรกออกมา
print (name[1]) # แสดงตัวอักษรที่สองออกมา
print (name[2:5]) # แสดงตัวอักษรที่ 2 ถึง 5
print (name[-5]) # แสดงตัวอักษรจากข้างหลังตัวที่ 5
print (len(name)) # นับจำนวนตัวอักษร
print (name.upper()) # เป็นตัวพิมพ์ใหญ่
print (name.lower()) # ให้เป็นตัวพิมพ์เล็ก
print (name.capitalize()) # ให้ตัวแรกสุดเป็นตัวใหญ่ตัวเดียว
print (name.replace("nathasophon", "James")) # คำสั่งแทนที่

address = "อยู่ถนน 4 ซอย 4 หมู่บ้าน 4"
print (address.replace("4", "5", 2)) # เลขสุดท้ายคือตัวกำหนดจำนวนที่เปลี่ยนค่า

name = "    Nathasophon Khamdechsak     "
print (len(name))
name = name.strip() # ตัวลบช่องว่าง
print (len(name))

text = "ไปซื้อกับข้าวและอาหารที่ตลาด"
x = "ข้าว" in name # การเช็คข้อความว่ามีในตัวแปรไหม ถ้ามีจะเป็น true ถ้าไม่มีเป็น false
x = "ข้าว" not in name # การเช็คข้อความว่าไม่มีในตัวแปรไหม
print (x)

# Part 2
fname = "nathasophon"
lname = "khamdechsak"
age = "38"
salary = 500.55520

fullname = fname + lname + age # การต่อข้อความ
text = "ชื่อ : {0} นามสกุล {1} อายุ {2} ตำแหน่ง {3} เงินเดือน {4:.2f}" #การจัดรูปแบบของการแสดงผล
print (text.format(fname,lname,age,"โปรแกรมเมอร์",salary))

fruit = "ไปซื้อผลไม้ มีมังคุด ทุเรียน ข้าวเหนียวทุเรียน ที่ตลาด จะแวะไปสวนทุเรียนด้วย" 
print (fruit.count("ทุเรียน")) #การนับจำนวนคำในประโยค

name = "นายกอไก่ ใจดี" 
print (name.startswith("นาย")) # เช็คคำขึ้นต้น