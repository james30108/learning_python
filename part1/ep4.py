# ตัวอย่างโปรแกรมหาค่าตัวเลข มาก / น้อย

a = int(input("ป้อนตัวเลข 1 : "))
b = int(input("ป้อนตัวเลข 2 : "))

if a > b :
    print(a, " มากกว่า ", b)
else :
    print(a, " น้อยกว่า ", b)

# ตัวอย่างโปรแกรมหาเลขคู่ / คี่

number = int(input("ป้อนตัวเลข : "))

if number % 2 == 0 :
    print("เป็นเลขคู่")
else :
    print("เป็นเลขคี่")