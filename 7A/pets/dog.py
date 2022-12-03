# 导入需要使用的类
from pets.pet import Pet  # 需要加包名pets
from pets.cat import Cat  # 需要加包名pets


# 类的继承：子类(父类)
class Dog(Pet):
    dog_count = 0  # 类的属性，狗狗计数

    # 构造方法（构造函数），创建对象时会调用
    def __init__(self, name, color, breed):
        super().__init__(name, color)
        Dog.dog_count += 1
        self.breed = breed  # 品种

    # 打印信息， 重写与父类（基类）同名的方法（多态）
    def print_info(self):
        print("狗的品种：", self.breed)
        super().print_info()  # 调用父类定义的方法

    # 吠叫
    def bark(self):
        print(self.name + ' is barking.')

    # 摇尾巴
    def wag_tail(self):
        print(self.name + ' is wagging its tail.')

    # 练习添加：
    # 坐下
    # sit()

    # 打滚
    # roll_over()


# 测试
def main():
    dog1 = Dog('Harley', 'brown and black', '柯基犬')  # 使用类的构造2函数创建一个对象实例
    dog1.print_info()  # 调用对象的方法
    dog1.bark()

    dog2 = Dog('Bella', 'black', '牧羊犬')  # 使用构造函数创建一个对象实例
    print(dog2)  # 调用的是父类的__str__(self)方法
    dog2.wag_tail()

    cat1 = Cat('Coward', 'yellow and brown', '加菲猫')  # 使用构造函数创建一个对象实例
    print(cat1)  # 调用的是__str__(self)方法
    cat1.meow()

    print(f'{Dog.dog_count} dogs.')
    print(str(Cat.cat_count) + " cats.")
    print("%d pets." % (Pet.count))


if __name__ == '__main__':  # 当模块被别的程序导入时， 主程序不会被执行
    main()
