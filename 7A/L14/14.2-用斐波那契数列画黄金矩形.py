#导入模块
import turtle
import time



#非递归法：生成斐波那契数列
def fib(n):
    print(n)
    if n in (1, 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)


"""
    a1 = 1
    a2 = 1
    fib_list = []
    for i in range(0, n):
        #数列添加数值
        fib_list.append(a1)
        a1, a2 = a2, a1 + a2
    print(fib_list)
    return fib_list
    """

# 画出斐波那契图形（长方形+曲线）
def draw_fib(t, n, show_number=False):
    colors = ("cyan", "green", "blue", "orange", "black", "purple")
    # turtle画图
    t.penup()
    t.goto(100, -150)
    t.pendown()
    fib_list = []
    for i in range(0, n):
        fib_list.append(fib(i+1))
    for i in range(0, n):
        t.color(colors[i % 6])
        t.fillcolor(colors[(i + 1) % 6])
        # 画填充正方形
        t.begin_fill()
        for n in range(4):
            t.forward(fib_list[i] * 40) # 适当放大，在数值较小时画图能看清
            t.left(90)
        t.end_fill()
        time.sleep(1)
        # 画圆弧(1/4圆)
        t.color('red')
        t.circle(fib_list[i] * 40, 90)  # 适当放大相同倍数
        time.sleep(1)

        # 输出数列数值
        if show_number:
            t.penup()
            t.forward(-fib_list[i] * 4)  # 避免写出来的字被后续填充掉了
            t.pendown()
            t.color(colors[i % 6])
            t.write(fib_list[i], font=("微软雅黑", 10 + i * 2))
            t.forward(fib_list[i] * 4)
    t.penup()


def main():
    turtle.setup(1300, 800)
    t = turtle.Pen()
    t.speed(5)
    t.pensize(2)
    t.setheading(0)
    #输入自定义数列的个数
    n = int(turtle.numinput("输入数字", "请输入斐波那契数列的个数：", 
                            7, 4, 14))  # default, min, max
    draw_fib(t, n, True)
    turtle.done()



if __name__ == '__main__':
    main()
