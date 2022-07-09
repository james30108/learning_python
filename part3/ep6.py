# * โปรแกรม Crack รหัสผ่าน

import random
from unittest import result 

ATM_PASSWORD = "132"
result = "" # เก็บผลลัพธ์

while result != ATM_PASSWORD : # ถ้าสุ่มไม่เจอก็ให้ทำงานไปเรื่อยๆ
    result = ""
    for letter in range (len (ATM_PASSWORD)) : # สุ่มตามจำนวนหลักของพาสเวิร์ด
        list_number = random.choice ("0123456789") # สุ่มตัวเลข
        result = "".join (list_number) + str (result) # ต่อเลขที่สุ่ม
        print ("SEARCH ", result)

print ("CRACK_PASSWORD IS ", result)