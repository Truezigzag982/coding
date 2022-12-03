class Pet(object):
    """定义父类：宠物类
    Attributes:
        count:记录宠物的数量
    """
    # 类变量，它的值将在这个类的所有实例之间共享
    count = 0  # 类的属性，记录猫狗的总数量

    # 构造函数/方法，在创建实例/对象时会调用
    def __init__(self, name, color, breed, age, sex):
        self.name = name  # 实例属性
        self.color = color  # 实例属性
        self.breed = breed  # 实例属性
        self.age = age  # 实例属性
        self.sex = sex  # 实例属性
        Pet.count += 1  # 宠物计数增加1

    # print实例对象时，输出宠物的信息
    def __str__(self):
        return f'pet name:{self.name}, color: {self.color}, breed: {self.breed}, age: {self.age}, sex: {self.sex}.'


# 定义主函数，进行测试
def main():
    pet1 = Pet('snowball', 'white', 'british shorthair ', '0-2month', 'male')  # 创建实例对象
    print(pet1)  # 实际调用的是__str__(self)方法
    print("现有宠物数量:", Pet.count)  # Pet是类的对象

    pet2 = Pet('fluffy', 'whith', 'pomeranian', '1-2years', 'female')
    print(pet2)
    print("现有宠物数量:", Pet.count)

    #pet2.color = '灰白'  # 修改对象的属性值
    #pet2.name = 'SMART一号'  # 修改对象的属性值
    #print(pet2)


if __name__ == '__main__':
    main()
