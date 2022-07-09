#โปรแกรมคำนวนค่า BMI แบบบอกรูปร่าง

# input
weight  = int(input("น้ำหนัก (kg) = "))
high    = int(input("ส่วนสูง (cm) = "))


# process
high    /= 100 # แปลง เซนติเมตร เป็น เมตร
bmi     = weight / (high ** 2)

# putput
if bmi >= 0 and bmi < 18.0 :
    result = "ต่ำกว่าเกณฑ์"
elif bmi >= 18.5 and bmi <= 22.9 :
    result = "สมส่วน"
elif bmi >= 23.0 and bmi <= 24.9 :
    result = "น้ำหนักเกิน"
elif bmi >= 25.0 and bmi <= 29.9 :
    result = "โรคอ้วน ระดับที่ 1"
elif bmi > 30 :
    result = "โรคอ้วนระดับอันตราย"
else :
    result  = "ไม่ทราบค่าที่ชัดเจน"

print ("ค่า BMI = ", bmi, " ทำนายว่า = ", result)