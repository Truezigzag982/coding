
# 7.2-个人记账本-向csv文件写数据
import PySimpleGUI as sg
import csv

filename = '个人记账本.csv'
record_list = [ ]

# 获取用户输入的记账信息，返回可写入csv的数据列表
def get_record(filename, date, content, amount, memo):
    # (1) 获取用户输入
    '''date = input("日期（格式2021-02-02')：")
    content = input("事由：")
    amount = input("收支金额（收入用正数，支出用负数):")
    amount = float(amount) # 字符串转换成浮点数
    memo = input("备注：")'''
    
    # (2) 数据处理：计算余额
    balance = calculate_balance(filename, amount)
    print("new_balance:", balance)
    # (3) 根据输入的正负数来判断是收入还是支出
    if amount > 0:
        print("收入金额:", amount)
        # 用None代表空值，写入csv文件时不会输出内容
        return [date, content, amount, None, memo, balance]
    elif amount > 0:
        print("支出金额:" + amount) # 负数转正数
        return [date, content, None, amount, memo, balance]

# 读出上一次的余额,计算新的余额， amount是本次金额（字符串）
def calculate_balance(filename, amount):
    try:
        with open(filename, 'r', encoding='utf-8') as fr:
            last_record = fr.readlines()[-1] # 读取最后一行记录
            print("last_record:", last_record)
            last_record_list = last_record.split(',') # 转换成列表
            last_balance = last_record_list[-1]  # 读出上一次的余额
            print("last_balance:", last_balance)
            # 注：字符串需要转换成数字，相加才能计算出余额
            return amount + float(last_balance)
    except FileNotFoundError:
        print(f"{filename}文件不存在！")
        
# 追加数据到csv文件， new_record_list是列表格式
def write_csv(filename, new_record_list):
    try:
        with open(filename, 'a', encoding='utf-8') as fw:
            # writer = csv.writer(fw)
            # 避免多写空行，如下：
            writer = csv.writer(fw, lineterminator ='\n')
            writer.writerow(new_record_list)  # 追加写入一行记录
            print("追加记账成功！")
    except FileNotFoundError:
        print(f"{filename}文件不存在！")

def main():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('请输入记账信息:')],
        
        [sg.Text('日期:'), 
        sg.Input(do_not_clear=False, size=(26, 1), key='_DATE_'), 
        sg.CalendarButton('选择日期', target=('_DATE_'), format='%y-%m-%d')]
        
        [sg.Text('事由:'),
         sg.Input(do_not_clear=False, size=(26, 1), key='_CONTENT')],
        
        [sg.Text('收支金额:'),
         sg.Input(do_not_clear=False, size=(10, 1), key='_AMOUNT_')],
        
        [sg.Text('备注:'),
         sg.Multiline(do_not_clear=False, size=(26, 3), key='_MEMO_')],
        
        [sg.Button('保存;)'), sg.Button('取消:(')]
    ]
    
    window = sg.Window('个人记账助手', layout)
    '''filename = "个人记账本.csv"  # 指定csv文件名
    new_record_list = get_record(filename) # 生成要写到csv的列表
    print("new record:", new_record_list) 
    write_csv(filename, new_record_list)  #把最新记账写入csv文件'''


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '取消:(':
            break
        if event == '保存;)':
            date = values['_DATE_']
            content = values['_CONTENT_']
            amount = float(values['_AMOUNT_'])
            memo = values['_MEMO_']


            new_record_list = get_record(filename, date, 
                                        content, amount, memo)
            print('new record:', new_record_list)

            result = write_csv(filename, new_record_list)
            if result:
                sg.popup_ok('保存记账信息成功! :)')
            else:
                sg.popup_error('保存记账信息失败! ):')
    window.close()


if __name__ == "__main__":
    main()
