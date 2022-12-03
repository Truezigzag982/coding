# 对象的存储与读取（序列化与反序列化）
import pickle
from cat4 import Cat
from dog4 import Dog
import os

# 保存对象列表
def write_object(filename, object_list):
    result = False
    with open(filename, 'wb') as file:
        pickle.dump(object_list, file)  # 序列化(保存对象)
        result = True
    return result


# 读取对象列表
def read_object(filename):
    with open(filename, 'rb') as file:
        object_list = pickle.load(file)  # 反序列化（读取对象）
    return object_list


def main():
    current_work_dir = os.path.dirname(__file__) # 获取当前文件所在目录
    filename = current_work_dir + "\\pets_info.data"  # 用于存储序列化的对象
    print(filename)
    dog1 = Dog('Harley', '棕黄', '柯基犬', '2岁', 'male')
    dog2 = Dog('Bella', '黑白', '牧羊犬', '1岁', 'female')
    cat1 = Cat('红眼大王', '黑白', '波斯猫', '3-6个月', 'female')
    cat2 = Cat('逗逗', '黄白', '加菲猫', '3-6岁', 'male')
    object_list = [dog1, dog2, cat1]
    object_list.append(cat2)

    for pet in object_list:
        if pet.name == 'Bella':
            pet = cat2  # 这种方式不会修改object_list[1]对应的dog2!
            pet.name = 'Newnew'
    print('new pet:', object_list[1])

    # 把对象列表序列化（保存）到数据文件
    if write_object(filename, object_list):
        print('对象列表序列化到文件成功。')
    else:
        print('对象列表序列化到文件失败！')

    # 从数据文件反序列化（读取）对象列表
    object_list2 = read_object(filename)
    if object_list2 is not None:
        for object in object_list2:  # 从对象列表中依次读取出对象
            print(object)
            if isinstance(object, Cat):  # 判断对象是否是指定类型的实例
                object.meow()
            elif isinstance(object, Dog):
                object.bark()
    else:
        print('对象列表反序列化失败！')


if __name__ == '__main__':
    main()
