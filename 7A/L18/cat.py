# 导入需要使用的类 # from pet3 import Pet
import pet3


class Cat(pet3.Pet):  # class Cat(Pet):
    cat_count = 0  # 类的属性，猫猫计数

    def __init__(self, name, color, breed, age, sex):
        super().__init__(name, color, breed, age, sex)
        Cat.cat_count += 1  # 猫的计数增加

    # 重写与父类（基类）同名的方法（多态）
    def eat(self):
        food = 'fish'
        print(f'{self.name} wantes to eat {food}')

    # 猫叫
    def meow(self):
        print(f'{self.name}is purring.')

    # 练习：请添加定义并调用 爬树 climb
    def climb(self):
        print(f'oh no! {self.name} is climbing a tree.')


# 定义主函数，进行测试
def main():
    cat1 = Cat('Hayden', 'white', 'british shorthair', '3-6month', 'female')
    print(cat1)
    cat1.eat()

    cat2 = Cat('Hesiod', 'gray, and white', 'amercian shorthair', '3-6years', 'male')
    print(cat2)
    cat2.meow()
    cat2.climb()
    print('cats number:', Cat.cat_count)


if __name__ == '__main__':
    main()
