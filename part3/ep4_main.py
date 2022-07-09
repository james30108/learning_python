# Module (โมดูล) และ Package
# โมดูล คือโปรแกรมย่อย
# ไกล้เคียงกับคำว่า Library ในภาษาอื่นๆ
# Package คือ โฟลเดอร์ต่างๆ (หรือการเข้าถึงโฟลเดอร์)


# --------------------------
# การสร้างโมดูล
# โปรแกรมหลัก
import package.ep4_module # ดึงโมดูลมาใช้งาน (คล้ายๆ include ใน PHP)

# การตั้งชื่อให้กับโมดูล
import package.ep4_module2 as weather 

# from ทำให้สามารถเรียกใช้งานฟังก์ชั่นหรือตัวแปรนั้นได้เลยโดยที่ไม่ต้องกำหนดชื่อโมดูลนำหน้า
from package.ep4_module import subtraction 
from package.ep4_module2 import * # เข้าถึงทุกตัวแปรและทุกฟังก์ชั่นในโมดูลนั้น ๆ


# --------------------------

package.ep4_module.showName ("james") # เรียกใช้งานฟังกืชั่นในโมดูลนั้นๆ
package.ep4_module.addition (5,10) 
subtraction (10, 5)

showWeather = weather.city["เชียงใหม่"]
print (showWeather)

