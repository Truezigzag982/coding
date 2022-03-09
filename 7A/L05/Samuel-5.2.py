dict_animals = {
    "aligator": "短吻鳄",
    "deer": "鹿",
    "giraffe": "长颈鹿",
    "jaguar": "美洲豹"
}

def save_data(filename, data):
    fw = open(filename, 'w', encoding='utf-8')
    fw.write(str(data))
    fw.close()

def read_data(filename):
    try:
        with open(filename,'r', encoding='utf-8') as fr:
            data = fr.read()
            dict_data = eval(data) #
        return dict_data
    except FileNotFoundError:
        print(f"文件{filename}不存在! :(")
        return None

def add_data(filename, key, value):
    dict_data = read_data(filename)
    dict_data[key] = value  
    with open(filename, 'w', encoding='utf-8') as fw:
        fw.write(str(dict_data))

def main():
    filename = 'animals_data.txt'
    key = input('English name: ')
    value = input('中文名称: ')
    add_data(filename, key, value)
    animals_data = read_data(filename)
    for key, value in animals_data.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    main()