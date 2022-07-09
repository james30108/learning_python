# Dictionary (Object)

"""
- คล้ายกับ Object
- มีการใช้งาน key กับ value
"""

# การสร้าง Dict
color   = {"red":"สีแดง", "yellow":"สีเหลือง", "green":"สีเีขียว", 98:"สีฟ้า"}
animal  = dict(cat="แมว", dog="หมา", duck="เป็ด") # แบบ constructor
test    = dict({"red":"สีแดง", "yellow":"สีเหลือง", "green":"สีเีขียว", 98:"สีฟ้า"}) # แบบ constructor
print(color["yellow"])
print(test)


color.update({"blue":"สีน้ำเงิน"}) # การเพิ่มข้อมูล
color.update({"red":"สีแดงสดมากๆ"}) # แกาแก้ไขข้อมูล

# การใช้ loop แสดงผลข้อมูล
for item in color.keys() : # แสดง key
    print (item)

for item in color.values() : # แสดง value
    print (item)

for k, v in color.items() : # แสดงทั้ง key และ value
    print ("key = ", k, " value = ", v)

# การตัดลอก
x = color.copy()

# การลบข้อมูล
color.pop("red")
color.popitem() # ลบข้อมูลท้ายสุด
color.clear() # ลบสมาชิกทั้งหมด
del color # ลบตัวแปรทิ้งง




# ----------------------------
# การทำ Dictionary ซ้อนกัน

market = {
    "ร้านป้าพร" : {
        "name" : "ป้าพร",
        "menu" : ["กะเพราไก่", "ก่วยเตี๋ยว"],
        "zone" : "ตะวันตก"
    },
    "ร้านลุงป้อม" : {
        "name" : "ลุงป้อม",
        "menu" : ["มะละกอ", "แตงโม"],
        "zone" : "ตะวันออก"
    },
}

print (market["ร้านป้าพร"]["menu"])

# เช็คข้อมูล
print ("ก๋วยเตี๋ยว" in market["ร้านป้าพร"]["menu"])