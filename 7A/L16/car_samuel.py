# 课堂练习2：请按以下注释，修改或补充代码，让程序正常运行

# 请编写父类:
class Car(object):  # 请在括号里填写补充完整
    def __init__(self, make, year):  # 此行缺少什么，请补充完整
        '''
        make = 生产厂家
        year = 生产年份'''
        pass # 请编写程序替代此行, 设置实例属性：make和year

    def get_make(self):  # 请在括号里添加一个参数
        print("生产厂家" + self.make)
        return "生产厂家" + self.make# 请编写程序替代此行，打印出make(生产厂家)

    def get_year(self):  # 请在括号里添加两个个参数
        print ("生产年份" + self.year)
        return "生产年份" + self.year #请编写程序替代此行，打印出生产的年份


# 请编写子类:
class ElectricCar(Car):  # 请在括号里填写父类名称
    def recharge(self): # 充电提醒
        print('电量仅剩余5%，请及时充电！')

# 创建实例对象：
tesla1 = ElectricCar('Tesla', '2018') # 请补充代码
beyond1 = Car('Beyond', 2021)  # 请补充代码，创建实例对象
# 调用实例方法：
print(tesla1.get_make())  # 请补充代码,打印生产厂家
tesla1.recharge()    # 请补充代码, 打印充电提醒
print(beyond1.get_year())    # 请补充代码,打印生产年份
