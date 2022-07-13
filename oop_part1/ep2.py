"""
การห่อหุ่ม (Encapsulation)
"""

class Employee:

    # public method
    def detail1 (self, name, salary): 
        # public attribute
        self.name = name
        self.salary = salary

    # protected method
    def _detail2 (self, name, salary): 
        # protected attribute
        self._name = name
        self._salary = salary

# ---------------------
# การเรียกใช้งาน 
employee_1 = Employee()

# เรียกใช้งาน public
employee_1.detail1("james", 15000) # method
employee_1.name = "nathasophon" # attribute
employee_1.salary = 20000 # attribute
