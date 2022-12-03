# 导入需要使用的类
import pets.pet  # 添加包名


# 类的继承：子类(父类)
class Cat(pets.pet.Pet):  # 添加包名
    cat_count = 0  # 类的属性，猫猫计数

    # 构造方法（构造函数），创建对象时会调用
    def __init__(self, name, color, breed):
        super().__init__(name, color)
        Cat.cat_count += 1
        self.breed = breed

    # 打印信息， 重写与父类（基类）同名的方法（多态）
    def print_info(self):
        print("猫的品种：", self.breed)
        super().print_info()  # 调用父类定义的方法

    # 猫叫
    def meow(self):
        print(self.name + ' is meowing.')

    # 练习：请添加定义并调用
    # 爬树 climb


# 定义主函数，进行测试
def main():
    cat1 = Cat('红眼大王', 'white', '波斯猫')  # 使用构造函数创建一个对象实例
    cat1.print_info()  # 调用对象的方法
    print(cat1)  # 调用的是__str__(self)方法
    cat2 = Cat('豆豆', 'yellow and brown', '加菲猫')  # 使用构造函数创建一个对象实例
    print(cat2)  # 调用的是__str__(self)方法
    print('cats number:', Cat.cat_count)


if __name__ == '__main__':  # 当模块被别的程序导入时， 主程序不会被执行
    main()
