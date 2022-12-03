# 添加实例属性image,以便后续显示宠物图片
from pet4 import Pet
from cat4 import Cat


# 类的继承：子类(父类)
class Dog(Pet):
    dog_count = 0  # 类的属性，狗狗计数

    def __init__(self, name, color, breed, age, sex, image='pet.png'):
        super().__init__(name, color, breed, age, sex, image)
        Dog.dog_count += 1  # 狗的计数增加
        #self.preowner = '查不到前主人'

    # 重写与父类（基类）同名的方法（多态）
    def eat(self):
        food = 'bone'
        print(f'{self.name}要吃{food}。')

    # 吠叫
    def bark(self):
        print(self.name + ' is barking.')
'''
    # 修改前主人信息
    def set_preowner(self, owner):
        self.preowner = owner

    # 获取前主人信息
    def get_preowner(self):
        return self.preowner    
    
    def change_owner(self, owner):
        print('change owner in Dog')
        #self.__preowner = owner
'''
def modify_pet(pet):
    pet.name = 'changed.'
    
# 测试
def main():
    dog1 = Dog('Harley', 'brown and black', '柯基犬', '2岁', 'male')
    print(dog1.preowner)
    
    dog2 = Dog('Bella', 'black', '牧羊犬', '1岁', 'female')
    
    cat1 = Cat('红眼大王', '黑白', '波斯猫', '3-6个月', 'female')
    
    pets_list = [dog1, dog2, cat1]
    
    pet3 = pets_list[2] # cat1 #指向同一个对象
    '''
    pet3.set_preowner('new cat1 owner.') # 也会修改cat1的属性
    print(f'{dog1.name}的前主人是：{dog1.get_preowner()}')
    dog1.set_preowner('Lovely Owner')
    print(f'{dog1.name}的前主人是：{dog1.get_preowner()}')

    for pet in pets_list:
        modify_pet(pet)
        pet.set_preowner('owner found.')

    for pet in pets_list:
        print(pet.name) # 经测试，以上调用函数修改的其实是pets_list中对象的属性
        print('owner:', pet.get_preowner())
    '''        
    
    print(f'现有{Dog.dog_count}条狗。')
    print(f'现有{Cat.cat_count}只猫。')
    print("共有%d只宠物可供领养。" % (Pet.count))


if __name__ == '__main__':
    main()
