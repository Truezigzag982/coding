puppy_dict = {
    '宠物':{
        '博美': '博美是一只狗\n' + 
            ':)'},
    '年龄':{ 
        '3个月': 
        '博美三个月了' },
    '体重':{
        '0.5kg': '博美体重是0.5千克'
    }
}


for key in puppy_dict:
    print('/n宠物: ', key)
    puppy = puppy_dict.get(key)
    for title, content in puppy.items():
        print('\n年龄: ', title)
        print('内容: ')
        print(content)
