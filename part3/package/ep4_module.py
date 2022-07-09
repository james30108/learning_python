# ไฟล์โปรแกรมย่อย (Module)

# โปรแกมหาผลบวก
def addition (*args) :
    total = 0
    for i in range (len(args)) :
        total += args[i]
    print ("ผลบวก = ", total)

# หาผลลบ
def subtraction (num1, num2) :
    print ("ผลลบ = ", (num1 - num2))

def showName (name) :
    print ("ชื่อของท่านคือ = ", name)

