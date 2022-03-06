#短吻鳄（拉丁学名Osteolaemus tetraspis Cope），吻鳄是肉食类动物，栖息在宽广的水域，如湖泊、沼泽和大河的周围。其英文名alligator源自西班牙语el lagarto（意思：蜥蜴）。这名称是早期在佛罗里达州的西班牙探险家和定居者命名的。
#长颈鹿（学名：Giraffe camelopardalis [23]  ）：是一种生长在非洲的反刍偶蹄动物，拉丁文名字的意思是“长着豹纹的骆驼”。它们是世界上现存最高的陆生动物。站立时由头至脚可达6-8米，体重约700千克。
#鹿科（Cervidae）是哺乳纲偶蹄目的一科动物。体型大小不等，为有角的反刍类，分布于欧亚大陆、日本、菲律宾、印度尼西亚、北美洲、南美洲的南纬 40°以北地区及西南非洲，全世界约有34种，共16属约52种。
#美洲豹，学名：Panthera onca (Linnaeus, 1758)，又叫美洲虎，是现存第三大的猫科动物。体重35—150千克，最大亚种雄性亚马孙美洲豹平均体重为98千克，咬力可达1250磅。是生活在中南美洲的一种大型猫科动物。'
#西伯利亚虎（学名：Panthera tigris ssp.altaica）：又称东北虎，是虎的亚种之一。是现存体重最大的肉食性猫科动物，成年雄性西伯利亚虎体重平均为250千克，头体长约为2.3米。'

'''
dict_aminals = {
    "aligator": "短吻鳄🐊",
    "girraffe": "长颈鹿🦒",
    "deer": "鹿🦌",
    "jaguar": "美洲豹🐆"
}
sorted_key = sorted(dict_aminals)
print('sorted keys: ', sorted_key)

d_ascending = {}
for k in sorted_key:
    d_ascending[k] = dict_aminals[k]
print("ascending dict: ", d_ascending)

sorted_key = sorted(dict_aminals, reverse=True)
print('sorted keys: ', sorted_key)
d_descending = {k: dict_aminals[k] for k in sorted_key}
print('descending dict: ', d_descending)

animal = input('Please type animal name to search: ')
if animal in dict_aminals:
    print(f'{animal}:{dict_aminals[animal]}')
else:
    print(f'sorry, {animal} is not found in the dictionary.:(')
'''

aligator_dict = {
    '中文名称': '短吻鳄🐊',
    '简介': '短吻鳄（拉丁学名Osteolaemus tetraspis Cope），吻鳄是肉食类动物，'
    '栖息在宽广的水域，如湖泊、沼泽和大河的周围。源自西班牙语el lagarto（意思：蜥蜴）。这名称是早期在佛罗里达州的西班牙探险家和定居者命名的。',
}

dict_aminal = {'aligator': aligator_dict}

girraffe_dict = {
     '中文名称': '长颈鹿🦒',
        '简介': '长颈鹿（学名：Giraffe camelopardalis）：是一种生长在非洲的反刍偶蹄动物，拉丁文名字的意思是“长着豹纹的骆驼”。'
   '它们是世界上现存最高的陆生动物。站立时由头至脚可达6-8米，体重约700千克。',
}
dict_aminal['girraffe'] = girraffe_dict

deer_dict = {
     '中文名称': '鹿🦌',
    '简介': '鹿科（Cervidae）是哺乳纲偶蹄目的一科动物。体型大小不等，为有角的反刍类，'
    '分布于欧亚大陆、日本、菲律宾、印度尼西亚、北美洲、南美洲的南纬 40°以北地区及西南非洲，全世界约有34种，共16属约52种。'
}

dict_aminal['deer'] = deer_dict

jaguar_dict = {
     '中文名称': '美洲豹🐆',
    '简介': '美洲豹，学名：Panthera onca (Linnaeus, 1758)，又叫美洲虎，是现存第三大的猫科动物。'
    '体重35—150千克，最大亚种雄性亚马孙美洲豹平均体重为98千克，咬力可达1250磅。是生活在中南美洲的一种大型猫科动物。',
}

dict_aminal['jaguar'] = jaguar_dict

tiger_dict = {
     '中文名称': '东北虎🐅',
    '简介': '西伯利亚虎（学名：Panthera tigris ssp.altaica）：又称东北虎，是虎的亚种之一。'
    '是现存体重最大的肉食性猫科动物，成年雄性西伯利亚虎体重平均为250千克，头体长约为2.3米。',
}

dict_aminal['tiger'] = tiger_dict


sorted_key = sorted(dict_aminal)

d_ascending = {}
for k in sorted_key:
    d_ascending[k] = dict_aminal[k]

for key, value in d_ascending.items():
    print('\n' + key)
    print(value)
animal = input('Please type animal name to search: ')
if animal in dict_aminal:
    print(f'{animal}:{dict_aminal[animal]}')
else:
    print(f'sorry, {animal} is not found in the dictionary.:(')
