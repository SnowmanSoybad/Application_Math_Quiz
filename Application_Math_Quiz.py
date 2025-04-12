import tkinter as tk
import random

operator = ["+", "-", "*"]
minnum = 1
maxnum = 12

app = tk.Tk()
app.title("Application_Math_Quiz")
app.geometry("250x180")

question_label = tk.Label(app)
question_label.pack()

entry = tk.Entry(app)
entry.pack()

result_label = tk.Label(app)
result_label.pack()

def generate_question():
    global answer
    x1 = random.randint(minnum, maxnum)
    x2 = random.randint(minnum, maxnum)
    x3 = random.choice(operator)
    expression = f"{x1} {x3} {x2}"
    answer = eval(expression)
    question_label.config(text=f"จงหาคำตอบ: {expression}")
    entry.delete(0, tk.END)  
    result_label.config(text="")  

def check_answer():
    user_answer = entry.get()
    try:
        number = int(user_answer)
        if number == answer:
            result_label.config(text="ถูกต้อง! 🎉")
            generate_question() 
        else:
            result_label.config(text="ผิด ลองอีกครั้ง 😢")
    except ValueError:
        result_label.config(text="กรุณากรอกตัวเลขจำนวนเต็มนะครับ.")

submit_button = tk.Button(app, text="ตรวจคำตอบ", command=check_answer)
submit_button.pack()

generate_question()

app.mainloop()
