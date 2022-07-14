"""
Setter, Getter Method

---------------------
Class Variable
= ตัวแปรที่อยู่ใน class

Instance Variable
= ตัวแปรที่อยู่ใน method 
"""

from unicodedata import name


class Employee:

    #  Class Variable 
    _minSalrary = 12000
    _maxSalary  = 50000

    # private method
    __name = ""
    __salary = ""

    # Setter Method
    def setName (self, newname):
        # Instance Variable
        self.__name = newname
    def setSalary (self, newsalary):
        # Instance Variable
        self.__salary = newsalary

    # Getter method
    def getName (self):
        return self.__name
    def getSalary (self):
        return self.__salary


# เรียกใช้งาน 
employee_1 = Employee()
employee_1.setName("james") # เรียกใช้งาน setter
employee_1.setSalary(15000) # เรียกใช้งาน setter

name    = employee_1.getName() # เรียกใช้งาน getter
salary  = employee_1.getSalary() # เรียกใช้งาน getter

print ("name : ", name, " / salary : ", salary)

# ตัวอย่างการเข้าถึงตัวแปร Class Variable
print ("Class Variable min : ", employee_1._minSalrary, " max : ", employee_1._maxSalary)