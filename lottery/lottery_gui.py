import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from random import randint, sample, shuffle

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


# 生成幸运数字（随机在1到10之间）
def generate_lucky_number():
    # 禁用按钮，防止多次点击
    generate_lucky_button.config(state="disabled")

    # 显示转动效果（1到10之间的数字随机显示）
    lucky_number_var.set("转动中...")
    rotate_effect()  # 启动转动效果

    # 使用after模拟延时，过1秒后显示幸运数字
    root.after(1000, display_lucky_number)


# 转动效果函数，1到10的数字乱序变化
def rotate_effect():
    def update_rotate():
        # 生成1到10的数字并随机显示
        lucky_number_var.set(str(randint(1, 10)))  # 随机选择1到10的数字显示
        # 每150ms更新一次数字，创造转动效果
        if rotating_flag[0]:
            root.after(150, update_rotate)

    rotating_flag[0] = True  # 设置旋转标志为True，开始动画
    update_rotate()  # 开始转动效果


# 显示幸运数字
def display_lucky_number():
    lucky_num = randint(1, 10)  # 幸运数字是1到10之间的随机数
    lucky_number_var.set(lucky_num)  # 设置幸运数字的显示值

    # 停止数字旋转
    rotating_flag[0] = False

    # 重新启用按钮
    generate_lucky_button.config(state="normal")


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
root.geometry("600x500")  # 设置窗口大小

style = ttk.Style()
style.theme_use('clam')  # 选择主题

# 选择彩票类型
tk.Label(root, text="请选择彩票类型：", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
lottery_type_var = tk.StringVar(value="大乐透")
lottery_type_menu = ttk.Combobox(root, textvariable=lottery_type_var, values=["大乐透", "双色球", "排列3", "排列5"],
                                 state="readonly", font=("Arial", 12))
lottery_type_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# 输入注数
tk.Label(root, text="请输入生成注数：", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_number = tk.Entry(root, font=("Arial", 12))
entry_number.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# 生成幸运数字按钮
generate_lucky_button = ttk.Button(root, text="生成幸运数字", command=generate_lucky_number, width=20)
generate_lucky_button.grid(row=2, column=0, columnspan=2, pady=10)

# 显示幸运数字
tk.Label(root, text="幸运数字：", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
lucky_number_var = tk.IntVar()
lucky_number_label = tk.Label(root, textvariable=lucky_number_var, font=("Arial", 12))
lucky_number_label.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# 生成号码按钮
generate_button = ttk.Button(root, text="生成号码", command=generate_tickets, width=20)
generate_button.grid(row=4, column=0, columnspan=2, pady=20)

# 显示结果
result_text = tk.Text(root, height=15, width=70, font=("Arial", 12))
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

# 设置权重以使文本框在窗口调整时能放大
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# 存储旋转动画的标志
rotating_flag = [False]

# 运行界面
root.mainloop()
