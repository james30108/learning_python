# Loop

# while

i   = 1
sum = 0

while i <= 3 :
    sum += i
    print ("number : ", i, " sum : ", sum)
    i += 1

print ("ผลรวม = ", sum)

# for

for i in range(5) : # range คือตัวกำหนดจำนวนรอบ (start, stop, step)
    print ("รอบที่ :", i)

for i in range(0, 6, 2) :
    print ("รอบที่ :", i)

for i in range(10, 0, -1) : # นับถอยหลัง
    print ("รอบที่ :", i)

sum = 0

for i in range(1, 11) :
    sum += i
    print ("รอบที่ = ", i, " sum = ", sum)

print ("ผลรวม = ", sum)

# Loop ซ้อน Loop
i = 1
while i <= 3 :
    j = 1
    while j <= 5 :
        print ("รอบที่ = ", i, " ตำแหน่งที่ = ", j)
        j += 1
    i += 1


for i in range(1, 4) :
    print ("รอบที่ = ", i)
    for j in range(1, 6) :
        print ("ตำแหน่งที่ = ", j)


# break / continue

i = 0
while i <= 10 :
    print ("รอบที่ = ", i)
    if (i == 5) :
        break # สั่งจบโปรแกรม
    i += 1

print ("จบโปรแกรม")

i = 0
while i <= 10 :
    i += 1
    if (i == 5) :
        continue # ข้ามคำสั่ง
    print ("รอบที่ = ", i)

print ("จบโปรแกรม")

