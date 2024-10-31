# 命令行方式
from random import randint, sample

def generate_dlt_ticket():
    red_balls = [x for x in range(1, 36)]
    selected_red_balls = sample(red_balls, 5)
    selected_red_balls.sort()

    blue_balls = [x for x in range(1, 13)]
    selected_blue_balls = sample(blue_balls, 2)
    selected_blue_balls.sort()

    print("红色球: ", ' '.join(f"{num:02d}" for num in selected_red_balls), end=' | ')
    print("蓝色球: ", ' '.join(f"{num:02d}" for num in selected_blue_balls))

def generate_ssq_ticket():
    red_balls = [x for x in range(1, 34)]
    selected_red_balls = sample(red_balls, 6)
    selected_red_balls.sort()

    blue_ball = randint(1, 16)

    print("红色球: ", ' '.join(f"{num:02d}" for num in selected_red_balls), end=' | ')
    print("蓝色球: ", f"{blue_ball:02d}")

def main():
    while True:
        lottery_type = input("请选择彩票类型（输入 'dlt' 为大乐透，'ssq' 为双色球）：").strip().lower()
        if lottery_type not in ['dlt', 'ssq']:
            print("无效的彩票类型，请输入 'dlt' 或 'ssq'")
            continue

        while True:
            try:
                n = int(input("请输入要生成的注数："))
                if n <= 0:
                    print("请输入大于 0 的整数！")
                    continue
                break
            except ValueError:
                print("无效输入，请输入一个整数！")

        if lottery_type == 'dlt':
            print("\n生成的大乐透号码：")
            for _ in range(n):
                generate_dlt_ticket()
        elif lottery_type == 'ssq':
            print("\n生成的双色球号码：")
            for _ in range(n):
                generate_ssq_ticket()

        retry = input("\n是否继续？(输入 'y' 继续，其他键退出)：").strip().lower()
        if retry != 'y':
            print("程序结束！")
            break

if __name__ == "__main__":
    main()
