"""
การพ้องรูป (Polumorphism)

Overloading method = เมธอดที่มีชื่อเหมือนกันและอยู่ในคลาสเดียวกันแต่รับค่าต่างกัน
Overriding method = เมธอดของคลาสลูกที่มีชื่อเหมือนกับเมธอดของคลาสแม่

"""

class Employee:

    _minSalrary = 12000
    _maxSalary  = 50000

    def __init__ (self, name, salary, department):
        self.__name         = name
        self.__salary       = salary
        self.__department   = department

    def _display (self):
        print ("department : ", self.__department, "name : ", self.__name, " / salary : ", self.__salary)



# ตัวอย่าง Overloading method หรือ Method ที่มีชื่อเหมือนกันแต่รับค่าต่างกัน
class Programer (Employee): 
    __department ="โปรแกรมเมอร์"
    def __init__ (self, name, salary, experiance, skill):
        super().__init__(name, salary, self.__department)
        self.__exp    = experiance
        self.__skill  = skill

    # ตัวอย่าง Overriding method
    def _display (self):
        super()._display () # เรียกใช้งาน showdata จากคลาสแม่
        print ("Exp :", self.__exp)
        print ("skill :", self.__skill)
        print ("################")



class Sale (Employee): 
    __department ="ฝ่ายขาย"
    def __init__ (self, name, salary, area):
        super().__init__(name, salary, self.__department)
        self.__area = area

    # ตัวอย่าง Overriding method
    def _display (self):
        super()._display () # เรียกใช้งาน showdata จากคลาสแม่
        print ("area :", self.__area)
        print ("################")


# การสร้าง Object
programer_1 = Programer ("เจมส์", 15000, 2, "พัฒนาเว็บ")
sale_1      = Sale ("ป่าน", 18000, "เชียงใหม่")

programer_1._display()
sale_1._display()
