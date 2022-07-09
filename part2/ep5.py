# Set

# union (รวมข้อมูลทั้งหมด)
fruitA = {"กล้วย","มะยม", "แอปเปิ้ล"}
fruitB = {"แอปเปิ้ล","กีวี","มะม่วง"}

all = fruitA.union(fruitB) # รวมสมาชิก
fruitA.update(fruitB) # นำสมาชิกของ B มาต่อกับ A โดยไม่ต้องใช้ตัวแปรใหม่
fruitW = fruitA.copy() # copy ข้อมูลจาก A มาใส่ C

# Difference (ข้อมุลที่แตกต่างกัน)
fruitC = fruitA.difference(fruitB) # ดูว่าข้อมูลที่แตกต่างกันมีอะไรบ้าง โดยนำข้อมูล A เป็นหลัก
fruitD = fruitB.difference(fruitA) # ดูว่าข้อมูลที่แตกต่างกันมีอะไรบ้าง โดยนำข้อมูล B เป็นหลัก
fruitA.difference_update(fruitB) # นำข้อมูลที่แตกต่างมาเก็บลงในข้อมูล A
print (fruitC)
print (fruitD)

# Intersection (แสดงข้อมูลที่เหมือนกัน)
fruitE = fruitA.intersection(fruitB)
print (fruitE)

# subset (เซ็ตย่อย)
fish = {"ปลาดุก", "ปลาหมอ", "ปลาวาฬ", "ปลาโลมา"}
x = {"ปลาหมอ", "ปลาดุก"}
print (x.issubset(fish)) # เช็คว่า x เป็น subset ของ fish ไหม (เช็คว่าอยู่ในกลุ่มเดียวกันไหม) True / False
print (x.issuperset(fish)) # เช็คว่า x เป็น superset ของ fish ไหม (เช็คว่าเป้นเซ้ตแม่ของ subset นั้นไหม) True / False

# superset คือการนำสมาชิกชิกทั้งหมดมาค้นหาสมิชิกย่อย
# subset คือการนำสมาชิกย่อยมาหาว่าเป็นส่วนหนึ่งจากสมาชิกหลัก (superset) หรือไม่

# หาค่าต่ำสุด / สูงสุด
number = {1,2,3,3,5,7}
min(number)
max(number)



# ---------------------------
# Frozen Set หรือสมาชิกที่ไม่สามารถเปลี่ยนแปลงข้อมูลได้
fruit = frozenset(["มะม่วง","มะยม","มะนาว"]) # ไม่สามารถ เพิ่ม ลบ แก้ไข ข้อมูลได้
print (fruit)