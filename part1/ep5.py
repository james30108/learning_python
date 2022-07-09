# โปรแกรมแลกเงิน

"""
2000 -> 1000 2 ใบ
1500 -> 1000 1 ใบ, 500 1 ใบ
"""
number = int(input("ป้อนจำนวนเงิน : "))

if number >= 1000 :
    print("1000 บาท = ", number//1000, " ใบ" )
    number %= 1000 # หาจำนวนที่เหลือ
if number >= 500 :
    print("500 บาท = ", number//500, " ใบ" )
    number %= 500 # หาจำนวนที่เหลือ
if number >= 100 :
    print("100 บาท = ", number//100, " ใบ" )
    number %= 100 # หาจำนวนที่เหลือ
if number >= 50 :
    print("50 บาท = ", number//50, " ใบ" )
    number %= 50 # หาจำนวนที่เหลือ
if number >= 20 :
    print("20 บาท = ", number//20, " ใบ" )
    number %= 20 # หาจำนวนที่เหลือ

