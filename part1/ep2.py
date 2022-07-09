# ตัีวอย่างโปรแกรมคำนวนค่า BMI
# สูตร BMI = น้ำหนัก (kg) / ส่วนสูงยกกำลัง 2 (เมตร)

# input
weight  = int(input("น้ำหนัก (kg) = "))
high    = int(input("ส่วนสูง (cm) = "))

# process
high    /= 100 # แปลง เซนติเมตร เป็น เมตร
bmi     = weight / (high ** 2)

# putput
print("BMI ของท่านคือ ", bmi)