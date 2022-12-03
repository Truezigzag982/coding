#子类Circle
#from msilib.schema import Class
import turtle as Pen
import shape  # 导入自定义模块
import math

class Circle(shape.Shape):  # 注意加上模块名shape.
    """从父类/基类定义圆（继承父类）"""

    def __init__(self, radius, color="red", x=0, y=0):
        """  子类重写构造方法
        radius:半径
        color:画笔颜色 """
        super().__init__(x, y)  # 调用父类的构造方法
        self.radius = radius  # 添加实例属性：半径
        self.color = color  # 添加实例属性：画笔颜色

    def circumference(self):
        """ 求周长（多态：重写父类同名方法）"""
        return 2 * math.pi * self.radius

    def area(self):
        """ 求面积（多态：重写父类同名方法）"""
        return math.pi * (self.radius**2)

class rectangle(shape.Shape):
    def __init__(self, length, width, color='red', fillcolor = 'yellow', x=0, y=0):
        super().__init__(x, y)
        self.length = length
        self.width = width
        self.color = color
        self.fillcolor = fillcolor

    def circumference2(self):
        return 2 * (self.length + self.width)

    def area2(self):
        return  self.length * self.width

    def draw(self):
        Pen.pencolor(self.color)
        Pen.fillcolor(self.fillcolor)
        Pen.penup()
        Pen.begin_fill()
        #Pen.goto(self.x, self.y)
        Pen.pendown()
        Pen.begin_fill()
        Pen.forward(self.length)
        Pen.right(90)
        Pen.forward(self.width)
        Pen.right(90)
        Pen.forward(self.length)
        Pen.right(90)
        Pen.forward(self.width)
        Pen.end_fill()


# 默认color="red", x=0, y=0，可不写
c1 = Circle(10)
area = round(c1.area())  # 四舍五入到个位
print(f'半径为{c1.radius}厘米的圆，', '其面积为{area}平方厘米。')
c2 = Circle(4, x=-100, y=100)
# 四舍五入到小数点后2位
circumference = round(c2.circumference(), 2)
print(f'半径为{c2.radius}厘米的圆，', '其周长为{circumference}厘米。')

r1 = rectangle(10, 20)
print(f'长为{r1.length}厘米和宽为{r1.width}厘米的长方形，', '其面积为{area2}平方厘米。')
r2 = rectangle(4, 8, x=-100, y=100)
# 四舍五入到小数点后2位
circumference = round(c2.circumference(), 2)
print(f'长为{r2.length}厘米和宽为{r2.width}厘米的长方形，', '其周长为{circumference2}厘米。')

r1 = rectangle(300, 50)
r1.draw()
Pen.hideturtle()
Pen.done()