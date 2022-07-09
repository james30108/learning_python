# โปรแกรมแม่สูตรคูณ
"""
start = int(input("ป้อนแม่สูตรคูณเริ่มต้น : "))
stop = int(input("ป้อนแม่สูตรคูณสุดท้าย : "))

for x in range(start, stop + 1) :
    print ("แม่ = ", x)
    for y in range(1, 13) :
        print (x, "x", y, " = ", (x * y))
"""

"""
# EP 2

start, stop = 1, 5
sum = 0
while (start <= stop) :
    number = int(input("ป้อนตัวเลขของคุณ : "))
    sum += number # บวกเลขที่ป้อนในแตละรอบ
    start += 1

print ("ผลรวม = ", sum)
"""

"""
# EP 3

sum = 0
while True :
    number = int(input("ป้อนตัวเลขของคุณ : "))
    sum += number # บวกเลขที่ป้อนในแตละรอบ
    if sum > 100 :
        break
    print ("ผลรวม = ", sum)
"""

"""
# EP 4
min, max = 0, 9999

while True :
    number = int(input("ป้อนตัวเลขของคุณ : "))
    if number < 0 :
        break
    if number > max :
        max = number
    if number < min :
        min = number

print ("ค่าสูงสุด = ", max)
print ("ค่าต่ำสุด = ", min)
"""

# ตัวเชขขั้นบันได
last = int(input("ป้อนตัวเลข = "))
for row in range (1, last + 1) :
    for column in range (1, row + 1) :
        print (column, end = "")
    print ("")