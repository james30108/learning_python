# ตัวจัดการ File

# -----------------
# การอ่าน Text Flie

# open ("ชื่อไฟล์", "โหมด หรือ รูปแบบการทำงาน", "การเข้ารหัส ระบุหรือไม่ระบุก็ได้") 
# ต้องมีการประกาศทุกครั้งเมื่อมีการจัดการไฟล์

# r = read (อ่านอย่างเดียว),
# w = write (เขียนทับ)
# a = append (การต่อข้อความลงในไฟล์ หรือการเพิ่มข้อมูล)

fr = open ("student.txt", "r", encoding="utf-8") # r คืออ่านได้อย่างเดียว
print (fr) # แสดงข้อมูลของไฟล์
print (fr.read()) # อ่านไฟล์
print (fr.read(10)) # อ่านไฟล์ 10 ตัว

fr.readline () # การอ่านทีละบรรทัด
fw.write ("Hello Score \n") # เขียนข้อความลงในไฟล์
fw.writelines ("Hello Score") # เขียนข้อความแบบยาวๆแบบบรรทัดเดียว
fw.close () # ปิดการทำงาน โดยให้ทำการปิดการทำงานทุกครัง้ที่ใช้งานเสร็จสิ้น

# ตัวอย่งาการทำงาน

try :
    fr = open ("studentsss.txt", "r", encoding="utf-8")
    fr.close ()
except FileNotFoundError :
    print ("หาไฟล์ไม่เจอ")


# ---------------
# การลบไฟล์

import os # ให้ import ทุกครั้งที่จะทำการลบไฟล์
os.remove("student.txt") # การลบไฟล์

# ตัวอย่างการทำงาน
if os.path.exists("student.txt") : # ใช้ในการเช็คว่าไฟล์มีอยู่ไหม
    os.remove("student.txt") # ถ้ามีก้ให้ทำการลบไฟล์
