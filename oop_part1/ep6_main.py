"""
การสร้าง CLass แบบแยกไฟล์
"""

# ดึงไฟล์ที่เป็น class ที่ใช้งานเข้ามาทำงาน
from ep6_2 import Programer
from ep6_3 import Sale


programer_1 = Programer ("เจมส์", 15000, 2, "พัฒนาเว็บ")
sale_1      = Sale ("ป่าน", 18000, "เชียงใหม่")

programer_1._display()
sale_1._display()