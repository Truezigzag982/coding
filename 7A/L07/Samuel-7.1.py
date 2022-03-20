import csv

def main():
    filename = '个人记账本.csv'
    try:
        with open(filename, 'r', encoding='utf-8-sig') as fr:
            reader = csv.reader(fr)
            print('reader: ', reader)
            header = next(reader)
            records_dict = {}
            records_list = []
            print('header: ', header)
            for row in reader:
                print('row: ', row)
                for key, value in zip(header, row):
                    records_dict[key] = value
                print('records_dict: ', records_dict)
                records_list.append(records_dict)
            print('records_list: ', records_list)
    except FileNotFoundError:
        print(f"{filename}文件不存在！ ):")
    
if __name__ == '__main__':
    main()