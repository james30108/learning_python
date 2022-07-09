# รับและเรียงลำดับข้อมูล หาจำนวนมากที่สุดและน้อยที่สุด
"""
number = []
while True :
    x = int(input("ป้อนตัวเลขของคุณ : "))
    if x < 0 :
        break
    number.append(x)

number.sort() # น้อยไปมาก
print (number)
number.reverse() # น้อยไปมาก
print (number)

print ("ค่ามากที่สุด = ", max(number))
print ("ค่าน้อยที่สุด = ", min(number))
print ("จบโปรแกรม")
"""



# -----------------------------------------
# เรียงจากหลังมาหน้า
fruit = ["มะม่วง", "มะนาว", "มะยม", "มะปราง"]
fruit = fruit[::-1]
print (fruit)


# -----------------------------------------
# หาค่าเลขยกกำลังในแต่ละสมาชิก
number = [1,2,3,4,5,6]

# เขียนแบบปกติ
for i in range(len(number)) :
    number[i] = number[i] * number[i]

print (number)

# เขียนแบบลดรูป
number = [i * i for i in number]
print (number)


# -----------------------------------------
# จับคู่คำทักทาย / บุคคล
greeting = ["สวัสดี", "Hi", "Hello"]
people = ["james", "Joe", "John"]
result = []

# เขียนแบบปกติ
for x in greeting :
    for y in people :
        result.append(x + y)

print (result)
# เขียนแบบลดรูป
result = [x + y for x in greeting for y in people]
print (result)


# -----------------------------------------
# จับคู่สินค้า / ราคา
fruit = ["มะม่วงดอง", "แตงโมปั่น", "ผรั่งแช่บ๊วย"]
price = [50,30,15]

for x, y in zip(fruit, price[::-1]) : # การ for เก้บข้อมูล 2 ตัว, จับคู่โดยให้ราคาย้อนหลัง
    print ("สินค้า = ", x, " ราคา = ", y)


# -----------------------------------------
# การค้นหาและนับจำนวนตัวอักษรในสมาชิก

message = ["aa", "aab", "cba", "bba", "cca"]
result = []

for item in message :
    result.append(item.count("a"))
print (result)