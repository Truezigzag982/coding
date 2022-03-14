dict_diary1 = {
    '当前日期' : '12/3/2022',
    '天气' : '多云',
    '感恩主题' : '时间',
    '感恩内容' : '今天上课我没有迟到。'
}

def init_header(filename, dict_data):
    header = ""
    for key in dict_data:
        header += '%-12s\t' % (key)
    with open(filename, 'w', encoding='utf8') as fw:
        fw.write(header)

def main():
    filename = 'thanksgiving_dairy.txt'
    init_header(filename, dict_diary1)

if __name__ == '__main__':
    main()