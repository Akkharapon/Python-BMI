import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # แปลงจาก cm เป็น m
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2) #

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


        # เพิ่มการเขียน log
        write_log(weight, height * 100, bmi, status)

    except ValueError:  # ถ้าทำงานไม่ถูกต้อง ให้แสดงข้อความ
        messagebox.showerror("Error", "กรุณากรอกข้อมูลให้ถูกต้อง (ตัวเลขเท่านั้น)")


def write_log(weight, height, bmi, status):
    log_dir = "log"
    os.makedirs(log_dir, exist_ok=True)  # สร้างโฟลเดอร์ log ถ้ายังไม่มี

    log_path = os.path.join(log_dir, "bmi_log.txt")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{now}] น้ำหนัก: {weight} kg, ส่วนสูง: {height} cm, BMI: {bmi}, สถานะ: {status}\n"

    with open(log_path, "a", encoding="utf-8") as file:
        file.write(log_message)

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

v_version = "1.1.1"  # เพิ่มเวอร์ชันของโปรแกรม
label_version = tk.Label(window, text=f"เวอร์ชัน: {v_version}", font=("Arial", 6), fg="gray")
label_version.pack(side="bottom",pady=5)

# เริ่มต้น GUI
window.mainloop()
