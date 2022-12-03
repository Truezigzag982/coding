# 宠物类：添加品种breed、年龄age和性别sex
# 添加实例方法eat，之后可由子类重写
class Pet(object):
    count = 0  # 类的属性，记录宠物的数量

    # 构造函数
    def __init__(self, name, color, breed, age, sex):
        self.name = name
        self.color = color
        Pet.count += 1  # 宠物数量增加1

        self.breed = breed  # 品种
        self.age = age
        self.sex = sex

    # 添加breed和age信息：输出宠物的信息
    def __str__(self):
        msg = 'name:{}, color: {},breed:{}, years:{}, sex:{}'.format(
            self.name, self.color, self.breed, self.age, self.sex)
        return msg

    # 喂食
    def eat(self):
        pass  # 之后可由子类重写, 需要吃的东西


def main():
    pet1 = Pet('snowball', 'white', 'british shorthair ', '2-3years', 'male')
    pet1.age = '1-2years'  # 修改对象的属性值
    print(pet1)  # 调用的是父类__str__(self)方法

    # 使用构造函数创建另一个对象
    pet2 = Pet('fluffy', 'white', 'pomeranian', '1-2years', 'female')
    print(pet2)
    print(pet2.breed)
    print("现有宠物数量:", Pet.count)  # Pet是类的对象


if __name__ == '__main__':
    main()
