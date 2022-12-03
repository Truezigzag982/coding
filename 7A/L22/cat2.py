# 导入需要使用的类 # from pet3 import Pet
# 类的封装：私有属性和私有方法
import pet3


class Cat(pet3.Pet):  # class Cat(Pet):
    cat_count = 0  # 类的属性，猫猫计数

    # 添加私有属性：preowner(前主人)
    def __init__(self, name, color, breed, age, sex):
        super().__init__(name, color, breed, age, sex)
        self.__preowner = '查不到前主人'
        Cat.cat_count += 1  # 猫的计数增加

    # 重写与父类（基类）同名的方法（多态）``
    def eat(self):
        food = 'fish'
        print(f'{self.name}要吃{food}。')

    # 猫叫
    def meow(self):
        print(f'{self.name}在喵喵叫。')

    # 修改前主人信息
    def set_preowner(self, preowner):
        self.__preowner = preowner

    # 获取前主人信息
    def get_preowner(self):
        return self.__preowner


# 定义主函数，进行测试
def main():
    cat1 = Cat('红眼大王', '黑白', '波斯猫', '3-6个月', 'female')
    print('前主人是：', cat1.get_preowner())
    cat1.set_preowner('A区陈小虎同学')
    print(cat1)
    print('前主人是：', cat1.get_preowner())

    print('前主人是：', cat1.preowner)  # 不能访问私有变量！
    # print('前主人是：', cat1.__preowner)  # 不能访问私有变量！

    # cat1.__preowner = '实例对象的属性：主人'  # 实际是可以修改的，是Python的Bug!


if __name__ == '__main__':
    main()
