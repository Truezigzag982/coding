# 宠物类：添加品种breed、年龄age和性别sex
# 添加实例属性image,以便后续显示宠物图片
class Pet(object):
    count = 0  # 类的属性，记录宠物的数量

    # 构造函数
    def __init__(self, name, color, breed, age, sex,
                 image='pet.png', preowner='查不到前主人'):
        self.name = name
        self.color = color
        self.breed = breed  # 品种
        self.age = age
        self.sex = sex
        self.image = image
        self.__preowner = preowner
        Pet.count += 1  # 宠物数量增加1

    # 添加breed和age信息：输出宠物的信息
    def __str__(self):
        msg = '名称:{}, 颜色: {},品种:{}, 年龄：{}, 性别：{}'.format(
            self.name, self.color, self.breed, self.age, self.sex)
        return msg

    # 喂食
    def eat(self):
        pass  # 之后可由子类重写, 需要吃的东西

    # 修改前主人信息
    def set_preowner(self, preowner):
        self.__preowner = preowner

    # 获取前主人信息
    def get_preowner(self):
        return self.__preowner


def main():
    pet1 = Pet('红眼波斯猫哥', 'white', '波斯猫', '2-3岁', 'male')
    pet1.age = '1-2岁'  # 修改对象的属性值
    print(pet1)  # 调用的是父类__str__(self)方法

    # 使用构造函数创建另一个对象
    pet2 = Pet('SMART一号', 'white and black', '边境牧养犬', '1-2岁', 'female')
    print(pet2.breed)
    print("现有宠物数量:", Pet.count)  # Pet是类的对象
    print(pet2.get_preowner())


if __name__ == '__main__':
    main()
