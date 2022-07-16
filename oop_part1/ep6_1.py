"""
การสร้าง CLass แบบแยกไฟล์
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