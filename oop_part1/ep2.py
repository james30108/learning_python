"""
การห่อหุ่ม (Encapsulation)
"""

class Employee:

    # self = this

    # public method
    def detail1 (self, name, salary): 
        # public attribute
        self.name = name
        self.salary = salary

    # protected method
    def _detail2 (self, name, salary): # ใส่ _ หน้าชื่อ
        # protected attribute
        self._name = name
        self._salary = salary

        self.__detail3 ("joe", 18000)

    # private method
    def __detail3 (self, name, salary): # ใส่ __ หน้าชื่อ
        # protected attribute
        self.__name = name
        self.__salary = salary
        # เรียกใช้งาน class
        self.__display () 

    def __display (self):
        print ("private name : ", self.__name, " / salary : ", self.__salary)


# ---------------------
# การเรียกใช้งาน 
employee_1 = Employee()

# เรียกใช้งาน public
employee_1.detail1("james", 15000) # method
employee_1.name = "nathasophon" # attribute
employee_1.salary = 20000 # attribute
print ("public name : ", employee_1.name, " / salary : ", employee_1.salary)

# เรียกใช้งาน protected
employee_1._detail2("james", 15000) # method
employee_1._name = "somsak" # attribute
employee_1._salary = 15000 # attribute
print ("protected name : ", employee_1._name, " / salary : ", employee_1._salary)

# เรียกใช้งาน private
# ไม่สามารถเรียกใช้งานนอก class ได้
