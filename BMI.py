import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # แปลงจาก cm เป็น m
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            status = "ผอม"
        elif 18.5 <= bmi < 23:
            status = "น้ำหนักปกติ"
        elif 23 <= bmi < 25:
            status = "น้ำหนักเกิน"
        elif 25 <= bmi < 30:
            status = "อ้วนระดับ 1"
        else:
            status = "อ้วนระดับ 2"

        result_text = f"BMI: {bmi}\nสถานะ: {status}"
        label_result.config(text=result_text)

    except ValueError:  # ถ้าทำงานไม่ถูกต้อง ให้แสดงข้อความ
        messagebox.showerror("Error", "กรุณากรอกข้อมูลให้ถูกต้อง (ตัวเลขเท่านั้น)")

# สร้างหน้าต่าง
window = tk.Tk()
window.title("โปรแกรมคำนวณ BMI")
window.geometry("300x250")

# ป้ายข้อความ
label_weight = tk.Label(window, text="น้ำหนัก (kg):")
label_weight.pack(pady=5)
entry_weight = tk.Entry(window)
entry_weight.pack()

label_height = tk.Label(window, text="ส่วนสูง (cm):")
label_height.pack(pady=5)
entry_height = tk.Entry(window)
entry_height.pack()

# ปุ่มคำนวณ
button_calc = tk.Button(window, text="คำนวณ BMI", command=calculate_bmi)
button_calc.pack(pady=10)

# แสดงผลลัพธ์
label_result = tk.Label(window, text="", font=("Arial", 12))
label_result.pack(pady=10)

# เริ่มต้น GUI
window.mainloop()
