# Function

# การสร้าง Function

def sayhi () :
    print ("Hello")

def saybye () :
    print ("Good Bye")

def add () :
    x = 3 + 1
    print (x)

# เรีกยกใช้งาน

sayhi ()
saybye ()
add ()


# Global Variable / Local Variable
# Global Variable = ทำงานได้ทุกส่วน (อยู่นอก Function)
# Local Variable = ทำงานได้เฉพาะส่วน (อยู่ใน Fuction)

def displayNumber () :
    x = 10 # Local Variable
    print ("Local Variable = ", x)


x = 20 # Global Variable
displayNumber ()
print ("Global Variable = ", x)


# การรักค่าส่งค่าใน Function

def myData1 (data) : # Parameter
    print ("Hello = ", data)

name = "James"
myData1 (name) # Arguments


# ---------------------------------------------------
# * Agrs
# สามารถทำงานกับ Arguments แบบไม่จำกัดจำนวน  *ชื่อตัวแปรที่ต้องการ 
# แปลงการเก็บข้อมูลเป็นแบบ tuple

def myData2 (*agrs) :
    sum = 0
    for item in agrs :
        sum += item
    print (sum)

myData2 (10)
myData2 (10,20)
myData2 (10,20,30)


# ---------------------------------------------------
# Keyword Arguments
# การผูก Parameter กับ arguments

def myData3 (fname, lname, city) :
    print ("ชื่อ = ", fname)
    print ("นามสกุล = ", lname)
    print ("จังหวัด = ", city)

myData3 (city = "ระยอง", lname = "ใจดี", fname = "นัท") # ทำการผูกข้อมูลที่สั่งกับ arguments ของฟังก์ชั่น


# ---------------------------------------------------
# Default Parameter
# การกำหนดค่าเริ่มต้นให้กับ Parameter

def myData4 (fname , lname, city = "กรุงเทพ") : # การกำหนดค่าเริ่มต้นนของ city เป็น กรุงเทพ
    print ("ชื่อ = ", fname)
    print ("นามสกุล = ", lname)
    print ("จังหวัด = ", city)

myData4 ("john", "doe") # กรณีที่ไม่ส่ง city ไป


# ---------------------------------------------------
# List Parameter
# การส่งข้อมูลแบบ List, Tuple เข้าไปใน Function

def myData5 (item) : 
    print (item)

fruit  = ["มะม่วง", "มะนาว"] # list
fruit2 = ("ผักกาด", "ชะอม") # Tuple
myData5 (fruit)
myData5 (fruit2)


# ---------------------------------------------------
# ฟังก์ชั่นแบบ return ค่า
# สำหรับส่งค่าออกไปใช้งานต่อ

def myData6 (a, b) : 
    return a + b

x = myData6 (10, 20)
print (x)

# กรณีที่ return ค่า break 
def myData7 (x) : 
    if x < 3 : # เช็คว่าตัวเลขที่ 3 หลักไหม
        return # return ค่าว่างออกไป มีค่าคล้ายๆ break
    else :
        return "เสร็จสิ้น"

x = myData7 (12)
print (x)



# ---------------------------------------------------
# ** kwargs
# ในงานในกณีที่ใส่ parameter มาเกิน arguments ที่กำหนด
# เก็บข้อมูลแบบ Dictionary

def myData8 (**kwargs) :
    print (kwargs)
    print (kwargs["fname"])

myData8 (fname = "james", lname = "joe")
myData8 (fname = "champoo")
myData8 (fname = "music", lname = "fahsai", city = "bangkok")



# ---------------------------------------------------
# ฟังก์ชั่น เรียก ฟังก์ชั่น

def compare (x, y) :
    if x > y : # ห่าค่ามากที่สุด แล้ว return ออกไป
        return x
    else :
        return y

def myData9 (x, y, z) :
    return compare (compare(x, y), z) # ฟังกืชั่นซ้อนฟังก์ชั่น เพื่อหาค่ามากที่สุด

max = myData9 (3, 6, 5)
print ("ค่ามากที่สุดค่า = ", max)



# ตัวอย่างที่ 2 

def food () :
    print ("หูฉลาม")

def city () :
    food ()
    print ("กรุงเทพ")

city()





# ---------------------------------------------------
# ฟังก์ชั่น เรียก ฟังก์ชั่นตัวเอง (Recursive Function)

"""
หลักการ
- หาจุดวนซ้ำ
- หาจุดออกจาก function
"""

# ตัวอย่างที่ 1
def myData10 (number) :

    if number == 5 :
        return # break
    
    print (number)
    number += 1
    myData10 (number)

myData10 (0)




# ---------------------------------------------------
# lamda function (Anonemaus Function)
# ฟังก์ชั่นแบบไม่กำหนดชื่อ
# รูปแบบคือ lambda argument : expression


x = lambda name : name
print (x ("James"))

sum = lambda x, y : x + y
print (sum (5, 10))




# ---------------------------------------------------
# การส่งค่า return ออกมาหลายค่า

def myData11 (number) :
    total, avg = 0, 0
    for i in number :
        total += i
    avg = total / len (number)
    return total, avg

x = [1, 2, 3]
y = myData11 (x)
total, avg = myData11 (x)
print (y)
print (total)
print (avg)