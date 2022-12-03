class Pet(object):
    """
    定义父类/基类：宠物类
    Attributes:
        count:记录宠物的数量
    """
    count = 0  # 类的属性，记录宠物的数量

    # 类变量，它的值将在这个类的所有实例之间共享

    # 构造函数/方法，在创建实例/对象时会调用
    def __init__(self, name, color):
        self.name = name  # 实例属性
        self.color = color  # 实例属性
        Pet.count += 1  # 宠物计数增加1

    # 在类的外面使用print(实例对象)输出的内容
    def __str__(self):
        # return '宠物名:' + self.name + ', 颜色: ' + self.color
        return f'宠物名:{self.name}, 颜色: {self.color}.'


# 定义主函数，进行测试
def main():
    # 创建实例对象
    pet1 = Pet('红眼波斯猫哥', '白色')  # 使用构造函数创建一个对象pet1(实例)
    print(pet1)  # 实际调用的是__str__(self)方法
    print("Pet.count:", Pet.count)  # Pet是类的对象

    # 使用构造函数创建另一个对象
    pet2 = Pet('边牧一号', '黑白')
    print("Pet.count:", Pet.count)

    print(pet2)
    pet2.color = '灰白'  # 修改对象的属性值
    print(pet2)


if __name__ == '__main__':  # 当模块被别的程序导入时， 主程序不会被执行
    main()
