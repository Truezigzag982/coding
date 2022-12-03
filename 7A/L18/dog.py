# 导入需要使用的类 # from pet3 import Pet
import pet3


class Dog(pet3.Pet):  # class Cat(Pet):
    dog_count = 0  # 类的属性，猫猫计数

    def __init__(self, name, color, breed, age, sex):
        super().__init__(name, color, breed, age, sex)
        Dog.dog_count += 1  # 狗的计数增加🐶

    # 重写与父类（基类）同名的方法（多态）
    def eat(self):
        food = 'hotdog'
        print(f'{self.name} wantes to eat {food}.')

    # 猫叫
    def bark(self):
        print(f'{self.name} is bakring.')

    # 练习：请添加定义并调用 爬树 climb
    '''def climb(self):
        print(f'oh no! {self.name} is climbing a tree.')'''


# 定义主函数，进行测试
def main():
    dog1 = Dog('Lina', 'gold', 'golden retriever', '5-7month', 'female')
    print(dog1)
    dog1.eat()

    dog2 = Dog('Teboho', 'white',  'pomeranian', '4-5years', 'male')
    print(dog2)
    dog2.bark()
    print('dogs number:', Dog.dog_count)


if __name__ == '__main__':
    main()
