'''
字典操作
'''
puppy = dict(宠物='博美', 年龄='3个月', 体重='0.5kg')
print(puppy)
print(puppy['宠物'])
print(puppy['年龄'])
print(puppy['体重'])

puppy['颜色'] = '白色' 
print(puppy)
puppy['体重'] = '0.6kg'
print(puppy)
del puppy['年龄']
print(puppy)
del puppy['宠物']
del puppy['体重']
del puppy['颜色']
print(puppy)
del puppy
