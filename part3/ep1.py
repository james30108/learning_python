# Exception
# - การจัดการกับความผิดพลาดของโปรแกรม
# - ใช้คำสั่ง try...Except มาจัดการ

"""
วิธีการใช้งาน

try :
    คำสั่งรันโปรแกรม
except :
    คำสั่งเมื่อโปรแกรมทำงานผิดพลาด
"""

"""
try : # ทำงานปกติ
    number1 = int (input ("จำนวนที่ 1 = "))
    number2 = int (input ("จำนวนที่ 2 = "))
    result = number1 / number2
    print (result)
except : # เมื่อทำงานผิดพลาด
    print ("โปรแกรมทำงานผิดพลาด")
"""




# ----------------------------------------
# การจัดกรกับ Exception

"""
try : # ทำงานปกติ
    number1 = int (input ("จำนวนที่ 1 = "))
    number2 = int (input ("จำนวนที่ 2 = "))
    result = number1 / number2
    print (result)
except ValueError : # เมื่อทำงานผิดพลาด 1
    print ("ต้องป้อนตัวเลขเท่านั้นถึงจะหารได้")
except ZeroDivisionError : # เมื่อทำงานผิดพลาด 1
    print ("หารด้วย 0 ไม่ได้")
"""



# ----------------------------------------
# กรณีที่ไม่ทราบชื่อ Exception
# ให้ระบุ except Exception : 

"""
try : # ทำงานปกติ
    number1 = int (input ("จำนวนที่ 1 = "))
    number2 = int (input ("จำนวนที่ 2 = "))
    result = number1 / number2
    print (result)
except Exception as e : # ให้แสดงชื่อ exception
    print (e)
"""



# ----------------------------------------
# ใช้งาน else ร่วมกับ try ... except
# else จะทำงานก็ต่อเมื่อไม่พบข้อผิดพลาดในโปรแกรม

"""
try : # ทำงานปกติ
    number1 = int (input ("จำนวนที่ 1 = "))
    number2 = int (input ("จำนวนที่ 2 = "))
    result = number1 / number2
    print (result)
    print ("โอนเงิน")
except Exception as e : # ให้แสดงชื่อ exception
    print (e)
else :
    print ("โอนเงินเสร็จสิ้น")
"""


# ----------------------------------------
# Finally
# จะทำงานโดยไม่สนใจว่าจะมีข้อผิดพลาดหรือไม่

"""
try : # ทำงานปกติ
    number1 = int (input ("จำนวนที่ 1 = "))
    number2 = int (input ("จำนวนที่ 2 = "))
    result = number1 / number2
    print (result)
except Exception as e : # ให้แสดงชื่อ exception
    print (e)
finally :
    print ("ทำงานในส่วนนี้ต่อ ไม่ว่าโปรแกรมส่วนบนจะผิดพลาดหรือไม่")
"""



# ----------------------------------------
# ทำงาน Try ... Except ร่วมกับ Loop While

"""
while True : # Loop
    try : # ทำงานปกติ
        number1 = int(input ("จำนวนที่ 1 = "))
        number2 = int(input ("จำนวนที่ 2 = "))
        if number1 == 0 and number2 == 0 :
            break
        result = number1 / number2
        print (result)
    except Exception as e : # ให้แสดงชื่อ exception
        print (e)
    finally :
        print ("ทำงานในส่วนนี้ต่อ")
"""



# ----------------------------------------
# Raise การกำหนดกฏ exception ด้วยตัวเอง 

while True : # Loop
    try : # ทำงานปกติ

        name = int(input ("ชื่อผู้ใช้ = "))
        if name == "james" :
            raise Exception ("มีผู้ใช้งานนี้ในระบบแล้ว")

        number1 = int(input ("จำนวนที่ 1 = "))
        number2 = int(input ("จำนวนที่ 2 = "))
        if number1 == 0 and number2 == 0 :
            break
        if number1 < 0 or number2 < 0 :
            raise Exception ("ไม่สามารถป้อนค่าติดลบได้") # การใช้งาน Raise 
        result = number1 / number2
        print (result)
    except Exception as e : # ให้แสดงชื่อ exception
        print (e)