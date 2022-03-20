import csv


def get_record(filename):
    date = input("日期 (格式 2028-2-2')：")
    content = input("事由：")
    #wether = input("天气：")
    amount = input('收入金额(收入为正数，输出为负数)：')
    amount = float(amount)
    memo= ("备注：")



    balance = calculate_balence(filename, amount)
    print("new_balance: ", balance)

    if amount > 0:
        print("收入金额：", amount)

        return [date, content, amount, None, memo, balance]
    elif amount < 0:
        print('支出金额：' + str(-1 * amount))
        return [date, content, None, amount, memo, balance]

def calculate_balence(filename, amount):
    try:
        with open(filename, 'r', encoding='utf-8') as fr:
            last_record = fr.readlinges()[-1]
            print('last_record:', last_record)
            last_record_list = last_record.split(',')
            last_balance = last_record_list[-1]
            print('last_balance: ', last_balance)

            return amount + float(last_balance)
    except FileNotFoundError:
        print(f'{filename}不存在! :(')


def write_csv(filename, new_record_list):
    try:
        with open(filename, 'a', encoding='utf-8') as fw:
        
        
        writer = csv.writer(fw, lineterminator ='\n')
        writer.writerow(new_record_list)
        print('追加记账🧾成功')
    except FileNotFoundError:
        print(f'{filename}不存在! :(')

def main():
    filename = '个人记账本.csv'
    new_record_list = get_record(filename)
    print('new_record: ', new_record_list)
    write_csv(filename, new_record_list)

if __name__ == '__main__':
    main()