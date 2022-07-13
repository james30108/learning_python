"""
OOP

ประกอบไปด้วย 

1. CLass 
=ต้นแบบของวัตถุ

2. Object
= หรือก็คือวัตถุ ประกอบไปด้วย

2.1 Attribute = คุณสมบัติ
2.2 Method = พฤติกรรม หรือฟังก์ชั่น

----------

คุณสมับติของการทำ OOP ประกอบไปด้วย
1. การห่อหุ่ม (Encapsulation)
2. การสืบทอด (Inheritance)
3. การพ้องรูป (Polymorphism)
"""

# ตัวอย่าง การสร้าง class
# ควรสร้างโดยที่ตัวแรกเป็นตัวพิมพ์ใหญ่
class Employee:

    # attribute
    x = 5
  
    # method or function
    def detail(self): # ระบุ self ด้วยหากไม่มีการส่งค่ารักค่าอะไร
        print("Employee Class")
        # ตัวอย่างการนิยามตัวแปร
        self.name = "เจมส์"
        self.salary = 50000
        print ("กำหนดคุณสมบัติเรียบร้อย")
        print ("name = ", self.name)
        print ("salary = ", self.salary)
    
    # แบบมีการส่งค่า
    def detail2 (self, name, salary):
        self.name = name
        self.salary = salary
        print ("name 2 = ", self.name)
        print ("salary 2 = ", self.salary)
    
    # ตัวอย่าง constructer method 
    def __init__ (self):
        print ("Default Constructer")


class Employee2:

    # constructer แบบรับค่า
    def __init__ (self, company, year):
        print ("บริษัท = ", company, " ปีที่ก่อตั้ง ", year)



# ---------------------
# การเรียกใช้งาน 

# ตัวอย่างการสร้าง Object
employee_1 = Employee()
employee_2 = Employee2("deer-ary", "2020")

# เรียกใช้งาน attribute
print(employee_1.x)
# เรียกใช้งาน method
employee_1.detail()
employee_1.detail2("nathasophon", 15000)


# ---------------------
# การเรียกใช้งานฟังก์ชั่นเสริม

# ตรวจเช็คว่า object ที่สร้างมาจาก class ที่ระบุหรือเปล่า
print (isinstance(employee_1, Employee)) # true

# แสดงข้อมูลภายใน class
print (dir(employee_1))

# แสดงข้อมูลว่า object มาจาก class อะไร
print (employee_1.__class__)