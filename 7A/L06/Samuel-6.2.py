dict_diary1 = {
    '当前日期': '12/3/2022',
    '天气': '多云',
    '感恩主题': '时间',
    '感恩内容': '今天上课我没有迟到。'
}


def append_dairy(filename, dict_diary):
    dairy = "\n"
    for value in dict_diary.values():
        dairy += '%-12s\t' % (value)
    print('dairy to append: ' + dairy)
    try:
        with open(filename, 'a', encoding='utf-8') as fw:
            fw.write(dairy)
    except FileNotFoundError:
        print(f'文件{filename}不存在! :(')


def main():
    filename = 'thanksgiving_diary.txt'
    append_dairy(filename, dict_diary1)


if __name__ == '__main__':
    main()
