dict_diary1 = {
    '当前日期': '12/3/2022',
    '天气': '多云',
    '感恩主题': '时间',
    '感恩内容': '今天上课我没有迟到。'
}


def init_header(filename, dict_data):
    header = ""
    for key in dict_data:
        header += '%-12s\t' % (key)
    with open(filename, 'w', encoding='utf8') as fw:
        fw.write(header)


def append_diary(filename, dict_diary):
    diary = "\n"
    for value in dict_diary.values():
        diary += '%-12s\t' % (value)
    print('dairy to append: ' + diary)
    try:
        with open(filename, 'a', encoding='utf-8') as fw:
            fw.write(diary)
    except FileNotFoundError:
        print(f'文件{filename}不存在! :(')


def read_dairy(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as fr:
            header = fr.readline()
            print('标题行', header)
            keys = header.split()
            print('keys', keys)
            dairy_dict = {}
            dairy_list = []
            lines = fr.readlines()
            for line in lines:
                values = line.split()
                print('vlaues', values)
                for key, value in zip(keys, values):
                    dairy_dict[key] = value
                print('diary_dict', dairy_dict)
                dairy_list.append(dairy_dict)
            print('diary_list', dairy_list)
            return dairy_list
    except FileNotFoundError:
        print(f'文件{filename}不存在! :(')
        return None


def main():
    filename = 'thanksgiving_diary.txt'
    date = input('当前日期（格式为2028-03-14）:)  ')
    wether = input('天气： ')
    topic = input('感恩主题: ')
    content = input('感恩内容: ')
    dict_diary_new = {
        '当前日期': date,
        '天气': wether,
        '感恩主题': topic,
        '感恩内容': content
    }
    append_diary(filename, dict_diary_new)
    read_dairy(filename)


if __name__ == '__main__':
    main()
