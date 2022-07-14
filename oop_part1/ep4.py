"""

การสืบทอดคุณสมบัติ (Inheritance)

"""

# Super class = คล่าสแม่
class Employee:

    _minSalrary = 12000
    _maxSalary  = 50000

    def __init__ (self, name, salary, department):
        self.__name         = name
        self.__salary       = salary
        self.__department   = department
        self.__display()

    def __display (self):
        print ("department : ", self.__department, "name : ", self.__name, " / salary : ", self.__salary)

    # method สำหรับแปลง object เป็น string
    def __str__(self):
        return ("str : " + self.__name)


# Subclass = คลาสลูก
class Programer (Employee): # ใส่คลาสที่ต้องการสืบทอดคุณสมบัติลงไปในวงเล็บ
    __department ="โปรแกรมเมอร์"
    def __init__ (self, name, salary):
        # super คือ คีย์เวิร์ดสำหรับการเรียกใช้งานข้อมูลในคลาสแม่
        super().__init__(name, salary, self.__department) # เรียกใช้งาน constucter จากคลาสแม่


class Sale (Employee): # ใส่คลาสที่ต้องการสืบทอดคุณสมบัติลงไปในวงเล็บ
    __department ="ฝ่ายขาย"
    def __init__ (self, name, salary):
        # super คือ คีย์เวิร์ดสำหรับการเรียกใช้งานข้อมูลในคลาสแม่
        super().__init__(name, salary, self.__department) # เรียกใช้งาน constucter จากคลาสแม่


# เรียกใช้งาน 
programer   = Programer("เจมส์", 15000)
sale        = Sale("ป่าน", 18000)

# ทดสอบการเรียกใช้งานตัวแปรจากคลาสแม่ผ่านคลาสลูก
print ("Programer min : ", programer._minSalrary, " / max : ", programer._maxSalary)
print ("Sale min : ", sale._minSalrary, " / max : ", sale._maxSalary)

print (programer.__str__())
print (sale.__str__())