# ---------------------------------------------------
# ฟังก์ชั่น เรียก ฟังก์ชั่นตัวเอง (Recursive Function)

# หาค่า แฟกทอเรียล 
# หรือการนำจำนวนเต็มบวกมาคุณกันไปเรื่อย

"""
5! = 5*4*3*2*1
4! = 4*3*2*1
"""

from email import message
from statistics import mean
from unittest import result


def factorial (number) :
    if number == 1 :
        return number
    else :
        return number * factorial (number - 1)


x = factorial (5)
print (x)




# ---------------------------------------------------
# หาค่า ฟีโบนัชชี
# นำสองตัวหน้ามาบวกกันไปเรื่อยๆ โดยย้ายตัวแหน่งไปที่ละ 1 ขั้น

def fibonacci (number) :
    if number <= 1 :
        return number
    else :
        return fibonacci (number - 1) + fibonacci (number - 2)

for i in range (5) : # 0 - 4
    print (fibonacci(i)) # 0,1,1,2,3



# ---------------------------------------------------
# ฟังก์ชั่นเช็คตัวอักษร


"""
def checkString (message) :
    result = {"UPPRER" : 0, "LOWER" : 0}
    for c in message :
        if c.isupper () :
            result["UPPRER"] += 1
        elif c.islower () :
            result ["LOWER"] += 1
        else :
            pass
    return result

message = input ("Your Message : ")
x = checkString (message)
print (x)
"""




# ---------------------------------------------------
# การค้นหาเบอร์โทร

"""
data = {"191" : "แจ้งเหตุด่วน", "1668" : "รถโรงพยาบาล"}

def searchNumber (message) :
    for key, value in data.items () :
        if value == message :
            print ("เบอร์ติดต่อ = ", key)
        else :
            print ("ไม่มีข้อมูล")
            return

message = input ("ป้อนข้อมูลที่ต้องการ = ")
searchNumber (message)
"""



# ---------------------------------------------------
# หอคอยฮานอย

"""
n = จำนวนจาน
เสา => A,B,C

มีจำนวนจาน 3 ใบ
n = 1
n = 2 (n - 1)
n = 3 (ใหญ่สุด)
"""

def hanoi (n, a, b, c) :
    if (n == 0) :
        return
    hanoi (n - 1, a, b, c)
    print ("จานที่ = ", n, "จาก = ",a , " ไป = ", c)
    hanoi (n - 1, b, c, a)

hanoi (3, "A", "B", "C")