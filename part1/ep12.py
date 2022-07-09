# เกมทายเลขลูกเต๋า

import random 

myrandom = random.randrange(1, 7) # 1 - 6
k = 1
correct = False
print ("คุณมีโอกาสตอบได้ 3 ครั้ง")
print (myrandom)
while True :
    number = int(input("ป้อนคำตอบของคุณ = "))
    
    correct = (number == myrandom) # เก็บค่า boolean = true / false
    
    if not correct :
        if (number > myrandom) :
            print ("น้อยกว่า")
        if (number < myrandom) :
            print ("มากกว่า")
    if correct :
            print ("ตอบถูกรับไปเลย 1 ล้านบาท")
            break

    if number < 0 or k == 3 :
        break
    k += 1


if not correct :
    print ("เสียใจด้วยนะ")
    print ("เฉลย = ", myrandom)
