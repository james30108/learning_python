# ดึงไฟล์ที่เป็น class หลักเข้ามาทำงาน
from ep6_1 import Employee

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