"""
การสร้าง CLass แบบแยกไฟล์
"""

# ดึงไฟล์ที่เป็น class หลักเข้ามาทำงาน
from ep6_1 import Employee

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