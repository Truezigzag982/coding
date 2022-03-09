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
    fr = open(filename, 'r', encoding='utf-8')
    data = fr.read()
    dict_data=eval(data)
    print(data)
    print("type of data:", type(data))
    print("type of dict data:", type(dict_data))
    return dict_data

def main():
    filename = 'animals_data.txt'
    save_data(filename, dict_animals)
    animals_data = read_data(filename)
    for key, value in animals_data.items():
        print(f'{key}: {value}')
    
if __name__ == "__main__":
    main()