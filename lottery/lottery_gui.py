# 好看的界面
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from random import randint, sample

# 生成大乐透号码
def generate_dlt_ticket():
    red_balls = [x for x in range(1, 36)]
    selected_red_balls = sample(red_balls, 5)
    selected_red_balls.sort()

    blue_balls = [x for x in range(1, 13)]
    selected_blue_balls = sample(blue_balls, 2)
    selected_blue_balls.sort()

    return f"红色球: {' '.join(f'{num:02d}' for num in selected_red_balls)} | 蓝色球: {' '.join(f'{num:02d}' for num in selected_blue_balls)}"

# 生成双色球号码
def generate_ssq_ticket():
    red_balls = [x for x in range(1, 34)]
    selected_red_balls = sample(red_balls, 6)
    selected_red_balls.sort()

    blue_ball = randint(1, 16)

    return f"红色球: {' '.join(f'{num:02d}' for num in selected_red_balls)} | 蓝色球: {blue_ball:02d}"

# 生成排列3号码
def generate_arrangement_3_ticket():
    digits = [str(x) for x in range(10)]  # 0-9
    selected_digits = sample(digits, 3)  # 选3个数字
    return " | ".join(selected_digits)

# 生成排列5号码
def generate_arrangement_5_ticket():
    digits = [str(x) for x in range(10)]  # 0-9
    selected_digits = sample(digits, 5)  # 选5个数字
    return " | ".join(selected_digits)

# 生成号码的主函数
def generate_tickets():
    try:
        n = int(entry_number.get())
        if n <= 0:
            raise ValueError("注数必须为正整数")
    except ValueError:
        messagebox.showerror("输入错误", "请输入一个有效的注数")
        return

    lottery_type = lottery_type_var.get()
    result_text.delete(1.0, tk.END)  # 清空之前的内容

    # 根据选择的类型生成号码
    if lottery_type == "大乐透":
        for _ in range(n):
            result_text.insert(tk.END, generate_dlt_ticket() + "\n")
    elif lottery_type == "双色球":
        for _ in range(n):
            result_text.insert(tk.END, generate_ssq_ticket() + "\n")
    elif lottery_type == "排列3":
        for _ in range(n):
            result_text.insert(tk.END, generate_arrangement_3_ticket() + "\n")
    elif lottery_type == "排列5":
        for _ in range(n):
            result_text.insert(tk.END, generate_arrangement_5_ticket() + "\n")

# 初始化界面
root = tk.Tk()
root.title("彩票号码生成器")
style = ttk.Style()
style.theme_use('clam')  # 选择主题

# 选择彩票类型
tk.Label(root, text="请选择彩票类型：", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
lottery_type_var = tk.StringVar(value="大乐透")
lottery_type_menu = ttk.Combobox(root, textvariable=lottery_type_var, values=["大乐透", "双色球", "排列3", "排列5"], state="readonly")
lottery_type_menu.grid(row=0, column=1, padx=10, pady=10)

# 输入注数
tk.Label(root, text="请输入生成注数：", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
entry_number = tk.Entry(root, font=("Arial", 12))
entry_number.grid(row=1, column=1, padx=10, pady=10)

# 生成按钮
generate_button = ttk.Button(root, text="生成号码", command=generate_tickets)
generate_button.grid(row=2, column=0, columnspan=2, pady=20)

# 显示结果
result_text = tk.Text(root, height=20, width=70, font=("Arial", 12))
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

# 设置权重以使文本框在窗口调整时能放大
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# 运行界面
root.mainloop()
